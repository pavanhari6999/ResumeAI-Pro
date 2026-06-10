def predict_roles(skills):

    roles = []

    if "python" in skills:
        roles.append(("AI Engineer", 92))

    if "machine learning" in skills:
        roles.append(("Data Scientist", 88))

    if "aws" in skills:
        roles.append(("Cloud Engineer", 85))

    if "blockchain" in skills:
        roles.append(("Blockchain Developer", 90))

    if "react" in skills:
        roles.append(("Frontend Developer", 80))

    if "spring boot" in skills:
        roles.append(("Backend Developer", 84))

    return roles