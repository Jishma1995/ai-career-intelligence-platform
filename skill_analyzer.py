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