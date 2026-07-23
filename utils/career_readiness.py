def calculate_career_readiness(analysis, job_matches):

    resume_score = analysis["score"]

    best_job_match = max(
        [job["score"] for job in job_matches],
        default=0
    )

    total_skills = len(analysis["matched"]) + len(analysis["missing"])

    if total_skills > 0:
        skills_score = round(
            len(analysis["matched"]) / total_skills * 100
        )
    else:
        skills_score = 100

    overall = round(
        (resume_score + best_job_match + skills_score) / 3
    )

    if overall >= 80:
        status = "🟢 Job Ready"
    elif overall >= 60:
        status = "🟡 Almost Ready"
    else:
        status = "🔴 Needs Improvement"

    return {
        "overall": overall,
        "resume": resume_score,
        "job_match": best_job_match,
        "skills": skills_score,
        "status": status,
    }