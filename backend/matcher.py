# matcher.py

def match_skills(resume_skills, jd_skills):
    """
    Compare resume skills with JD skills.
    Returns matched and missing skills.
    """

    # Convert everything to lowercase
    resume = {skill.lower() for skill in resume_skills}
    jd = {skill.lower() for skill in jd_skills}

    matched = resume.intersection(jd)
    missing = jd.difference(resume)

    return list(matched), list(missing)


# Test the function
if __name__ == "__main__":

    resume_skills = [
        "Python",
        "Excel",
        "SQL",
        "Power BI"
    ]

    jd_skills = [
        "Python",
        "Excel",
        "Google Sheets",
        "Communication"
    ]

    matched, missing = match_skills(resume_skills, jd_skills)
    total_jd_skills = len(jd_skills)
matched_count = len(matched)

match_score = (matched_count / total_jd_skills) * 100

print("Matched Skills:")
print(matched)
print(f"\nResume Match Score: {match_score:.2f}%")

print("\nMissing Skills:")
print(missing)