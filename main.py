from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Any
import requests
import json
import logging
import threading
from loguru import logger
import os 
from dotenv import load_dotenv
import re

load_dotenv()

LOG_PATH = os.getenv("LOG_PATH")
FIREWORKS_URL = os.getenv("FIREWORKS_URL")
FIREWORKS_TOKEN = os.getenv("FIREWORKS_TOKEN")
FIREWORKS_API_MAX_TOKEN = os.getenv("FIREWORKS_API_MAX_TOKEN")
TEMPERATURE = os.getenv("TEMPERATURE")
FIREWORKS_MODEL = os.getenv("FIREWORKS_MODEL")

logger.add(LOG_PATH + "{time}.log", rotation="1 day")

app = FastAPI()

# Set up CORS middleware
origins = [
    "http://localhost",
    "http://localhost:8080",
    # Add other allowed origins here
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InferenceRequest(BaseModel):
    content_input: str
    main_brand: str

class InferenceResponse(BaseModel):
    result: Any


def extract_json_from_text(text):
    json_pattern = re.compile(r'{.*}', re.DOTALL)
    match = json_pattern.search(text)

    if match:
        json_str = match.group()
        try:
            data = json.loads(json_str)
            return data
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return None
    else:
        print("No JSON found in the text.")
        return None

def process_inference(content_input: str, main_brand: str):

    url = FIREWORKS_URL
    # payload = {
    #     "model": FIREWORKS_MODEL,
    #     "max_tokens": int(FIREWORKS_API_MAX_TOKEN),
    #     "top_p": 1,
    #     "top_k": 40,
    #     "presence_penalty": 0,
    #     "frequency_penalty": 0,
    #     "temperature": float(TEMPERATURE),
    #     "messages": [
    #         {
    #             "role": "user",
    #             "content": (
    #                 "Analyze the provided text to extract relevant data related to the main brand based on the identified sentiment "
    #                 "and return the result in JSON format.\n\nMain Brand: <main_brand>\n\nCriteria:\n\nsentiment: The sentiment towards the main brand, "
    #                 "with possible values: POSITIVE, NEGATIVE, NEUTRAL, MIXED\nseverity: An assessment of the severity of the sentiment, possible values: "
    #                 "LOW, MEDIUM, HIGH, VERY HIGH, CRITICAL\nemotion: Evaluation of the emotion expressed towards the main brand, possible values: Anger, "
    #                 "Disgust, Fear, Happiness, Sadness, Surprise, Interest, Joy\npolarity: The degree of emotion expressed in relation to the main brand, "
    #                 "ranging from -1 to 1\nintensity: The intensity of the emotion expressed towards the main brand, possible values: LOW, MEDIUM, HIGH\n"
    #                 "topic: The main topic of the text, determined by the language model\nsubtopic: Subtopics related to the main topic, determined by the "
    #                 "language model\ncategory: Prediction of the field to which the text belongs\nindustry: Prediction of the industry to which the text belongs\n"
    #                 "subject: The person or entity mentioned in the text, empty if none\nproduct_type: The type of product mentioned in the text, empty if none\n"
    #                 "angle: The perspective mentioned in the text, empty if none\nentity_recognition: Entities mentioned in the text, possible values: Person, "
    #                 "Location, Organization, Product, Event\nintent: The intent expressed in the text, one or more of the following values: Help, Search, Booking, "
    #                 "Payment, Feedback, Complaint\npurpose: The purpose stated in the text, empty if none\ntone: The tone(s) expressed in the text, possible values: "
    #                 "Friendly, Informal, Positive, Excited\naudience: The audience mentioned in the text, empty if none\nmention_mainbrand: true if the main brand "
    #                 "exists, false otherwise\ncontext:\nkeyword: Words or phrases related to the main brand.\nexplanation: A brief summary or statement reflecting "
    #                 "the sentiment towards the main brand."
    #             )
    #         },
    #         {
    #             "role": "assistant",
    #             "content": (
    #                 "I'll analyze the text and extract the relevant data related to the main brand based on the identified sentiment. Please provide the text, "
    #                 "and I'll return the result in JSON format.\n\nPlease note that I'll assume that the text is a review, comment, or any other type of text that "
    #                 "expresses an opinion about the main brand. If the text is not a review or opinion, please let me know, and I'll adjust my analysis accordingly.\n\n"
    #                 "Please provide the text, and I'll get started!"
    #             )
    #         },
    #         {
    #             "role": "user",
    #             "content": f"content: \"{content_input}\"\nmain_brand: \"{main_brand}\""
    #         }
    #     ]
    # }
    
    payload = {
    "model": FIREWORKS_MODEL,
    "max_tokens": int(FIREWORKS_API_MAX_TOKEN),
    "top_p": 1,
    "top_k": 40,
    "presence_penalty": 0,
    "frequency_penalty": 0,
    "temperature": float(TEMPERATURE),
    "messages": [
        {
            "role": "user",
            "content": (
                "Analyze the provided text to extract relevant data related to the main brand based on the identified sentiment "
                "and return the result in JSON format.\n\nMain Brand: [<main_brand>]\n\nCriteria:\n\nsentiment: [The sentiment towards the main brand, "
                "with possible values: POSITIVE, NEGATIVE, NEUTRAL, MIXED]\nseverity: [An assessment of the severity of the sentiment, possible values: "
                "LOW, MEDIUM, HIGH, VERY HIGH, CRITICAL]\nemotion: [Evaluation of the emotion expressed towards the main brand, possible values: Anger, "
                "Disgust, Fear, Happiness, Sadness, Surprise, Interest, Joy]\npolarity: [The degree of emotion expressed in relation to the main brand, "
                "ranging from -1 to 1]\nintensity: [The intensity of the emotion expressed towards the main brand, possible values: LOW, MEDIUM, HIGH]\n"
                "topic: [The main topic of the text, determined by the language model]\nsubtopic: [Subtopics related to the main topic, determined by the "
                "language model]\ncategory: [Prediction of the field to which the text belongs]\nindustry: [Prediction of the industry to which the text belongs]\n"
                "subject: [The person or entity mentioned in the text, empty if none]\nproduct_type: [The type of product mentioned in the text, empty if none]\n"
                "angle: [The perspective mentioned in the text, empty if none]\nentity_recognition: [A list of objects containing entities mentioned in the text, "
                "each with:\n  - type: The type of entity (e.g., Organization, Product)\n  - value: The entity value mentioned in the text]\n"
                "intent: [The intent expressed in the text, one or more of the following values: Help, Search, Booking, "
                "Payment, Feedback, Complaint]\npurpose: [The purpose stated in the text, empty if none]\ntone: [The tone(s) expressed in the text, possible values: "
                "Friendly, Informal, Positive, Excited]\naudience: [The audience mentioned in the text, empty if none]\nmention_mainbrand: [true if the main brand "
                "exists, false otherwise]\ncontext:\nkeyword: [A list of objects containing words, phrases, or sentences related to the main brand, each with:\n"
                "  - sentiment: The sentiment of the keyword, which must match the sentiment of the main text (POSITIVE, NEGATIVE, MIXED)\n"
                "  - value: The word, phrase, or sentence that clearly expresses the sentiment]\nexplanation: [A brief summary or statement reflecting "
                "the sentiment towards the main brand.]"
                "spam: Determine if the text being analyzed is spam, the result is a string with the value 'YES' or 'NO'\n"
                "advertisement: Determine if the text being analyzed is advertising a product or service, the result is a string with the value 'YES' or 'NO'\n\n"
            )
        },
        {
            "role": "assistant",
            "content": (
                "I'll analyze the text and extract the relevant data related to the main brand based on the identified sentiment. Please provide the text, "
                "and I'll return the result in JSON format.\n\nPlease note that I'll assume that the text is a review, comment, or any other type of text that "
                "expresses an opinion about the main brand. If the text is not a review or opinion, please let me know, and I'll adjust my analysis accordingly.\n\n"
                "Please provide the text, and I'll get started!"
            )
        },
        {
            "role": "user",
            "content": f"content: \"{content_input}\"\nmain_brand: [\"{main_brand}\"]"
        }
    ]
}

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {FIREWORKS_TOKEN}"
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        logger.info(f"Job completed for main_brand: {main_brand}")

        response_data = response.json()
        llm_response = response_data['choices'][0]['message']['content']
        if llm_response:
            inference = extract_json_from_text(llm_response)
            result = {
                "id": response.json()['id'],
                "created": response.json()['created'],
                "model": response.json()['model'],
                "inference": inference,
                "usage": response.json()['usage'],

            }
            return result
        else:
            return None
    else:
        logger.error(f"Failed to process inference: {response.text}")
        response.raise_for_status()

@app.post("/inference", response_model=InferenceResponse)
def inference_endpoint(request: InferenceRequest):
    try:
        # Use threading to handle the request
        result = {}
        thread = threading.Thread(
            target=lambda: result.update({"data": process_inference(request.content_input, request.main_brand)}))
        thread.start()
        thread.join()
        return InferenceResponse(result=result["data"])
    except Exception as e:
        logger.error(f"Error during inference: {str(e)}")
        raise HTTPException(status_code=500, detail="Inference processing failed")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
