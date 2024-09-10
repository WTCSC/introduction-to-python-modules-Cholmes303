"""
Import the text_utils module you created and calculate the average number of
words per line in a given text file. The text file that will be used to test
this is the text file called "sample.txt" (located in the same directory as
this exercise). The average number of words per line should be rounded down to
the nearest integer.

Print the average number of words per line in the text file in the following
format:

"Average words per line: [average]"
"""

#pulls text_utils file to count the words in sample.txt
import text_utils as tu

#creates function that defines average words of file
def average_words(): 

    #opens sample.txt file and reads
    file = open('sample.txt', 'r')
    
    #translate file into text
    text = file.read()

    #returns the program reading the file back to the start when it does not have any lines left to read
    file.seek(0)

    #sets text equal to reading file lines
    lines = len(file.readlines())

    #sets words to word count of file
    words = tu.count_words(text)

    #divides words per text and floors with //
    average = words//lines
    
    #closes file to stop running
    file.close()

    #returns average words in file per line
    return f'Average words per line: {average}'

print(average_words())
