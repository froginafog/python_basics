def countdown(start):
    print("countdown(",start, ") is called")
    if(start == 0):
        return 0
    else:
        countdown(start = start - 1)

countdown(5)

"""
countdown( 5 ) is called
countdown( 4 ) is called
countdown( 3 ) is called
countdown( 2 ) is called
countdown( 1 ) is called
countdown( 0 ) is called
"""
