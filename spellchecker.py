from autocorrect import spell

# Function to correct a paragraph
def correct_paragraph(paragraph):
    # Split paragraph into individual words
    words = paragraph.split()
    
    # Correct each word
    corrected_words = [spell(word) for word in words]
    
    # Join corrected words back into a paragraph
    corrected_paragraph = " ".join(corrected_words)
    
    return corrected_paragraph

# Example of correcting a paragraph
paragraph = "Today was a sunny day and I decidid to go for a walk in the park. As I strolled along, I saw many beautifull flowers blooming and chirping birds flying above. It was a perfect day to enjoy natures beauty."
print(f"error paragraph: {paragraph}")
corrected_paragraph = correct_paragraph(paragraph)
print(f"Corrected paragraph: {corrected_paragraph}")
