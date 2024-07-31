
# This program determines which pins remain standing after rolling K balls, based on given start and stop positions for each roll, and prints a sequence of N characters where 'I' represents a standing pin and '.' represents a knocked-down pin.

def bowling_pins(N,K):
    pins = ['I'] * N
    for i in range(K):
        start, stop=[int(s) for s in input().split()]
        for j in range(start, stop+1):
            pins[j-1] = '.'
    print(''.join(pins))
    
N,K=[int(s) for s in input().split()]
bowling_pins(N,K)
