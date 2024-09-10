def count_chars(text):
    """
    Count the number of characters in a text
    """
    
    #len() counts the string in text
    char = len(text)
    
    return char

def count_words(text):
    """
    Count the number of words in a text
    """
    
    #.split() moves text into words based on spaces, len() counts those words
    length = len(text.split())
    
    return length

def count_sentences(text):
    """
    Count the number of sentences in a text
    """
    
    #starts count at 0 for sentences
    sentence_count = 0

    #defines and loops through text looking for char 
    for char in text:
        
        #compares the char to !, ?, or . and counts them
        if char == '!' or char == '?' or char == '.':
        
            #adds each occurrence for a total sentence count
            sentence_count += 1
    
    return sentence_count
