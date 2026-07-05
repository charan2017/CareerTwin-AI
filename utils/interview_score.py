def evaluate_answer(user_answer, expected_answer):

    user_words = set(
        user_answer.lower().split()
    )

    expected_words = set(
        expected_answer.lower().split()
    )

    matched = user_words.intersection(
        expected_words
    )

    score = round(
        len(matched) /
        len(expected_words) * 100
    )

    if score >= 80:

        feedback = "🌟 Excellent answer."

    elif score >= 60:

        feedback = "👍 Good answer. Add a little more detail."

    elif score >= 40:

        feedback = "⚠ Fair answer. Improve your explanation."

    else:

        feedback = "❌ Weak answer. Review this topic."

    missing = sorted(
        expected_words - matched
    )

    return {
        "score": score,
        "feedback": feedback,
        "missing": missing[:10]
    }