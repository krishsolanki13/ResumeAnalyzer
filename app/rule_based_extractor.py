import re

def extract_email(text):
    match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    return match.group() if match else None

def extract_phone(text):
    match = re.search(r"(\+?\d{1,3}[\s-]?)?\(?\d{3,5}\)?[\s-]?\d{3,5}[\s-]?\d{3,5}", text)
    return match.group() if match else None

def extract_linkedin(text):
    match = re.search(r"(https?:\/\/)?(www\.)?linkedin\.com\/[^\s\n]+", text)
    return match.group() if match else None

def extract_github(text):
    match = re.search(r"(https?:\/\/)?(www\.)?github\.com\/[^\s\n]+", text)
    return match.group() if match else None

def extract_name(text):
    # Assume name is in the top few lines
    lines = text.strip().split("\n")
    for line in lines:
        if len(line.strip().split()) <= 4 and not any(char.isdigit() for char in line):
            return line.strip()
    return None

def extract_all_fields(text):
    return {
        "Name": extract_name(text),
        "Email": extract_email(text),
        "Phone": extract_phone(text),
        "LinkedIn": extract_linkedin(text),
        "Github": extract_github(text),
    }
