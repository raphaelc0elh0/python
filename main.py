with open("story.txt", "w") as file:
    file.write("This is overwriting whats in the file\n")

with open("story.txt", "r") as file:
    print(file.read())  # "This is overwriting whats in the file"
