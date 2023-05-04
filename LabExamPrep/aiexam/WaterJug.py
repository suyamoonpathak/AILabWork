import math
import time

def runner(a,b,capA,capB,tar):
    # a = jug1
    # b = jug2

    # if b is target then return
    if (b == tar):
        return
    # if b is full then pour value all a in b and empty a
    # or a is not 0 and b is 0
    elif (b == capB) or (a != 0 and b == 0):
        b = a
        a = 0
    # if a is target if empty b
    elif a == tar:
        b = 0
    # if a is less than target then fill full a
    elif a < capA:
        a = capA
    # if a is less than difference between capacity of b and jug2 then fill b wiht a+b and empty a
    elif a < (capB - b):
        b = a+b
        a = 0
    # else if nothing
    else:
        a = a - (capB-b)
        b = b + (capB-b)
    print(a,b)
    runner(a,b,capA,capB,tar)


if __name__ == "__main__":
    a = 0
    b = 0
    capA = int(input("Enter capacity A : "))
    capB = int(input("Enter capacity B : "))
    tar = int(input("Enter Target : "))

    if (capA > capB):
        capA, capB = capB, capA

    rem = math.gcd(capA, capB)%tar

    if (rem != 0):
        print("Steps:")

        start = time.time()
        runner(a,b,capA,capB,tar)
        stop = time.time() - start

        print(f"Time : {stop}")
    else:
        print("Not Possible")