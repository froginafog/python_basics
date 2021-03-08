words = ["apple", "orange", "melon", "strawberry"]

"""
for i in range(0, len(words)):
    print(words[i]," contains ", str(len(words[i])), " characters")
"""
num_words = len(words)
for i in range(0, num_words):
    s = words[i] + " contains " + str(len(words[i])) + " characters"
    print(s)

"""
apple contains 5 characters
orange contains 6 characters
melon contains 5 characters
strawberry contains 10 characters
"""
