import json
import re

def clean_and_parse_json(response_text):
    cleaned_text = re.sub(r',\\s*([\\]}])', r'\\1', response_text)
    json_start = cleaned_text.find('{')
    json_end = cleaned_text.rfind('}') + 1
    if json_start == -1 or json_end == -1:
        return {"clauses": {}, "obligations": {}}
    cleaned_text = cleaned_text[json_start:json_end]
    try:
        parsed_json = json.loads(cleaned_text)
    except json.JSONDecodeError:
        parsed_json = {"clauses": {}, "obligations": {}}
    return parsed_json
