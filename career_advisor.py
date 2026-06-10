def recommend(skills):

    roles = []

    if "python" in skills:
        roles.append("AI Engineer")

    if "aws" in skills:
        roles.append("Cloud Engineer")

    if "blockchain" in skills:
        roles.append("Blockchain Developer")

    if "react" in skills:
        roles.append("Frontend Developer")

    if "spring boot" in skills:
        roles.append("Backend Developer")

    return roles