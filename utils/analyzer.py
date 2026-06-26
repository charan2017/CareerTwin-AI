from skills_db import ROLES

def analyze_resume(resume_text, selected_role):
    required_skills = ROLES[selected_role]

    resume_lower = resume_text.lower()

    matched = []
    missing = []

    for skill in required_skills:
        if skill.lower() in resume_lower:
            matched.append(skill)
        else:
            missing.append(skill)

    score = round((len(matched) / len(required_skills)) * 100)

    if score >= 80:
        readiness = "🟢 Job Ready"

    elif score >= 60:
        readiness = "🟡 Almost Ready"

    else:
        readiness = "🔴 Needs Improvement"

    return {
        "score": score,
        "matched": matched,
        "missing": missing,
        "readiness": readiness
    }