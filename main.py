import math

def symbol_newtona(n,k):
    return int(math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))



def main():
    wejsciowe_liczby = input()
    wejsciowe_liczby = wejsciowe_liczby.split(' ')
    n = int(wejsciowe_liczby[0])
    k = int(wejsciowe_liczby[1])
    print(symbol_newtona(n,k))


if __name__ == '__main__':
    main()