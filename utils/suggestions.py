def generate_suggestions(analysis, role):
    """
    Generate AI-like resume suggestions based on
    ATS score and missing skills.
    """

    score = analysis["score"]
    matched = analysis["matched"]
    missing = analysis["missing"]

    suggestions = []

    # -------------------------
    # Missing Skills
    # -------------------------

    for skill in missing:

        suggestions.append({
            "title": f"Learn {skill}",
            "priority": "High",
            "description":
                f"Add {skill} to your resume after gaining practical experience."
        })

    # -------------------------
    # Resume Improvements
    # -------------------------

    suggestions.append({
        "title": "Improve Projects",
        "priority": "Medium",
        "description":
            "Include 3–5 technical projects with measurable results."
    })

    suggestions.append({
        "title": "Add GitHub",
        "priority": "Medium",
        "description":
            "Include your GitHub profile with active repositories."
    })

    suggestions.append({
        "title": "Quantify Achievements",
        "priority": "High",
        "description":
            "Use numbers like 'Improved accuracy by 12%' or 'Reduced execution time by 35%'."
    })

    suggestions.append({
        "title": "Keep Resume ATS Friendly",
        "priority": "Low",
        "description":
            "Use simple headings and avoid tables or images."
    })

    # -------------------------
    # Estimated Score
    # -------------------------

    estimated = score

    estimated += len(missing) * 5

    estimated += 10

    if estimated > 95:
        estimated = 95

    # -------------------------
    # Recommended Project
    # -------------------------

    projects = {

        "AI Engineer":
            "AI Resume Screening System",

        "Machine Learning Engineer":
            "House Price Prediction",

        "Data Scientist":
            "Customer Churn Prediction",

        "Data Analyst":
            "Interactive Sales Dashboard",

        "Software Engineer":
            "Library Management System",

        "Full Stack Developer":
            "E-Commerce Website"
    }

    return {

        "estimated_score": estimated,

        "project": projects.get(
            role,
            "Portfolio Website"
        ),

        "suggestions": suggestions
    }