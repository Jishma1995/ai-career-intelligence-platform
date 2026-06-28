## Version 1 Scope

Version 1 answers one question:

"How well does this resume match this job description, and what skills are missing?"

### User Flow

1. User uploads resume PDF
2. User pastes job description
3. System extracts resume text
4. System extracts skills from resume and job description
5. System compares skills
6. System displays:
   - Match score
   - Matched skills
   - Missing skills
   - Basic recommendations

## Version 1 Scoring Logic

Match Score = (Number of matched JD skills / Total JD skills) × 100

## Version 1 File Map

### app.py

**Purpose:** Streamlit user interface.

**Responsibilities:**

* Display application UI
* Accept resume PDF upload
* Accept job description input
* Trigger analysis when user clicks Analyze
* Display:

  * Match score
  * Matched skills
  * Missing skills
  * Recommendations

**Contains:**

* Streamlit components only
* No business logic

### resume_parser.py

**Purpose:** Extract text from uploaded resume PDFs.

**Responsibilities:**

* Read uploaded PDF files
* Extract text from all pages
* Return resume text to the application

**Functions:**

```python
extract_resume_text(pdf_file) -> str
```

**Input:**

* Uploaded PDF file

**Output:**

* Resume text

### skill_analyzer.py

**Purpose:** Analyze resume skills against job description skills.

**Responsibilities:**

* Extract skills from text
* Compare resume skills with job description skills
* Calculate match score
* Identify missing skills
* Generate rule-based recommendations

**Functions:**

```python
extract_skills(text: str) -> list[str]

calculate_match_score(
    resume_skills: list[str],
    jd_skills: list[str]
) -> float

get_missing_skills(
    resume_skills: list[str],
    jd_skills: list[str]
) -> list[str]

generate_recommendations(
    missing_skills: list[str]
) -> dict

analyze_match(
    resume_text: str,
    jd_text: str
) -> dict
```

### requirements.txt

**Purpose:** Store project dependencies.

**Version 1 Dependencies:**

```text
streamlit
pymupdf
```

## Future Improvements

### Resume Parser
- Ignore completely blank PDF pages before combining extracted text.
- Add support for DOCX resumes.
- Improve handling of scanned/image-only resumes.

### Skill Analyzer
- Improve skill matching using regular expressions to avoid substring false positives.
- Expand skill dictionary beyond AI/Data Science roles.
- Add LLM-based skill extraction in a future version.
- Introduce weighted skill scoring based on job requirement importance.
- Optimize membership lookup using sets if the skill dictionary grows significantly.
- Add semantic skill matching using embeddings instead of exact keyword matching.
- Support common skill synonyms and abbreviations (e.g. LLM ↔ Large Language Model).
- Replace rule-based recommendations with LLM-generated personalized recommendations.
- Recommend high-quality learning resources (official documentation, courses, GitHub repositories, and videos) dynamically instead of using predefined text.
- Personalize recommendations based on the user's current skill level and target role.
- Prioritize recommendations based on the importance of missing skills in the job description.
- Estimate the learning difficulty and time required for each recommended skill.
- Suggest portfolio projects for each missing skill instead of only learning resources.
- Recommend a learning sequence when multiple skills are missing (e.g., learn Python before LangChain).
- Explain why each recommended skill is important for the target job role.