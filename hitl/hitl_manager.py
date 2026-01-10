def check_confidence(agent_output):
    """
    Evaluates if human intervention is needed based on confidence scores.
    """
    confidence = agent_output.get("confidence", 1.0)
    
    if confidence < 0.7:
        return {
            "trigger": True,
            "reason": f"Low confidence score ({confidence})"
        }
        
    if agent_output.get("needs_clarification"):
        return {
            "trigger": True,
            "reason": "Agent explicitly requested clarification"
        }
        
    return {
        "trigger": False,
        "reason": None
    }
