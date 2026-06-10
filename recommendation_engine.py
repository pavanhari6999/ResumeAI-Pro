def generate_recommendations(
    skills,
    missing_keywords,
    roles,
    certifications
):

    recommendations = []

    if "sql" in missing_keywords:
        recommendations.append(
            "Add SQL projects to improve backend and data handling skills."
        )

    if "git" in missing_keywords:
        recommendations.append(
            "Add GitHub repository links to showcase version control experience."
        )

    if "docker" in missing_keywords:
        recommendations.append(
            "Learn Docker and containerize one project."
        )

    if "aws" in missing_keywords:
        recommendations.append(
            "Deploy a project on AWS to strengthen cloud skills."
        )

    role_names = [
        role[0] for role in roles
    ]

    if "Cloud Engineer" in role_names:
        recommendations.append(
            "Gain hands-on experience with AWS EC2, S3 and IAM."
        )

    if "AI Engineer" in role_names:
        recommendations.append(
            "Build Machine Learning projects and publish them on GitHub."
        )

    if certifications < 3:
        recommendations.append(
            "Earn additional industry certifications."
        )

    return recommendations