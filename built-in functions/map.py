# The map() function executes a specified function for each item in an iterable.
# The item is sent to the function as a parameter.

def countTheLengthOfEachWord(word):
    return len(word)

words = ["apple", "orange", "strawberry"]
wordLengths = map(countTheLengthOfEachWord, words)
print("wordLengths:", list(wordLengths))
    
"""
wordLengths: [5, 6, 10]
"""
