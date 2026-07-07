# Vokira

🚧 Status: Building

## Vision
An AI-powered Career Copilot that helps students analyze resumes, compare them with job descriptions, identify skill gaps, and recommend projects and certifications.

## Features (Planned)
- Resume Analysis
- Job Description Matching
- Skill Gap Analysis
- Project Recommendations
- Certification Suggestions
- Career Roadmap

## Tech Stack
- Python
- VS Code
- Git
- GitHub
- Ollama
- Qwen (Local AI Model)

Started: 5 July 2026

## Day 2 Progress

### Features Added
- Resume PDF Reader
- Skill Extractor
- Case-insensitive skill matching
- Basic GitHub integration

### Status
✅ Resume text extraction working
✅ Skills detected successfully

## Day 3 Progress

### Features Completed
- Added Job Description Reader (`jd_reader.py`)
- Built Skill Matcher (`matcher.py`)
- Added ATS Match Score calculation
- Successfully compared Resume Skills with Job Description Skills

### Testing
- Resume Reader tested successfully
- Job Description Reader tested successfully
- Skill Extractor tested successfully
- Skill Matcher tested successfully
- ATS Match Score generated successfully

### Debugging
- Fixed file path issues
- Fixed module import errors
- Fixed corrupted PDF issue by creating a new PDF
- Fixed Python indentation errors

### Current Project Modules
- resume_reader.py
- skill_extractor.py
- jd_reader.py
- matcher.py