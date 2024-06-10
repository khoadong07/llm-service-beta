def llm_json_template():
    template = {
        "sentiment": "",
        "severity": "",
        "emotion": "",
        "polarity": 0.0,
        "intensity": "",
        "topic": "",
        "subtopic": "",
        "category": "",
        "industry": "",
        "subject": "",
        "product_type": "",
        "angle": "",
        "entity_recognition": [
            {
                "type": "",
                "value": ""
            }
        ],
        "intent": "",
        "purpose": "",
        "tone": "",
        "audience": "",
        "mention_mainbrand": False,
        "context": [
            {
                "sentiment": "",
                "value": ""
            }
        ],
        "explanation": "",
        "spam": "",
        "advertisement": ""
    }
    return template