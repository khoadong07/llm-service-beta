import re
import json

def extract_json_from_string(json_string):
    pattern = r'\{.*\}'
    match = re.search(pattern, json_string, re.DOTALL)

    if match:
        extracted_json = match.group()
        try:
            data = json.loads(extracted_json)
            return data
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return None
    else:
        return None