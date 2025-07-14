# String Search Module
# Finds all case insensitive matches of a subtext in a main string
# without using any restricted built-in methods.

#Convert uppercase letter to lowercase ASCII format
# Character between A and Z to lower case.
#ASCII value 32
def ascii_lower(text):
    result = ""
    for c in text:
        if 'A' <= c <= 'Z':
            result += chr(ord(c) + 32)
        else:
            result += c
    return result

#Output the length of a string
def find_length(text):
    count = 0
    for _ in text:
        count += 1
    return count

# Changes sentence to lower case doesnt matter if the letter big or small
def find_substring_positions(text, subtext):
    text_lower = ascii_lower(text)
    subtext_lower = ascii_lower(subtext)

    positions = []

    #Check the length of the text
    text_len = find_length(text_lower)
    subtext_len = find_length(subtext_lower)
    
    #If match it remember the position 
    if subtext_len == 0 or text_len == 0 or subtext_len > text_len:
        return []

    #This will keep checking until the end of the sentence
    i = 0
    while i <= text_len - subtext_len:
        match = True
        j = 0
        while j < subtext_len:
            if text_lower[i + j] != subtext_lower[j]:
                match = False
                break
            j += 1
        if match:
            positions.append(i)
        i += 1

    return positions

#Check list empty
#If found build a result as a string
def format_position(positions):
    if not positions:
        return "<Sorry nothing matched>"
    
    result = ""
    for i in range(find_length(positions)):
        if i > 0:
            result += ", "
        result += str(positions[i] + 1)
    return result
