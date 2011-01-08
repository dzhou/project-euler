import math


def get_distance(v, r, h, g=9.81):
    r = math.radians(r)
    d = v*math.cos(r) / g
    d *= (v*math.sin(r) + math.sqrt((v*math.sin(r))**2 + 2*g*h))
    return d 

def get_max_height(v, r, h, g=9.81):
    return h + (v * math.sin(math.radians(r))) ** 2 / (g*2)
    
def get_max_distance(v, h, iteration=20):
    increment = 1.0/1000
    max_d = 0
    r = 0

    while iteration > 0:
        d = get_distance(20, r, 100)
        if d > max_d:
            max_d = d
            r += increment
        else:
            r -= increment
            increment /= 10 
            iteration -= 1 

    return max_d

    
def problem317():    
    """
    A firecracker explodes at a height of 100 m above level ground. It 
    breaks into a large number of very small fragments, which move in every 
    direction; all of them have the same initial velocity of 20 m/s. 

    We assume that the fragments move without air resistance, in a uniform 
    gravitational field with g=9.81 m/s2. 

    Find the volume (in m3) of the region through which the fragments move 
    before reaching the ground. Give your answer rounded to four decimal 
    places. """
    # 
    # equation of parabola: y = a*x^2 + b 
    # find a,b using (0, max_h) and (max_x, 0)
    # and calc solid of revolution 
    #
    max_x = get_max_distance(20, 100)
    b = get_max_height(20, 90, 100)
    a = -b / (max_x**2)
    f = lambda x: a*x**2 + b 

    # integrate x=[0..max_x]
    x = 0
    volume = 0
    increment = 0.0001
    while x <= max_x:
        h = (f(x) + f(x+increment)) / 2.0
        volume += math.pi * ((x+increment)**2-x**2) * h
        x += increment

    return round(volume,4)
    
    
if __name__=="__main__":
    print problem317()

