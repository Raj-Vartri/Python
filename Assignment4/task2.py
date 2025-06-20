def file_operations():
    initial_text = input("Enter text to write to the file: ")
    try:
        with open("output.txt", "w") as file:
            file.write(initial_text + "\n")
        print("Data successfully written to output.txt.")
    except IOError as e:
        print(f"Error writing to file: {e}")
        return

    additional_text = input("Enter additional text to append: ")
    try:
        with open("output.txt", "a") as file:
            file.write(additional_text + "\n")
        print("Data successfully appended.")
    except IOError as e:
        print(f"Error appending to file: {e}")
        return

    print("\nFinal content of output.txt:")
    try:
        with open("output.txt", "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Error: output.txt not found.")
    except IOError as e:
        print(f"Error reading file: {e}")

file_operations()