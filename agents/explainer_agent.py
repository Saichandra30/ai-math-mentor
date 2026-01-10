from utils.llm_client import query_llm

def explainer_agent(problem_text: str, solution_steps: list, final_answer):
    """
    Generates a student-friendly explanation of the solution.
    Fallback: Returns simple formatted text if LLM is down.
    """
    steps_str = "\n".join(solution_steps)
    
    prompt = f"""
    You are a helpful math tutor. Explain the solution to this problem step-by-step to a student.
    
    Problem: {problem_text}
    
    Technical Steps Performed:
    {steps_str}
    
    Final Answer: {final_answer}
    
    Write a clear, encouraging explanation. Point out key concepts or formulas used.
    """
    
    response = query_llm(prompt)
    
    # Generic error check (covers "Error", "Ollama", "Connection", etc)
    if "Error" in response or "Unable" in response:
        # Fallback explanation
        return f"""
        **Explanation (Offline Mode)**
        
        To solve **{problem_text}**, we followed these steps:
        
        {steps_str}
        
        And arrived at the final answer: **{final_answer}**.
        
        *(Note: The AI tutor service is currently unavailable, but the calculation above uses verified formulas.)*
        """
        
    return response
