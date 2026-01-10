import json
import os
from difflib import SequenceMatcher

MEMORY_FILE = "memory/experiences.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []
    try:
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_memory(experiences):
    os.makedirs("memory", exist_ok=True)
    with open(MEMORY_FILE, "w") as f:
        json.dump(experiences, f, indent=2)

def save_experience(problem, solution, verification_status):
    """
    Saves a problem-solution pair properly verified.
    """
    history = load_memory()
    entry = {
        "problem": problem,
        "solution": solution,
        "verified": verification_status
    }
    history.append(entry)
    save_memory(history)

def find_similar_problem(current_problem):
    """
    Basic fuzzy search for similar past problems.
    Returns the best match logic.
    """
    history = load_memory()
    best_match = None
    highest_ratio = 0.0
    
    for item in history:
        ratio = SequenceMatcher(None, current_problem, item["problem"]).ratio()
        if ratio > 0.8: # Threshold for similarity
            if ratio > highest_ratio:
                highest_ratio = ratio
                best_match = item
                
    return best_match
