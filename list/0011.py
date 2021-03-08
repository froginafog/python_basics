letters = ['d', 'e' , 'a', 'b', 'c']

print("letters:", letters)
letters.sort()
print("letters.sort() is called")
print("letters:", letters)
letters.sort(reverse = True)
print("letters.sort(reverse = True) is called")
print("letters:", letters)


"""
letters: ['d', 'e', 'a', 'b', 'c']
letters.sort() is called
letters: ['a', 'b', 'c', 'd', 'e']
letters.sort(reverse = True) is called
letters: ['e', 'd', 'c', 'b', 'a']
"""
