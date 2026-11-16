api_response = {
    "id": "resp_98234",
    "model": "gpt-4o",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "SVD decomposes a matrix into three orthogonal components."
            },
            "finish_reason": "stop"
        }
    ],
    "usage": {
        "prompt_tokens": 120,
        "completion_tokens": 45,
        "total_tokens": 165
    }
}
broken_response = {"error": "timeout"}
def calculate_cost(response: dict, prompt_price_per_1k: float = 0.005, completion_price_per_1k: float = 0.015) -> float:
    token1 = response["usage"]["prompt_tokens"]
    token2 = response["usage"]["completion_tokens"]
    return token1*prompt_price_per_1k/1000 + completion_price_per_1k*token2/1000
print(round(calculate_cost(api_response),6))
def extract_answer(response: dict) -> str:
    try:
        answer = response["choices"][0]["message"]["content"]
        return answer
    except(KeyError, IndexError):
        return "Error: invalid response format"
print(extract_answer(api_response))
print(extract_answer(broken_response))