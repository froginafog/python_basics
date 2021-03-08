words1 = ["apple", "orange", "melon"]
words2 = ["big", "small", "medium"]
words3 = ["", "", ""]

num_words = len(words1)
for i in range(0, num_words):
    words3[i] = words2[i] + " " + words1[i]

print("words3:", words3)

# words3: ['big apple', 'small orange', 'medium melon']
