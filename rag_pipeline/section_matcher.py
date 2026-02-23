def match_sections(query, chunks):
    """
    Returns only the section names relevant to the query.
    """

    query = query.lower()

    section_map = {
        "skills": ["skill", "programming", "language", "tech"],
        "education": ["education", "degree", "college"],
        "projects": ["project", "built", "developed"],
        "certifications": ["certification", "certificate"],
        "summary": ["summary", "profile"]
    }

    matched = set()

    for section, keywords in section_map.items():
        for word in keywords:
            if word in query:
                matched.add(section.capitalize())

    if not matched:
        matched.add("General Information")

    return list(matched)