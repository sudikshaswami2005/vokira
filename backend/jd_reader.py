# jd_reader.py
# This script reads a Job Description (JD) from a .txt file and returns it as text.

def read_job_description(file_path):
    """
    This function takes the path of a .txt file containing a job description,
    reads its content, and returns it as a single string of text.
    """
    try:
        # 'open' opens the file in read mode ('r')
        # 'encoding="utf-8"' makes sure special characters are read correctly
        with open(file_path, "r", encoding="utf-8") as file:
            # .read() reads the entire content of the file as one string
            jd_text = file.read()
        
        # Return the text so it can be used in other parts of the program
        return jd_text

    except FileNotFoundError:
        # This runs if the file path is wrong or the file doesn't exist
        print(f"Error: The file '{file_path}' was not found. Please check the file path.")
        return None

    except Exception as e:
        # This catches any other unexpected error and shows what went wrong
        print(f"Something went wrong while reading the file: {e}")
        return None


# This part only runs when you run this file directly (for testing)
if __name__ == "__main__":
    # Change this path to your actual JD text file
    file_path = "sample_jd.txt"

    jd_text = read_job_description(file_path)

    if jd_text:
        print("Job Description loaded successfully!\n")
        print(jd_text)