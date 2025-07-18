try:
    # Open file in write mode

    f =  r"C:\Users\lenovo\Documents\julypyton.txt"
    with open(f, "w") as file:
        sentence = "Python makes file handling easy!"
        file.write(sentence)
        print("Sentence written to file successfully.")

except FileNotFoundError:
    print("Error: The file path was not found.")

except PermissionError:
    print("Error: You don't have permission to write to this file.")

except Exception as e:
    print("An unexpected error occurred:", e)
