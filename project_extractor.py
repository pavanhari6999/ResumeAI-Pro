def extract_projects(text):

    projects = []

    lines = text.split("\n")

    ignore_words = [
        "developed",
        "implemented",
        "worked",
        "improved",
        "utilized",
        "collaborative",
        "communication",
        "scrum",
        "environment",
        "responsible"
    ]

    for line in lines:

        line = line.strip()

        if len(line) < 5:
            continue

        lower_line = line.lower()

        if any(word in lower_line for word in ignore_words):
            continue

        if (
            "system" in lower_line
            or "project" in lower_line
            or "management" in lower_line
            or "registration" in lower_line
        ):
            projects.append(line)

    return list(dict.fromkeys(projects))