def find_pattern_occurrences(text):
    occurrences = 0
    words = text.split()

    for word in words:

        if word.startswith("C") and word.endswith("jeb"):

            occurrences += 1


    return occurrences


text = "This is a test to check for occurrences of patterns like Catjeb, Ccccjeb, and Crayjeb"
print("Number of pattern occurrences:", find_pattern_occurrences(text))