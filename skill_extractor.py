from backend.resume_reader import extract_resume_text

SKILLS_LIST = [
    "Python",
    "Java",
    "SQL",
    "Excel",
    "Microsoft Excel",
    "Power BI",
    "Microsoft Office",
    "Word",
    "Communication",
    "Leadership",
    "Project Management",
    "Data Analysis",
    "Business Analysis",
    "Financial Analysis",
    "Accounting",
    "Auditing",
    "Finance",
    "Economics",
    "Research",
    "Presentation",
    "Problem Solving",
    "Critical Thinking",
    "Time Management",
    "Teamwork",
    "Sustainability",
    "AI",
    "Artificial Intelligence",
    "Machine Learning",
    "Business Development",
    "Customer Service"
]

def extract_skills(resume_text):
    found_skills = []

    # Remove all spaces and convert to lowercase
    lowered_text = resume_text.lower().replace(" ", "")

    for skill in SKILLS_LIST:
        lowered_skill = skill.lower().replace(" ", "")

        if lowered_skill in lowered_text:
            found_skills.append(skill)

    return found_skills


pdf_path = input("Enter the path to your resume PDF: ").strip().strip('"').strip("'")

resume_text = extract_resume_text(pdf_path)

matched_skills = extract_skills(resume_text)

print("\nSkills found:")
print(matched_skills)