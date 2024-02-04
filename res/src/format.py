def openai_format(response: str, model: str) -> str:
    
    return {
        "choices": [
            {
            "finish_reason": "stop",
            "index": 0,
            "message": {
                "content": f"{response}",
                "role": "assistant"
                }
            }
        ],                                 
        "model": f"{model}",
        "object": "chat.completion",
    }