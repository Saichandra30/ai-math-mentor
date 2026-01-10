
import re

def parser_agent(raw_text: str):
    """
    Cleans and structures the raw input text using Regex (No LLM).
    """
    if not raw_text or len(raw_text.strip()) < 2:
         return {
            "problem_text": None,
            "topic": None,
            "variables": [],
            "constraints": [],
            "needs_clarification": True,
            "clarification_question": "Input is empty or too short."
        }

    # 1. Clean Text
    # Normalize spaces
    clean_text = " ".join(raw_text.split())
    # Common OCR fix (e.g., 'l' vs '1' or '|' is context dependent, but we'll keep it simple)
    
    # 2. Extract Variables
    # Remove common words first to avoid false positives
    stopwords = ["solve", "find", "calculate", "evaluate", "simplify", "what", "is", "the", "value", "of", "in", "equation", "linear", "quadratic"]
    
    # Case-insensitive removal of whole words
    temp_text = clean_text
    for word in stopwords:
        temp_text = re.sub(r'\b' + word + r'\b', '', temp_text, flags=re.IGNORECASE)
        
    # Regex to find single letters possibly preceded by digits (e.g., 2x, x, 5y)
    # \b matches boundary, \d* matches optional number, ([a-zA-Z]) captures the letter, \b matches boundary
    # This avoids matching parts of larger words left over, but might miss if sticky.
    # Safe approach: strict single letter check after cleaning keywords.
    
    matches = re.findall(r'\b\d*([a-zA-Z])\b', temp_text)
    
    variables = sorted(list(set(matches)))

    # 3. Ambiguity Check
    is_ambiguous = False
    clarification = None
    
    # If no numbers and no variables??
    if not re.search(r'[0-9]', clean_text) and not sorted_vars:
        is_ambiguous = True
        clarification = "No numbers or variables detected. Is this a math problem?"

    return {
        "problem_text": clean_text,
        "topic": "Pending Router", 
        "variables": variables,
        "constraints": [], 
        "needs_clarification": is_ambiguous,
        "clarification_question": clarification
    }
