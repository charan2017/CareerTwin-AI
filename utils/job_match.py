from skills_db import ROLES


def calculate_job_matches(resume_text):

    resume = resume_text.lower()

    results = []

    for role, skills in ROLES.items():

        matched = 0

        for skill in skills:

            if skill.lower() in resume:

                matched += 1

        score = round(
            matched / len(skills) * 100
        )

        results.append(
            {
                "role": role,
                "score": score
            }
        )

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results