
# We will define a countElements function that essentially does the same thing 
# as len(list), but better. It returns an approximation of the number of elements 
# in the list.

# This function is able to count these elements with complexity O(n*ln(n)). The
# output will most often be within [n/4,4*n].
# However, in theory it may not always terminate, even for small values of n.

from random import random

def countElements(list):
    print("\nThrowing balls down the stairs...")
    maxi = 0
    for i in list :
        steps = 0
        while random() > 1/2:
            steps += 1
        if steps > maxi:
            maxi = steps
    print("One of the balls fell "+str(maxi) +" steps !")
    print("Therefore, you threw approximately "+str(2**(maxi+1)) +" balls.")
    return 2**(maxi+1)

def simulation():
    n = int(input("How many balls do you want to throw : "))
    if n>10000000:
        print("Keep calm, my algorithm is good, but not THAT good.")
        print("I'm not accepting this input because I don't want your PC to burn.")
        return
    a = [random() for i in range(n)]
    out = countElements(a)
    error = str(1-min(n,out)/max(n,out))
    if len(error)>5:
        error = error[:5]
    print("Error : "+error+"%")
    
simulation()