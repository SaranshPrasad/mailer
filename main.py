PLACEHOLDER = "[name]"

with open("invited_names.txt") as name_file:
    names = name_file.readlines()


with open("letter.txt") as letter:
    letter_content = letter.read()
    for nms in names:
        stripped_name = nms.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
        with open(f"letter_for_{stripped_name}.txt", mode="w") as name_letter:
            name_letter.write(new_letter)


