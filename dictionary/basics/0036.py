dictionary_of_dictionaries_of_matrices = {
                                                'dictionary_1':[
                                                                    {
                                                                        'A': [
                                                                                    ['a11', 'a12', 'a13', 'a14', 'a15'],
                                                                                    ['a21', 'a22', 'a23', 'a24', 'a25'],
                                                                                    ['a31', 'a32', 'a33', 'a34', 'a35']
                                                                             ]
                                                                    },
                                                                    {
                                                                        'B': [
                                                                                    ['b11', 'b12', 'b13', 'b14', 'b15'],
                                                                                    ['b21', 'b22', 'b23', 'b24', 'b25'],
                                                                                    ['b31', 'b32', 'b33', 'b34', 'b35']
                                                                             ]
                                                                    }
                                                               ],
                                                'dictionary_2':[
                                                                    {
                                                                        'C': [
                                                                                    ['c11', 'c12', 'c13', 'c14', 'c15'],
                                                                                    ['c21', 'c22', 'c23', 'c24', 'c25'],
                                                                                    ['c31', 'c32', 'c33', 'c34', 'c35']
                                                                             ]
                                                                    },
                                                                    {
                                                                        'D': [
                                                                                    ['d11', 'd12', 'd13', 'd14', 'd15'],
                                                                                    ['d21', 'd22', 'd23', 'd24', 'd25'],
                                                                                    ['d31', 'd32', 'd33', 'd34', 'd35']
                                                                             ]
                                                                    }
                                                               ]                
                                           }
 
for key_of_dictionary_of_dictionaries_of_matrices in dictionary_of_dictionaries_of_matrices:
    print('key_of_dictionary_of_dictionaries_of_matrices:', key_of_dictionary_of_dictionaries_of_matrices)
    list_of_dictionaries = dictionary_of_dictionaries_of_matrices[key_of_dictionary_of_dictionaries_of_matrices]
    for dictionary in list_of_dictionaries:
        for key_of_dictionary in dictionary:
            print('key_of_dictionary:', key_of_dictionary)
            matrix = dictionary[key_of_dictionary]
            for row in matrix:
                for item in row:
                    print(item, end = '\t')
                print()
            print('-------------------------------------------------------------')
    print('=============================================================')

"""
key_of_dictionary_of_dictionaries_of_matrices: dictionary_1
key_of_dictionary: A
a11	a12	a13	a14	a15	
a21	a22	a23	a24	a25	
a31	a32	a33	a34	a35	
-------------------------------------------------------------
key_of_dictionary: B
b11	b12	b13	b14	b15	
b21	b22	b23	b24	b25	
b31	b32	b33	b34	b35	
-------------------------------------------------------------
=============================================================
key_of_dictionary_of_dictionaries_of_matrices: dictionary_2
key_of_dictionary: C
c11	c12	c13	c14	c15	
c21	c22	c23	c24	c25	
c31	c32	c33	c34	c35	
-------------------------------------------------------------
key_of_dictionary: D
d11	d12	d13	d14	d15	
d21	d22	d23	d24	d25	
d31	d32	d33	d34	d35	
-------------------------------------------------------------
=============================================================
"""
