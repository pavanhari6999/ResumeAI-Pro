def extract_education(text):

    keywords = [
        "b.tech",
        "bachelor",
        "m.tech",
        "master",
        "university",
        "college"
    ]

    education = []

    for line in text.split("\n"):

        for keyword in keywords:

            if keyword.lower() in line.lower():

                education.append(line.strip())

                break

    return list(set(education))