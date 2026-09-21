import json

json_string = '{"name": "Alice", "address": {"city": "Delhi", "pin": 110001}}'

data = json.loads(json_string)

def contains_complex_object(obj):
    if isinstance(obj, dict):
        for value in obj.values():
            if isinstance(value, (dict, list)):
                return True
            if contains_complex_object(value):
                return True

    elif isinstance(obj, list):
        for item in obj:
            if isinstance(item, (dict, list)):
                return True
            if contains_complex_object(item):
                return True

    return False

if contains_complex_object(data):
    print("The JSON string contains a complex object.")
else:
    print("The JSON string does not contain a complex object.")
