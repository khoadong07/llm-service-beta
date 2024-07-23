import requests
import json
from config import settings
from core.template import llm_json_template
from prompt.bank import llm_prompt
from prompt.general import general_prompt
from util.extract_json import extract_json_from_string
from loguru import logger

from util.ner_extraction import merge_and_filter_entities


def process_inference(content_input: str, main_brand: str):
    """AI is creating summary for process_inference

    Args:
        content_input (str): [description]
        main_brand (str): [description]

    Returns:
        [type]: [description]
    """
    url = settings.FIREWORKS_URL
    payload = {
        "model": settings.FIREWORKS_MODEL,
        "max_tokens": int(settings.FIREWORKS_API_MAX_TOKEN),
        "top_p": 1,
        "top_k": 40,
        "presence_penalty": 0,
        "frequency_penalty": 0,
        "temperature": float(settings.TEMPERATURE),
        "messages": llm_prompt(main_brand=main_brand, content_input=content_input, template=llm_json_template())
    }

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {settings.FIREWORKS_TOKEN}"
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        logger.info(f"Job completed for main_brand: {main_brand}")

        response_data = response.json()
        # print(response_data)
        llm_response = response_data['choices'][0]['message']['content']
        if llm_response:
            core = extract_json_from_string(llm_response)
            print(core)
            result = {
                "id": response.json()['id'],
                "created": response.json()['created'],
                "model": response.json()['model'],
                "core": core,
                "usage": response.json()['usage'],

            }
            # print(result)
            return result
        else:
            # print("tạch")
            return None
    else:
        logger.error(f"Failed to process core: {response.text}")
        response.raise_for_status()

from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

tokenizer = AutoTokenizer.from_pretrained("NlpHUST/ner-vietnamese-electra-base")
model = AutoModelForTokenClassification.from_pretrained("NlpHUST/ner-vietnamese-electra-base")

nlp = pipeline("ner", model=model, tokenizer=tokenizer)


def check_json_response(response):
    expected_fields = [
        "sentiment", "severity", "emotion", "polarity", "intensity", "topic", "subtopic",
        "category", "industry", "subject", "product_type", "angle", "intent", "purpose",
        "tone", "audience", "mention_mainbrand", "context", "explanation", "spam",
        "advertisement", "opinion_expressed", "emotional_tone", "feedback_provided",
        "insight_provided", "entity_recognition"
    ]

    for field in expected_fields:
        if field not in response:
            print(f"Missing field: {field}")
            return None

    for field in response:
        if response[field] == "None":
            response[field] = None
        elif isinstance(response[field], list):
            for item in response[field]:
                if isinstance(item, dict):
                    for key in item:
                        if item[key] == "None":
                            item[key] = None

    return response


def general_inference(main_brand, content_input):
    ner_results = nlp(content_input)

    merged_entities = merge_and_filter_entities(ner_results)
    entity_array = []
    for entity in merged_entities:
        entity_array.append(entity)
    url = settings.FIREWORKS_URL
    payload = {
        "model": settings.FIREWORKS_MODEL,
        "max_tokens": int(settings.FIREWORKS_API_MAX_TOKEN),
        "top_p": 1,
        "top_k": 40,
        "presence_penalty": 0,
        "frequency_penalty": 0,
        "temperature": float(settings.TEMPERATURE),
        "messages": general_prompt(main_brand=main_brand, content=content_input)
    }

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {settings.FIREWORKS_TOKEN}"
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        logger.info(f"Job completed for main_brand: {main_brand}")

        response_data = response.json()
        llm_response = response_data['choices'][0]['message']['content']
        if llm_response:
            core = extract_json_from_string(llm_response)
            core.update({'entity_recognition': entity_array})

            validated_core = check_json_response(core)
            result = {
                "id": response.json()['id'],
                "created": response.json()['created'],
                "model": response.json()['model'],
                "core": validated_core,
                "usage": response.json()['usage']
            }
            return result
        else:
            return None
    else:
        logger.error(f"Failed to process core: {response.text}")
        response.raise_for_status()


def retry_general_inference(main_brand, content_input, max_retries=5):
    for attempt in range(max_retries):
        print(f"Attempt {attempt + 1}/{max_retries}")
        result = general_inference(main_brand, content_input)
        if result.get('core') is not None:
            return result
        else:
            logger.warning("Invalid response, retrying...")

    logger.error("Max retries reached, failed to generate a valid response.")
    return None