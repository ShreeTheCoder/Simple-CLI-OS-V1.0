

while True:
    cmd = input(">")

    #mkfile command
    if cmd == "mkfile":
        file_name = input("Enter the file name: ")
        file_text = input("Enter the text you wanna write: ")

        with open(file_name, "w") as file:
            file.write(file_text)
            file.close()

        continue