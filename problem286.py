import math


def problem286():
    """
    Barbara is a mathematician and a basketball player. She has found that 
    the probability of scoring a point when shooting from a distance x is 
    exactly (1- x/q), where q is a real constant greater than 50. 

    During each practice run, she takes shots from distances x=?1, x=2, 
    ..., x=50 and, according to her records, she has precisely a 2% 
    chance to score a total of exactly 20 points. 

    Find q and give your answer rounded to 10 decimal places. 
    """
    # dynamic programming + binary search 
    def calc_probability(x):
        q_map = {}
        q_map[(0,1)] = (1/x)
        q_map[(1,1)] = 1-(1/x)
        
        def Q(n,m):
            if n > m or n < 0:
                return 0 
            if (n,m) not in q_map:
                q_map[(n,m)] = (1-(m/x))*Q(n-1,m-1) + (m/x)*Q(n,m-1)
            return q_map[(n,m)]

        return Q(20,50)
    

    high_x = 100.0
    low_x = 50.0 
    for k in range(100):
        mid = (high_x + low_x) / 2
        x = calc_probability(mid)
        if x > 0.02:
            low_x = mid 
        elif x < 0.02:
            high_x = mid        
        else:
            break 

    return mid 

    
if __name__=="__main__":
    print problem286()