import random
from mpmath import *
import math

# Global decimal precision, 1000 decimal points.
mp.dps = 1000


def main():

    # Get the length of message.
    messageLength = get_messageLength()
    # Calculate the truncation space.
    decimalLength = get_decimalLength(messageLength)
    # Request the public key. This should be a irrational number.
    publicKey = get_publicKey(decimalLength)
    print()
    print('public key:', publicKey)
    # Generate random number a or b.
    # n = decimalLength # Arbitrary or length of message?
    n = 10  # generate 10 digit numbers.
    a = get_ab(n)
    b = get_ab(n)
    print()
    print('Alice\'s secret a:', a)
    print('Bob\'s secret b:', b)

    # get parameter prim, e.g. a' or b'
    a_prim = get_prim(a, publicKey)
    b_prim = get_prim(b, publicKey)
    print()
    print('Alice\'s a_prim:', a_prim)
    print('Bob\'s b_prim:', b_prim)


    # Shared secret k.
    k_a = get_k(a, b_prim)
    k_b = get_k(b, a_prim)
    print()
    print('Alice\'s shared secret k:', k_a)
    print('Bob\'s shared secret k:', k_b)

    # Check if respective calculated k is the same.
    check_k(k_a, k_b)


def check_k(k_a, k_b):
    if k_a == k_b:
        print()
        print('[+] Calculated shared secret is the same.')
    else:
        print()
        print('[-] Shared secret is not the same.')


def get_k(parameter, prim):
    # The persons own secret parameter, with the prim of the other person.
    k = str(parameter * prim)
    split = k.split('.') # same as mod 1.
    k = '0.' + split[1]
    return mpf(k)


def get_prim(parameter, publicKey):
    # parameter is either a or b.
    prim = str(parameter * publicKey)
    split = prim.split('.') # same as mod 1.
    prim = '0.' + split[1]
    return mpf(prim)

def get_ab(n):
    # Dn{10^(n-1), ..., 10^n - 1}
    lowerBound = 10 ** (n - 1)
    upperBound = (10 ** n) - 1
    return random.randint(lowerBound, upperBound)


def get_publicKey(decimalLength):
    # Provide exponent to e.
    while True:
        print('Provide the exponent to e, to generate the irrational number.')
        try:
            exponent = mpf(input('> '))
            split = str(exponent).split('.')
            if split[1] == str(0):   # If an integer is given.
                exponent = int(exponent)
            break
        except:
            print('Not a valid input')
    decimals = str(mpf(math.exp(exponent)))
    split = decimals.split('.')
    decimals = split[1][:decimalLength] # Only decimalLength number of decimals.
    publicKey = '0.'+ decimals
    return mpf(publicKey)


def get_decimalLength(messageLength):
    # Calculate the decimalLength, truncation space necessary. Given by 2N+1
    return 2 * messageLength + 1


def get_messageLength():
    # Get the message length from user.
    while True:
        try:
            print('Length of plaintext message: ')
            messageLength = int(input('> '))
            if messageLength in range(1, 5000+1):
                break
            else:
                print('Message is too long or too short.')
        except:
            print('Not a valid input')
    return messageLength


if __name__ == '__main__':
    main()
