import re

def analyze_resume(text):

    skills_db = [
        "python",
        "java",
        "c++",
        "c",
        "sql",
        "mysql",
        "mongodb",
        "html",
        "css",
        "javascript",
        "react",
        "angular",
        "nodejs",
        "spring boot",
        "django",
        "flask",
        "machine learning",
        "deep learning",
        "artificial intelligence",
        "data science",
        "tensorflow",
        "pytorch",
        "aws",
        "azure",
        "gcp",
        "docker",
        "kubernetes",
        "git",
        "github",
        "jenkins",
        "linux",
        "blockchain"
    ]

    found_skills = []

    for skill in skills_db:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    cert_keywords = [
        "certified",
        "certificate",
        "certification"
    ]

    certifications = 0

    for word in cert_keywords:
        certifications += text.lower().count(word)

    projects = text.lower().count("project")

    score = 40

    score += len(found_skills) * 3
    score += certifications * 4
    score += projects * 5

    score = min(score, 100)

    suggestions = []

    if "python" not in found_skills:
        suggestions.append("Add Python")

    if "sql" not in found_skills:
        suggestions.append("Add SQL")

    if "aws" not in found_skills:
        suggestions.append("Add AWS")

    if "git" not in found_skills:
        suggestions.append("Add Git")

    if "docker" not in found_skills:
        suggestions.append("Learn Docker")

    if "kubernetes" not in found_skills:
        suggestions.append("Learn Kubernetes")

    return (
        found_skills,
        score,
        suggestions,
        certifications,
        projects
    )