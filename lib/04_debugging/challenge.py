def get_most_common_letter(text):
    counter = {}
    for char in text:
        if char != ' ':
            counter[char] = counter.get(char, 0) + 1
    max_count = max(counter.values())
    most_common_letters = [char for char, count in counter.items() if count == max_count]
    letter = most_common_letters[0]
    return letter

print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!")
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")
