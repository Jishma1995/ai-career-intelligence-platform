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


def get_missing_skills(resume_skills: list[str], jd_skills: list[str]) -> list[str]:
    """
    Find skills required by the job description that are missing from the resume.

    Args:
        resume_skills: Skills found in the resume.
        jd_skills: Skills found in the job description.

    Returns:
        JD skills that do not appear in the resume, in the same order as jd_skills.
    """
    missing_skills = []

    # Walk through JD skills in order and keep only those not on the resume
    for skill in jd_skills:
        if skill not in resume_skills:
            missing_skills.append(skill)

    return missing_skills


# Rule-based recommendations for common missing skills (Version 1).
# Keys must match the display names used in SKILL_DICTIONARY.
SKILL_RECOMMENDATIONS = {
    "Python": (
        "Add a Python project to your resume (e.g., data pipeline, API, or automation script) "
        "and list libraries you used such as Pandas or FastAPI."
    ),
    "SQL": (
        "Practice writing JOIN, GROUP BY, and window-function queries, then add a bullet showing "
        "how you used SQL for reporting or data extraction."
    ),
    "GitHub": (
        "Create or polish a public GitHub profile with 1–2 well-documented repos, clear README files, "
        "and consistent commit history."
    ),
    "Machine Learning": (
        "Complete an end-to-end ML project (problem definition, training, evaluation, deployment) "
        "and describe the model, metrics, and business outcome on your resume."
    ),
    "Deep Learning": (
        "Build a small deep learning project with TensorFlow or PyTorch (e.g., image or text classification) "
        "and report accuracy or F1 score in a resume bullet."
    ),
    "NLP": (
        "Add an NLP project such as text classification, sentiment analysis, or named-entity recognition, "
        "and mention the dataset, model, and evaluation metrics."
    ),
    "RAG": (
        "Build a retrieval-augmented generation demo that loads documents, embeds them, retrieves relevant "
        "chunks, and generates answers with an LLM."
    ),
    "OpenAI": (
        "Create a small project using the OpenAI API (chat, embeddings, or function calling) and note "
        "prompt design, cost awareness, and error handling."
    ),
    "LangChain": (
        "Build a LangChain app with chains or agents (e.g., document Q&A or tool use) and highlight "
        "components like loaders, retrievers, and memory on your resume."
    ),
    "ChromaDB": (
        "Practice storing and querying embeddings in ChromaDB as part of a RAG or semantic search project, "
        "and mention collection setup and retrieval quality."
    ),
    "FastAPI": (
        "Deploy a REST API with FastAPI (CRUD endpoints, request validation, and docs at /docs) "
        "and link it from a portfolio or GitHub repo."
    ),
    "Streamlit": (
        "Publish an interactive Streamlit app (dashboard, model demo, or data explorer) and add the "
        "live link or repo to your resume."
    ),
    "Docker": (
        "Containerize one of your projects with a Dockerfile and docker-compose, then note how Docker "
        "improved reproducibility or deployment."
    ),
    "Azure": (
        "Earn a foundational Azure certification or deploy a project using a core service "
        "(e.g., Azure App Service, Blob Storage, or Azure OpenAI) and list it on your resume."
    ),
    "AWS": (
        "Complete a hands-on AWS project (e.g., S3 + Lambda, EC2 deployment, or SageMaker) "
        "and describe the architecture in one resume bullet."
    ),
    "Power BI": (
        "Build a Power BI dashboard from a real dataset, publish or export it, and describe "
        "the KPIs, visuals, and business insights you delivered."
    ),
}

# Used when a missing skill has no specific recommendation above.
GENERIC_RECOMMENDATION = (
    "Add a relevant project, course, or certification that demonstrates this skill, "
    "and mention concrete tools, outcomes, and metrics on your resume."
)


def generate_recommendations(missing_skills: list[str]) -> dict:
    """
    Build rule-based recommendations for each missing skill.

    Args:
        missing_skills: Skills required by the JD that are not on the resume.

    Returns:
        A dictionary mapping each missing skill to an actionable recommendation string.
    """
    recommendations = {}

    for skill in missing_skills:
        # Use a specific recommendation if we have one; otherwise use the generic fallback
        if skill in SKILL_RECOMMENDATIONS:
            recommendations[skill] = SKILL_RECOMMENDATIONS[skill]
        else:
            recommendations[skill] = GENERIC_RECOMMENDATION

    return recommendations

