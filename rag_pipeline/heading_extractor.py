import re

def extract_heading(text):
    """
    Extracts likely section heading from chunk.
    """

    # look for ALL CAPS words or Title Case lines
    lines = text.split("\n")

    for line in lines:
        line = line.strip()

        # skip long sentences
        if len(line.split()) > 6:
            continue

        # detect headings
        if re.match(r'^[A-Z][A-Za-z ]+$', line):
            return line

        if line.isupper():
            return line

    return "Document Section"