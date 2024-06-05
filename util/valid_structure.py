
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


def validate_structure(data):
    if isinstance(template, dict):
        if not isinstance(data, dict):
            return False
        for key, sub_template in template.items():
            if key not in data:
                return False
            if not validate_structure(data[key], sub_template):
                return False
    elif isinstance(template, list):
        if not isinstance(data, list):
            return False
        if len(template) > 0:
            sub_template = template[0]
            for item in data:
                if not validate_structure(item, sub_template):
                    return False
    else:
        return isinstance(data, type(template))
    return True
