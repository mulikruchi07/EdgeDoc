import re

def extract_dynamic_fields(text):
    data = {}

    lines = text.split('\n')

    for line in lines:
        line = line.strip()

        if len(line) < 3:
            continue

        # Case 1: Key : Value
        if ':' in line:
            parts = line.split(':', 1)
            key = parts[0].strip()
            value = parts[1].strip()

        # Case 2: Key - Value
        elif '-' in line:
            parts = line.split('-', 1)
            key = parts[0].strip()
            value = parts[1].strip()

        else:
            words = line.split()

            if len(words) >= 2:
                key = words[0]
                key = key.replace(".", "").strip()
                value = " ".join(words[1:])
            else:
                continue

        if len(key) > 1 and len(value) > 1:
            data[key] = value

    return data   # ← MUST be here


def filter_important_fields(data):
    if not data:
        return {}

    important = {}

    keywords = [
        'name', 'id', 'no', 'number',
        'date', 'phone', 'mobile',
        'address', 'pnr'
    ]

    for key, value in data.items():
        for word in keywords:
            if word in key.lower():
                important[key] = value

    # fallback if nothing matched
    if not important:
        return data

    return important