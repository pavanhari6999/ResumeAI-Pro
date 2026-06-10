def calculate_match(resume_text, jd_text):

    resume_words = set(resume_text.lower().split())
    jd_words = set(jd_text.lower().split())

    matched = resume_words.intersection(jd_words)

    score = int(
        len(matched) /
        max(len(jd_words), 1)
        * 100
    )

    missing = jd_words - resume_words

    return score, list(missing)[:20]