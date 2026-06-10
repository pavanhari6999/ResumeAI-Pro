def calculate_ats(
    skills,
    projects,
    certifications,
    education,
    experience,
    missing_keywords
):

    skills_score = min(len(skills) * 4, 40)

    project_score = min(projects * 8, 20)

    cert_score = min(certifications * 4, 15)

    education_score = 15 if education else 0

    experience_score = min(experience * 2, 10)

    keyword_score = max(
        0,
        15 - len(missing_keywords) * 2
    )

    breakdown = {
        "Skills": skills_score,
        "Projects": project_score,
        "Certifications": cert_score,
        "Education": education_score,
        "Experience": experience_score,
        "Keyword Match": keyword_score
    }

    score = sum(breakdown.values())

    if score > 100:
        score = 100

    return score, breakdown