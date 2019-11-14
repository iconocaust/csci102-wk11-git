# Galen Stevenson
# CSCI 101 - B
# WEEK 1 - LAB 1B
# fibonacci.py

def fib():
    fibs = [1, 2]

    for i in range(1,9):

        ''' 
        implement Fibonacci sequence to calculate the 
        first 10 Fibonacci numbers, note Fn = Fn-1 + Fn-2
        '''

    return fibs

def main():
    print('OUTPUT', fib())

if __name__ == "__main__":
    main()
    
F0=1
F1=1
F2=F1+F0
F3=F2+F1
F4=F3+F2
F5=F4+F3
F6=F5+F4
F7=F6+F5
F8=F7+F6
F9=F8+F7
F10=F9+F8
F11=F10+F9

print ('The first 10 digits of the Fibonacci Sequence are:')
print ('  ')
print ('  ')
print(F1, F2, F3, F4, F5, F6, F7, F8, F9, F10)

