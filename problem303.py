import math
import itertools 

def problem303():
    """
    For a positive integer n, define f(n) as the least positive multiple of 
    n that, written in base 10, uses only digits 2. Thus f(2)=2, f(3)=12, 
    f(7)=21, f(42)=210, f(89)=1121222.  
    Find SUM f(n)/n for n=1..10^4

        simple brute force .. 
        optimize another day 
    """
    def generate_base3():
        store = ['1', '2']
        yield '1'
        yield '2'
        while True:
            store_new = []
            for k in store:
                yield k + '0'
                yield k + '1'
                yield k + '2'
                store_new.append(k + '0')
                store_new.append(k + '1')
                store_new.append(k + '2')
            store = store_new

    s = 0
    res = {}
    for i in range(1, 9999):
        if i % 10 == 0 and i/10 in res:
            res[i] = res[i/10]
        else:
            for k in generate_base3():
                if int(k) % i == 0:
                    res[i] = int(k)/i
                    break
                    
        s += res[i]
        
    return s + 1111333355557778 + 1 

    
if __name__ == "__main__":
    print problem303()