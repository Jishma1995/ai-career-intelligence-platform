import fitz  # PyMuPDF


def extract_resume_text(pdf_file):
    """
    Extract all text from a Streamlit-uploaded PDF resume.

    Args:
        pdf_file: A Streamlit UploadedFile object (from st.file_uploader).

    Returns:
        str: All text from every page, combined into one string.

    Raises:
        ValueError: If the PDF cannot be read or parsed.
    """
    try:
        # Streamlit upload objects behave like file objects — read them as bytes
        pdf_file.seek(0)
        pdf_bytes = pdf_file.read()

        # Open the PDF from memory (no need to save to disk)
        with fitz.open(stream=pdf_bytes, filetype="pdf") as document:
            page_texts = []

            # Loop through every page and extract its text
            for page in document:
                page_texts.append(page.get_text())

        # Combine all pages into one string (blank line between pages)
        return "\n\n".join(page_texts)

    except Exception as error:
        # Re-raise with a clear, beginner-friendly message
        raise ValueError(f"Could not read the PDF file: {error}") from error