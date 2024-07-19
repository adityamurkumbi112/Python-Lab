#Write a function in Python to count and display the total number of words in a text file “ABC.txt”


def count_words_in_file(file_name):
    try:
        # Open the file in read mode
        with open("C:\\Demo\\abc.txt", 'r') as file:
            # Read the entire content of the file
            text = file.read()
            
            # Split the text into words based on whitespace
            words = text.split()
            
            # Count the number of words
            word_count = len(words)
        
        # Display the total word count
        print(f"Total number of words in {file_name}: {word_count}")
    except FileNotFoundError:
        # Handle the case where the file does not exist
        print(f"The file {file_name} was not found.")
    except Exception as e:
        # Handle any other exceptions that may occur
        print(f"An error occurred: {e}")

# Call the function with the filename 'ABC.txt'
count_words_in_file('ABC.txt')



#output:Total number of words in ABC.txt: 5
