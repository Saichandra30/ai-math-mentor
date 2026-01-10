from utils.llm_client import query_llm
import json
import re
import math

def solve_linear_equation(text):
    """ Matches: 2x + 5 = 11 """
    match = re.search(r'([-]?\d*)x\s*\+\s*([-]?\d+)\s*=\s*([-]?\d+)', text)
    if not match: return None
    
    a_str, b_str, c_str = match.groups()
    a = 1 if a_str in ["", "+"] else -1 if a_str == "-" else int(a_str)
    b, c = int(b_str), int(c_str)
    
    rhs = c - b
    res = rhs / a if a != 0 else 0
    
    return {
        "solution": str(res),
        "steps": [
            f"Identified Linear Equation: {a}x + {b} = {c}",
            f"Subtract {b}: {a}x = {rhs}",
            f"Divide by {a}: x = {res}"
        ],
        "confidence": 1.0, 
        "error": None
    }

def solve_probability_binom(text):
    """ Matches: P(3 heads in 5 coin tosses) """
    # Regex for "P(k heads/tails in n ...)"
    match = re.search(r'P\(\s*(\d+)\s*(?:heads|tails).*?in\s*(\d+)', text, re.IGNORECASE)
    if not match: return None
    
    k, n = map(int, match.groups())
    
    # nCk * (0.5)^n
    if k > n: return None
    combinations = math.comb(n, k)
    prob = combinations * (0.5 ** n)
    
    return {
        "solution": f"{prob:.4f}",
        "steps": [
            f"Identified Binomial Probability: P(X={k}) with n={n}, p=0.5",
            f"Formula: C({n}, {k}) * (0.5)^{n}",
            f"Combinations: {n}C{k} = {combinations}",
            f"Calculation: {combinations} * {0.5**n} = {prob}"
        ],
        "confidence": 1.0,
        "error": None
    }

def solve_quadratic(text):
    """ Matches: roots of x^2 - 5x + 6 = 0 """
    # Simple parser for ax^2 + bx + c = 0
    # Assumes standard form for simplicity in fallback mode
    match = re.search(r'([-]?\d*)x\^2\s*([+-]\s*\d+)x\s*([+-]\s*\d+)\s*=\s*0', text.replace(" ", ""))
    if not match: return None
    
    a_str, b_str, c_str = match.groups()
    a = 1 if a_str in ["", "+"] else -1 if a_str == "-" else int(a_str)
    b = int(b_str.replace("+", ""))
    c = int(c_str.replace("+", ""))
    
    D = b**2 - 4*a*c
    
    if D < 0:
        return {"solution": "Complex Roots", "steps": [f"Discriminant D = {D} < 0"], "confidence": 1.0, "error": None}
        
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    
    return {
        "solution": f"{x1}, {x2}",
        "steps": [
            f"Quadratic Formula: ax^2+bx+c=0 (a={a}, b={b}, c={c})",
            f"Discriminant D = b^2 - 4ac = {D}",
            f"Roots: (-{b} ± √{D}) / {2*a}",
            f"x1 = {x1}, x2 = {x2}"
        ],
        "confidence": 1.0, 
        "error": None
    }

def solver_agent(problem_text, retrieved_chunks, topic=None):
    """
    Hybrid Solver with robust Offline Fallbacks.
    """
    
    # 1. Try Deterministic Solvers (The "Pattern Math" Layer)
    clean_text = problem_text.replace(" ", "").lower()
    
    # Basic Arithmetic
    if topic == "Basic Arithmetic":
        try:
            allowed = set("0123456789+-*/().^ \t\n")
            if all(c in allowed for c in problem_text):
                return {"solution": str(eval(problem_text.replace("^","**"))), "steps": ["Calculated safely"], "confidence": 1.0, "error": None}
        except: pass

    # Patterns
    if "x=" in clean_text or "x+" in clean_text or "x^2" in clean_text:
        res = solve_quadratic(problem_text)
        if res: return res
        res = solve_linear_equation(problem_text)
        if res: return res
        
    if "p(" in clean_text:
        res = solve_probability_binom(problem_text)
        if res: return res

    # 2. Try RAG + LLM
    context_str = "\n\n".join(retrieved_chunks) if retrieved_chunks else "No specific context available."
    prompt = f"""
    Solve this math problem step-by-step.
    Context: {context_str}
    Problem: {problem_text}
    Return JSON: {{ "steps": [], "solution": "", "confidence": float }}
    """
    
    response_text = query_llm(prompt)
    
    # 3. Handle LLM Failure
    if "Error" in response_text: # Generic check
        return {
            "solution": "Error",
            "steps": ["The advanced reasoning engine is currently unavailable.", "Try checking your internet or local AI service."],
            "confidence": 0.0,
            "error": "AI Service Unavailable"
        }

    # Process Success
    response_text = response_text.replace("```json", "").replace("```", "").strip()
    try:
        data = json.loads(response_text)
        return {
            "solution": data.get("solution", "Unknown"),
            "steps": data.get("steps", []),
            "confidence": data.get("confidence", 0.5),
            "error": None
        }
    except:
        return {
            "solution": "See steps",
            "steps": [response_text],
            "confidence": 0.5,
            "error": "Failed to parse solution"
        }
