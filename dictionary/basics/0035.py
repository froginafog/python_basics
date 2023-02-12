dictionary_of_matrices = {
                                'A': [
                                        ['a11', 'a12', 'a13', 'a14', 'a15'],
                                        ['a21', 'a22', 'a23', 'a24', 'a25'],
                                        ['a31', 'a32', 'a33', 'a34', 'a35']
                                     ],
                                'B': [
                                        ['b11', 'b12', 'b13', 'b14', 'b15'],
                                        ['b21', 'b22', 'b23', 'b24', 'b25'],
                                        ['b31', 'b32', 'b33', 'b34', 'b35']
                                     ]
                         }

for key in dictionary_of_matrices:
    print('key:', key)
    matrix = dictionary_of_matrices[key]
    for row in matrix:
        for item in row:
            print(item, end = '\t')
        print()
    print('------------------------------------')

"""
key: A
a11	a12	a13	a14	a15	
a21	a22	a23	a24	a25	
a31	a32	a33	a34	a35	
------------------------------------
key: B
b11	b12	b13	b14	b15	
b21	b22	b23	b24	b25	
b31	b32	b33	b34	b35	
------------------------------------
"""
