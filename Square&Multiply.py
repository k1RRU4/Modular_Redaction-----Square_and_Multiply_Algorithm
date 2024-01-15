import math
import array as arr
from math import gcd
import time



def fastMod(base,power,n):
    """Implement fast modular exponentiation.
    """
    r=1
    while power > 0:
        if power % 2 == 1:
            r = r * base % n
        base = base**2 % n
        power = power // 2
    return(r)

def Mod(base,power,n):
        return (base **power % n )



def main():
    base = int (input ("donner la base :"))
    power = int (input ("donner la puissance :"))
    n = int (input ("donner le modulo :"))
    
    start_time = time.time()
    print (fastMod(base,power,n))
    print("--- temps pris par square & multiply : %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    print (Mod(base,power,n))
    print("--- temps pris par la fonction Mod : %s seconds ---" % (time.time() - start_time))
    

if __name__ == "__main__":
     main()
