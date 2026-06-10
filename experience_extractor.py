import re

def detect_experience(text):

    text = text.lower()

    patterns = [
        r'(\d+)\+?\s*years',
        r'(\d+)\+?\s*yrs',
        r'(\d+)\+?\s*year'
    ]

    for pattern in patterns:
        matches = re.findall(pattern, text)

        if matches:
            return int(matches[0])

    return 0