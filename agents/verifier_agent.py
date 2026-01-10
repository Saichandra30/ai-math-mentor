def verifier_agent(problem_text, solution):
    """
    Verify the solution by substituting back into equation.
    """

    try:
        import re

        match = re.search(r"([0-9]+)x\s*\+\s*([0-9]+)\s*=\s*([0-9]+)", problem_text)

        if not match:
            return {
                "verified": False,
                "reason": "Unsupported verification format"
            }

        a = int(match.group(1))
        b = int(match.group(2))
        c = int(match.group(3))

        lhs = a * solution + b

        if abs(lhs - c) < 1e-6:
            return {
                "verified": True,
                "reason": "Solution verified successfully"
            }

        return {
            "verified": False,
            "reason": "Substitution check failed"
        }

    except Exception as e:
        return {
            "verified": False,
            "reason": str(e)
        }
