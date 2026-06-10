def keyword_gap(skills):

    target = [
        "python",
        "sql",
        "aws",
        "git",
        "docker",
        "linux",
        "kubernetes"
    ]

    missing = []

    for skill in target:

        if skill not in skills:

            missing.append(skill)

    return missing