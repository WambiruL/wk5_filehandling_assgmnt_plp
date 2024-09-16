# Create a Python script (file_handling_assignment.py) that does the following:
# Creates a new text file named "my_file.txt" in write mode ('w').
# Write at least three lines of text to the file, including a mix of strings and numbers.
try:
    with open("my_file.txt", 'w') as file:
        file.write("Hello, this is the first line.\n")
        file.write("This is line number 2 with a number: 42.\n")
        file.write("Line 3 says: Python file handling is fun!\n")
except PermissionError:
    print("Error: You don't have permission to write to the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("File creation attempt complete.")

# File Reading and Display:
# Enhance your script to read the contents of "my_file.txt" and display them on the console.
try:
    with open("my_file.txt", 'r') as file:
        content = file.read()
        print("\nContents of 'my_file.txt':")
        print(content)
except FileNotFoundError:
    print("Error: The file 'my_file.txt' was not found.")
except PermissionError:
    print("Error: You don't have permission to read the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("File reading attempt complete.")
    
# File Appending:
# Modify the script to open "my_file.txt" in append mode ('a').
# Append three additional lines of text to the existing content.
try:
    with open("my_file.txt", 'a') as file:
        file.write("Here is an additional line.\n")
        file.write("Appending another line with a number: 100.\n")
        file.write("Finally, the third appended line wraps up!\n")
except PermissionError:
    print("Error: You don't have permission to append to the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("File append attempt complete.")
    
# Re-read and display the updated contents after appending
try:
    with open("my_file.txt", 'r') as file:
        updated_content = file.read()
        print("\nUpdated contents of 'my_file.txt' after appending:")
        print(updated_content)
except FileNotFoundError:
    print("Error: The file 'my_file.txt' was not found.")
except PermissionError:
    print("Error: You don't have permission to read the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("Final file reading attempt complete.")