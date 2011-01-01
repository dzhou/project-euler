import math


def problem297():
    """ Each new term in the Fibonacci sequence is generated by adding the 
    previous two terms. Starting with 1 and 2, the first 10 terms will be: 
    1, 2, 3, 5, 8, 13, 21, 34, 55, 89. 

    Every positive integer can be uniquely written as a sum of 
    nonconsecutive terms of the Fibonacci sequence. For example, 100 = 3 + 8 
    + 89. Such a sum is called the Zeckendorf representation of the number. 

    For any integer n>0, let z(n) be the number of terms in the Zeckendorf 
    representation of n. Thus, z(5)=1, z(14)=2, z(100)=3 etc. Also, 
    for 0<10^6, SUM z(n)=7894453. 

    Find SUM z(n) for 0<n<10^17. 
    """
    fsrs = {0:1, 1:1, 2:2, 3:3, 4:5, 5:6}
    fibs = {1:1, 2:2}
    for c in range(3,100):
        fibs[c] = fibs[c-1] + fibs[c-2]
    fibs_list = fibs.values()
    fibs_list.sort(reverse=True)
    fibs = dict([(k,True) for k in fibs_list])
    
    def last_fib(k):
        for n in fibs_list:
            if n < k:
                return n 

    def zeckendorf(k):
        if k in fsrs:
            return fsrs[k]
        if k in fibs:
            fsrs[k] = zeckendorf(k-1) + 1
        else:
            f_n_1 = last_fib(k)
            fsrs[k] = zeckendorf(f_n_1) + zeckendorf(k - f_n_1) + k - f_n_1
        return fsrs[k]
    
    return zeckendorf(10**17-1)

    
if __name__=="__main__":
    print problem297()