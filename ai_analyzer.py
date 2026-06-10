import re

def generate_summary(text):

    text_lower = text.lower()

    summary_parts = []

    # Education

    if "b.tech" in text_lower:
        summary_parts.append(
            "Bachelor of Technology student"
        )

    elif "m.tech" in text_lower:
        summary_parts.append(
            "Master of Technology candidate"
        )

    # Skills

    skills = []

    skill_keywords = [
        "python",
        "java",
        "react",
        "spring boot",
        "aws",
        "blockchain",
        "machine learning",
        "artificial intelligence",
        "docker",
        "sql"
    ]

    for skill in skill_keywords:

        if skill in text_lower:
            skills.append(skill.title())

    if skills:

        summary_parts.append(
            "Skilled in " +
            ", ".join(skills[:6])
        )

    # Projects

    project_count = text_lower.count("project")

    if project_count > 0:

        summary_parts.append(
            f"Completed {project_count} academic or personal projects"
        )

    # Certifications

    cert_count = (
        text_lower.count("certified")
        + text_lower.count("certificate")
        + text_lower.count("certification")
    )

    if cert_count > 0:

        summary_parts.append(
            f"Holds {cert_count} professional certifications"
        )

    # Career Focus

    if "blockchain" in text_lower:

        summary_parts.append(
            "Interested in Blockchain development"
        )

    if "aws" in text_lower:

        summary_parts.append(
            "Has exposure to Cloud technologies"
        )

    if (
        "machine learning" in text_lower
        or "artificial intelligence" in text_lower
    ):

        summary_parts.append(
            "Focused on AI and Machine Learning applications"
        )

    if len(summary_parts) == 0:

        return (
            "Resume analyzed successfully. "
            "Additional information required "
            "for detailed profiling."
        )

    return ". ".join(summary_parts) + "."