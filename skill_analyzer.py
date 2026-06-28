# Common skills used to detect mentions in resume and job description text.
# Each entry is the display name shown in the UI.
SKILL_DICTIONARY = [
    # Core programming
    "Python",
    "SQL",
    "Git",
    "GitHub",

    # Data analysis
    "Pandas",
    "NumPy",
    "Excel",
    "Power BI",
    "Tableau",
    "Data Analysis",
    "Statistics",

    # Machine learning
    "Machine Learning",
    "Deep Learning",
    "Scikit-learn",
    "TensorFlow",
    "PyTorch",
    "NLP",
    "Computer Vision",

    # GenAI / LLM
    "OpenAI",
    "LLM",
    "LangChain",
    "RAG",
    "Prompt Engineering",
    "Vector Database",
    "ChromaDB",

    # Backend / deployment
    "FastAPI",
    "Streamlit",
    "Docker",
    "Azure",
    "AWS",
]


def extract_skills(text: str) -> list[str]:
    """
    Find skills from SKILL_DICTIONARY that appear in the given text.

    Args:
        text: Resume text or job description text.

    Returns:
        A list of matched skills using the original display names
        from SKILL_DICTIONARY. Each skill appears at most once.
    """
    # Normalize text once for case-insensitive matching
    text_lower = text.lower()

    matched_skills = []

    # Check each known skill against the text
    for skill in SKILL_DICTIONARY:
        skill_lower = skill.lower()

        # If the skill appears in the text, add its display name
        if skill_lower in text_lower:
            matched_skills.append(skill)

    return matched_skills


def calculate_match_score(resume_skills: list[str], jd_skills: list[str]) -> float:
    """
    Calculate what percentage of job description skills appear on the resume.

    Version 1 uses equal weighting: every JD skill counts the same.

    Args:
        resume_skills: Skills found in the resume.
        jd_skills: Skills found in the job description.

    Returns:
        Match score as a percentage (0.00 to 100.00), rounded to 2 decimal places.
        Returns 0.0 if the job description has no skills.
    """
    # Avoid division by zero when no JD skills were found
    if not jd_skills:
        return {
        "success": False,
        "message": "No recognizable skills were found in the job description."
    }

    # Count how many JD skills also appear in the resume
    matched_count = 0
    for skill in jd_skills:
        if skill in resume_skills:
            matched_count += 1

    # Equal weighting: each JD skill contributes equally to the score
    score = (matched_count / len(jd_skills)) * 100

    return round(score, 2)