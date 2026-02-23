def chunk_text(text, chunk_size=500, overlap=100):

    lines = text.split("\n")

    chunks = []
    current_heading = ""
    buffer = ""

    for line in lines:
        clean = line.strip()

        # detect heading (ALL CAPS or title with many words)
        if clean.isupper() and len(clean) > 5:
            current_heading = clean
            continue

        buffer += line + "\n"

        if len(buffer) > chunk_size:
            chunk = f"{current_heading}\n{buffer}"
            chunks.append(chunk)
            buffer = buffer[-overlap:]

    if buffer:
        chunk = f"{current_heading}\n{buffer}"
        chunks.append(chunk)

    return chunks