import streamlit as st

from resume_parser import extract_resume_text
from skill_analyzer import analyze_match


def display_skill_list(skills: list[str]) -> None:
    """Show a list of skills in a simple, readable format."""
    if skills:
        st.write(", ".join(skills))
    else:
        st.write("None found.")


def display_recommendations(recommendations: dict) -> None:
    """Show rule-based recommendations for missing skills."""
    if not recommendations:
        st.write("No recommendations needed.")
        return

    for skill, recommendation in recommendations.items():
        st.markdown(f"**{skill}**")
        st.write(recommendation)


# --- Page layout ---

st.title("AI Career Intelligence Platform")

st.write(
    "Upload your resume and paste a job description to see how well your "
    "skills match the role, which skills overlap, what's missing, and "
    "actionable steps to improve your fit."
)

# User inputs
uploaded_resume = st.file_uploader(
    "Upload your resume (PDF only)",
    type="pdf",
)

job_description = st.text_area(
    "Job Description",
    placeholder="Paste the full job description here...",
    height=200,
)

# Run analysis when the user clicks the button
if st.button("Analyze Resume"):
    # Validate required inputs before calling backend functions
    if uploaded_resume is None:
        st.warning("Please upload a resume PDF before analyzing.")
    elif not job_description.strip():
        st.warning("Please enter a job description before analyzing.")
    else:
        try:
            # Extract text from the uploaded PDF
            resume_text = extract_resume_text(uploaded_resume)

            # Compare resume skills against job description skills
            results = analyze_match(resume_text, job_description)

            if not results["success"]:
                st.warning(results["message"])
            else:
                st.subheader("Analysis Results")

                # Match score as a prominent metric
                st.metric(
                    label="Match Score",
                    value=f"{results['match_score']}%",
                )

                st.markdown("**Resume Skills**")
                display_skill_list(results["resume_skills"])

                st.markdown("**Job Description Skills**")
                display_skill_list(results["jd_skills"])

                st.markdown("**Matched Skills**")
                display_skill_list(results["matched_skills"])

                st.markdown("**Missing Skills**")
                display_skill_list(results["missing_skills"])

                st.markdown("**Recommendations**")
                display_recommendations(results["recommendations"])

        except Exception as error:
            st.error(str(error))