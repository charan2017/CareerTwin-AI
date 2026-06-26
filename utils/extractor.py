import re


def extract_candidate_info(text):

    email = ""
    phone = ""
    github = ""
    linkedin = ""

    email_match = re.search(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        text
    )

    if email_match:
        email = email_match.group()

    phone_match = re.search(
        r"(\+91[- ]?)?[6-9]\d{9}",
        text
    )

    if phone_match:
        phone = phone_match.group()

    github_match = re.search(
        r"github\.com/[A-Za-z0-9_-]+",
        text,
        re.IGNORECASE
    )

    if github_match:
        github = github_match.group()

    linkedin_match = re.search(
        r"linkedin\.com/in/[A-Za-z0-9_-]+",
        text,
        re.IGNORECASE
    )

    if linkedin_match:
        linkedin = linkedin_match.group()

    return {
        "email": email,
        "phone": phone,
        "github": github,
        "linkedin": linkedin
    }