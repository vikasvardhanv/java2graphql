import json

def is_integer(value):
    return isinstance(value, int)

def is_boolean(value):
    return isinstance(value, bool)

def is_number(value):
    return isinstance(value, (int, float))

def is_object(value):
    return isinstance(value, dict)

def json_to_schema(json_input):
    try:
        data = json.loads(json_input)
        types = {}
        generate_graphql_schema(data, "GeneratedMainType", types)
        return '\n'.join(types.values())
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON input provided.")

def generate_graphql_schema(data, name, types):
    if name in types:
        return name

    fields = []
    for key, value in data.items():
        field_type = convert_type(value, key, types)
        fields.append(f"  {key}: {field_type}")

    types[name] = f"type {name} {{\n" + '\n'.join(fields) + "\n}"
    return name

def convert_type(value, key, types):
    if is_boolean(value):
        return "Boolean"
    elif is_integer(value):
        return "Int"
    elif is_number(value):
        return "Float"
    elif is_object(value):
        type_name = f"{key.capitalize()}"
        return generate_graphql_schema(value, type_name, types)
    elif isinstance(value, list):
        if len(value) > 0 and is_object(value[0]):
            type_name = f"{key.capitalize()}"
            item_type = generate_graphql_schema(value[0], type_name, types)
            return f"[{item_type}]"
        else:
            return "[String]"
    else:
        return "String"

def transformer(value):
    return json_to_schema(value)