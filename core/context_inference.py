from http.client import HTTPException
from typing import List

import requests
from config import settings
from model.inference_model import Comment
from prompt.bank import context_prompt, context_sentiment
import json

from util.extract_json import extract_json_from_string


def context_inference(content_input: str, comment_input: List[Comment]):
    """Process inference to determine context sentiment.

    Args:
        content_input (str): The content of the post.
        comment_input (list): A list of comments.

    Returns:
        dict: The inference result.
    """
    url = settings.FIREWORKS_URL
    comments_str = ', '.join([f'{{"id": "{comment.id}", "content": "{comment.content}"}}' for comment in comment_input])
    payload = {
        "model": settings.FIREWORKS_MODEL,
        "max_tokens": int(settings.FIREWORKS_API_MAX_TOKEN),
        "top_p": 1,
        "top_k": 40,
        "presence_penalty": 0,
        "frequency_penalty": 0,
        "temperature": float(settings.TEMPERATURE),
        "messages": context_sentiment(content_input=content_input, comment_input=comments_str)
    }

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {settings.FIREWORKS_TOKEN}"
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))


    if response.status_code == 200:
        response_data = response.json()
        # print(response_data)
        llm_response = response_data['choices'][0]['message']['content']
        if llm_response:
            print(llm_response)
            core = extract_json_from_string(llm_response)
            print(core)
            result = {
                "id": response.json()['id'],
                "created": response.json()['created'],
                "model": response.json()['model'],
                "core": core,
                "usage": response.json()['usage'],

            }
            return result
        else:
            return None
    else:
        response.raise_for_status()


