"""
Print out and trace the output of the below program by hand.
"""
def recurse(num):
    if num > 5:
        return
    recurse(num+1)
    recurse(num+2)
    print(num, end=",")

recurse(1)