# Step 1: File Creation
try:
    with open('my_file.txt', 'w') as file:
        file.write("This is the first line of text.\n")
        file.write("Here is the second line with a number: 12345.\n")
        file.write("Finally, the third line contains some symbols: !@#$%^&*().\n")
except Exception as e:
    print(f"An error occurred while writing to the file: {e}")
finally:
    print("File creation step completed.")

# Step 2: File Reading and Display
try:
    with open('my_file.txt', 'r') as file:
        content = file.read()
        print("Contents of 'my_file.txt':")
        print(content)
except FileNotFoundError:
    print("Error: The file 'my_file.txt' was not found.")
except PermissionError:
    print("Error: You do not have permission to read 'my_file.txt'.")
except Exception as e:
    print(f"An unexpected error occurred while reading the file: {e}")
finally:
    print("File reading step completed.")

# Step 3: File Appending
try:
    with open('my_file.txt', 'a') as file:
        file.write("Appending the first additional line.\n")
        file.write("Appending the second additional line with a number: 67890.\n")
        file.write("Appending the third additional line with more symbols: <>?{}[]~.\n")
except Exception as e:
    print(f"An error occurred while appending to the file: {e}")
finally:
    print("File appending step completed.")

# Step 4: Display Updated Content
try:
    with open('my_file.txt', 'r') as file:
        updated_content = file.read()
        print("Updated contents of 'my_file.txt':")
        print(updated_content)
except FileNotFoundError:
    print("Error: The file 'my_file.txt' was not found.")
except PermissionError:
    print("Error: You do not have permission to read 'my_file.txt'.")
except Exception as e:
    print(f"An unexpected error occurred while reading the file: {e}")
finally:
    print("Final file reading step completed.")
