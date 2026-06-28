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

## Version 1 File Map

app.py
- Streamlit user interface
- Handles resume upload and job description input
- Displays analysis results

resume_parser.py
- Extracts text from uploaded resume PDF

skill_analyzer.py
- Contains skill dictionary
- Extracts skills from resume and job description text
- Calculates match score
- Identifies matched and missing skills
- Generates basic recommendations

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