def print_formatted(number):
    # your code goes here
    x = len(bin(n)) - 2
    print(bin(n))
    print(x)
    for i in range(1,n+1):
        
        width = len(bin(n)) - 2
        print
        deci = str(i).rjust(width,' ')
        octal = oct(i)[2:].rjust(width, ' ')
        hexx = hex(i)[2:].upper().rjust(width, ' ')
        binary = bin(i)[2:].rjust(width, ' ')
        #print('{} {}  {}  {}' .format(deci, octal[2:], hexx[2:], binary[2:]))
        print(deci, octal, hexx, binary)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
