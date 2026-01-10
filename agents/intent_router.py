
def intent_router_agent(problem_text: str):
    """
    Classifies the math problem using Keyword Matching (No LLM).
    """
    text = problem_text.lower()
    
    # 1. Define Keywords for Topics
    topics = {
        "Calculus": ["integral", "derivative", "limit", "dx", "dy/dx", "area under curve", "slope of tangent"],
        "Probability": ["probability", "chance", "dice", "coin", "card", "bayes", "distribution", "mean", "variance"],
        "Linear Algebra": ["matrix", "determinant", "eigen", "vector", "cross product", "dot product"],
        "Geometry": ["triangle", "circle", "area", "volume", "angle", "radius", "perimeter"],
        "Algebra": ["solve", "equation", "roots", "quadratic", "polynomial", "system", "find x", "inequality"]
    }
    
    # 2. Check for Basic Arithmetic (Pure numbers and symbols)
    # If the text contains ONLY numbers and + - * / ( ) . ^
    is_basic = True
    allowed_chars = set("0123456789+-*/().^ \t\n")
    for char in text:
        if char not in allowed_chars:
            is_basic = False
            break
            
    if is_basic and any(op in text for op in "+-*/^"):
        return {
            "topic": "Basic Arithmetic",
            "difficulty": "Easy",
            "required_tools": ["calculator"]
        }

    # 3. Score Topics
    scores = {t: 0 for t in topics}
    for topic, keywords in topics.items():
        for kw in keywords:
            if kw in text:
                scores[topic] += 1
                
    # 4. Determine Winner
    best_topic = "Unknown"
    max_score = 0
    
    for topic, score in scores.items():
        if score > max_score:
            max_score = score
            best_topic = topic
            
    # Default to Algebra if variables exist but no specific keywords
    if best_topic == "Unknown":
        import re
        if re.search(r'[a-z]', text):
            best_topic = "Algebra"

    return {
        "topic": best_topic,
        "difficulty": "Medium" if max_score > 0 else "Unknown",
        "required_tools": []
    }
