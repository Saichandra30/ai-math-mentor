from typing import TypedDict, List, Optional, Any, Dict
from langgraph.graph import StateGraph, END

# Import existing agents
from agents.parser_agent import parser_agent
from agents.intent_router import intent_router_agent
from agents.solver_agent import solver_agent
from agents.verifier_agent import verifier_agent
from agents.explainer_agent import explainer_agent
from rag.retriever import retrieve_context

# Define the State
class AgentState(TypedDict):
    input_text: str
    parsed_data: Optional[Dict[str, Any]]
    topic: Optional[str]
    retrieved_chunks: Optional[List[str]]
    solver_output: Optional[Dict[str, Any]]
    verification_result: Optional[Dict[str, Any]]
    explanation: Optional[str]
    messages: List[str] # For logging/trace

# Define Nodes

def parser_node(state: AgentState) -> AgentState:
    text = state["input_text"]
    parsed = parser_agent(text)
    return {
        "parsed_data": parsed,
        "messages": state["messages"] + [f"Parsed: {parsed.get('problem_text')}"]
    }

def router_node(state: AgentState) -> AgentState:
    text = state["parsed_data"]["problem_text"]
    intent = intent_router_agent(text)
    return {
        "topic": intent.get("topic"),
        "messages": state["messages"] + [f"Routed to: {intent.get('topic')}"]
    }

def retriever_node(state: AgentState) -> AgentState:
    text = state["parsed_data"]["problem_text"]
    chunks = retrieve_context(text)
    return {
        "retrieved_chunks": chunks,
        "messages": state["messages"] + [f"Retrieved {len(chunks)} context chunks"]
    }

def solver_node(state: AgentState) -> AgentState:
    text = state["parsed_data"]["problem_text"]
    chunks = state["retrieved_chunks"]
    topic = state["topic"]
    
    solution = solver_agent(text, chunks, topic)
    return {
        "solver_output": solution,
        "messages": state["messages"] + ["Solved problem"]
    }

def verifier_node(state: AgentState) -> AgentState:
    text = state["parsed_data"]["problem_text"]
    sol_val = state["solver_output"].get("solution")
    
    # Only verify if we have a valid solution value to check
    # The current verifier expects a specific format, so we handle safely
    try:
        verification = verifier_agent(text, sol_val)
    except:
        verification = {"verified": False, "reason": "Verification skipped or failed"}
        
    return {
        "verification_result": verification,
        "messages": state["messages"] + [f"Verification: {verification.get('verified')}"]
    }

def explainer_node(state: AgentState) -> AgentState:
    text = state["parsed_data"]["problem_text"]
    solution = state["solver_output"]
    
    explanation = explainer_agent(text, solution.get("steps", []), solution.get("solution"))
    return {
        "explanation": explanation,
        "messages": state["messages"] + ["Generated explanation"]
    }

# Conditional Logic
def check_ambiguity(state: AgentState):
    if state["parsed_data"].get("needs_clarification"):
        return "end"
    return "continue"

def check_confidence(state: AgentState):
    sol = state["solver_output"]
    if sol and (sol.get("confidence", 0.0) < 0.6 or sol.get("solution") == "Error"):
        return "flag_hitl"
    return "continue"

# Build Graph
builder = StateGraph(AgentState)

builder.add_node("parser", parser_node)
builder.add_node("router", router_node)
builder.add_node("retriever", retriever_node)
builder.add_node("solver", solver_node)
builder.add_node("verifier", verifier_node)
builder.add_node("explainer", explainer_node)

# Flow
builder.set_entry_point("parser")

builder.add_conditional_edges(
    "parser",
    check_ambiguity,
    {
        "end": END,
        "continue": "router"
    }
)

builder.add_edge("router", "retriever")
builder.add_edge("retriever", "solver")

builder.add_conditional_edges(
    "solver",
    check_confidence,
    {
        "flag_hitl": END,
        "continue": "verifier"
    }
)

builder.add_edge("verifier", "explainer")
builder.add_edge("explainer", END)

# Compile
graph = builder.compile()
