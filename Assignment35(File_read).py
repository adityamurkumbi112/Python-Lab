#Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen.

def read_and_display_file(file_name):
    try:
        # Open the file in read mode
        with open("C:\\Demo\\abc.txt", 'r') as file:
            # Iterate over each line in the file
            for line in file:
                # Print the line after stripping leading/trailing whitespace
                print(line.strip())
    except FileNotFoundError:
        # Handle the case where the file does not exist
        print(f"The file {C:\\Demo\\abc.txt} was not found.")
    except Exception as e:
        # Handle any other exceptions that may occur
        print(f"An error occurred: {e}")

# Call the function with the filename 'ABC.txt'
read_and_display_file("C:\\Demo\\abc.txt")


"""
Output:
abc
1254
hjd
456
"""
