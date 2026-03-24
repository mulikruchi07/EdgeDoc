import re

def extract_dynamic_fields(lines):
    data = {}

    i = 0
    while i < len(lines):

        line = lines[i].strip()

        # skip garbage
        if len(line) < 2:
            i += 1
            continue

        # -------------------------------
        # CASE 1: Numbered 3-line pattern
        # -------------------------------
        if line.isdigit():
            if i + 2 < len(lines):
                key = lines[i + 1].strip()
                value = lines[i + 2].strip()

                if len(key) > 1 and len(value) > 1:
                    data[key] = value
                    i += 3
                    continue

        # --------------------------------
        # CASE 2: Inline key value
        # --------------------------------
        words = line.split()

        if len(words) >= 2:
            key = " ".join(words[:-1])
            value = words[-1]

            # Detect meaningful value
            if re.search(r'\d', value) or len(value) > 2:
                data[key] = value

        # --------------------------------
        # CASE 3: "Key" on one line, value next
        # --------------------------------
        if i + 1 < len(lines):
            next_line = lines[i + 1].strip()

            if (
                len(line) > 2 and
                len(next_line) > 2 and
                not next_line.isdigit()
            ):
                data[line] = next_line
                i += 2
                continue

        i += 1

    return data

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
