#!/usr/bin/python3


if __name__=='__main__':
    try:
        num_string=input("please enter two numbers:")
        n,k=num_string.split(' ')
        n=int(n)
        k=int(k)
        for x in range(2,10**600):
            if n**x % (10**k)==n%(10**k):
                print(x)
                break
        else:
            print(1)
    except:
        print("Please check your input!!!")
