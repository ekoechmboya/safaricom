def read_and_write_file(input_filename, output_filename):
    try:
        # Open the input file for reading
        with open(input_filename, 'r') as infile:
            content = infile.read()
        
        # Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()
        
        # Write the modified content to the output file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"Content successfully written to {output_filename}")
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Usage
input_file = input("Enter the name of the input file: ")
output_file = input("Enter the name of the output file: ")
read_and_write_file(input_file, output_file)


def read_file_with_error_handling():
    try:
        filename = input("Enter the filename to read: ")
        with open(filename, 'r') as file:
            print("File content:")
            print(file.read())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied for accessing the file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Usage
read_file_with_error_handling()
