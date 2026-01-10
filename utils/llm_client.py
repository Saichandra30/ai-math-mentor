
import ollama

def query_llm(prompt: str, model: str = "llama3") -> str:
    """
    Query the local Ollama LLM.
    Returns the response string.
    """
    try:
        response = ollama.chat(model=model, messages=[
            {
                'role': 'user',
                'content': prompt,
            },
        ])
        return response['message']['content']
    except Exception as e:
        print(f"Error querying LLM: {e}")
        return "Error: Unable to generate response. Ensure Ollama is running."
