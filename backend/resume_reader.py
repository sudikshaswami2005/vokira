# Install the required library first if needed:
# pip install pypdf

from pypdf import PdfReader


def extract_resume_text(pdf_path):
    """Read a PDF file and return all extracted text from every page."""
    # Open the PDF file.
    reader = PdfReader(pdf_path)

    # Create a list to hold text from each page.
    page_texts = []

    # Loop through every page in the PDF.
    for page in reader.pages:
        # Extract the text from the current page.
        text = page.extract_text()

        # Add the page text to the list if it exists.
        if text:
            page_texts.append(text)

    # Join all page texts into one long string.
    return "\n\n".join(page_texts)


def main():
    # Ask the user to type the path to the PDF file.
    pdf_path = input("Enter the path to your PDF file: ").strip().strip('"').strip("'")

    # Try to open the PDF file.
    try:
        resume_text = extract_resume_text(pdf_path)
    except FileNotFoundError:
        print("File not found. Please check the path and try again.")
        return
    except Exception as error:
        print(f"Could not read the PDF file: {error}")
        return

    # Print the extracted resume text.
    print(resume_text)


if __name__ == "__main__":
    main()
