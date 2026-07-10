def clean_text(text):

    words = text.split()

    filtered_words = []

    blacklist = [
        "alamy",
        "jpeg",
        "jpg",
        "png",
        "club",
        "com",
        "life"
    ]

    for word in words:

        if len(word) < 3:
            continue

        if word.lower() in blacklist:
            continue

        filtered_words.append(word)

    return " ".join(filtered_words)