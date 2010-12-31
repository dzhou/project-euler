import math
import itertools

# Common stuff 
# distance/area formulas that should go into mathlib 
def get_distance((x1,y1), (x2,y2)):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def get_triangle_area(p1, p2, p3):
    # heron's formula 
    a = get_distance(p1, p2)
    b = get_distance(p1, p3)
    c = get_distance(p2, p3)
    s = (a + b + c) / 2.0 
    return math.sqrt(s * (s-a) * (s-b) * (s-c))
# End 


# 
# full_grid_size is a quarter of the original size (since this is 8-fold)
# grid_size is reduced grid by assuming the "arc" will start around 130 
#   ie. we already have (0,250) to ~(130,250)
#
radius = 130 
full_grid_size = 250 
grid_size = 130
source = (0, grid_size)
target = (grid_size, 0)

# ratio here is a rough approx of the final ratio 
# the best ratio (~132.59) is quarter circle with r ~ 130 
# since area/perimeter = ratio -> ratio*perimeter-area = 0 at "shortest path" 
ratio = 132.5


def filter_graph(x, y):
    # restrict valid points on grid 
    # 1. on/above target-source line since the shape must be convex 
    # 2. points within 10 units of quarter circle with r=130
    # (not really necessary but make it a whole lotttt faster 
    return (y >= grid_size - x and
        abs(y - math.sqrt(radius**2 - x**2)) < 10)

# shortest-path algo 
# first build a graph with the above filter 
def get_initial_graph():
    graph = dict(
        ((x,y), (get_weight((x,y),source),source)) for 
            x,y in itertools.product(range(grid_size+1), repeat=2)
            if filter_graph(x, y)
    )
    return graph    
    
# weight between any two points
def get_weight(p1, p2, target_ratio=ratio):
    if p1 == p2:
        return 0 
    perimeter = get_distance(p1, p2)
    area = get_triangle_area(p1, p2, (0,0))
    return target_ratio*perimeter - area 

# this is a direct graph 
# each point can only go to other points with >= X AND <= Y
#   and again filter for points above source-target line 
def get_neighbors((x,y), radius=15):
    for x1 in range(x, min(x+radius, grid_size+1)):
        for y1 in range(y, max(y-radius,-1), -1):
            if (filter_graph(x1, y1) and
                (x != x1 or y != y1)):
                yield (x1, y1)


# Dijkstra's algorithm (shortest path) - pretty straightforward 
def reduce_graph(graph):
    path = []
    nodes = graph.keys()
    while nodes:
        u = min(nodes, key=lambda k: graph[k][0])
        nodes.remove(u)
        if u == target:
            break

        weight, _ = graph[u]
        for n in get_neighbors(u):
            old_weight, _ = graph[n]
            new_weight = weight + get_weight(n, u)
            if new_weight < old_weight:
                graph[n] = (new_weight, u)
    
    return graph 
    
# calculate the final ratio from graph
def calculate_ratio(graph, target, source):
    grid_diff = full_grid_size - grid_size
    area = grid_diff*(full_grid_size*2 - grid_diff)
    perimeter = grid_diff*2    
    current = target
    while current != source:
        perimeter += get_distance(current, graph[current][1])
        area += get_triangle_area(current, graph[current][1], (0,0))  
        current = graph[current][-1]

    return area/perimeter


def problem314():
    graph = get_initial_graph()
    graph = reduce_graph(graph)
    ratio = calculate_ratio(graph, target, source)
    return round(ratio,8)
    
    

if __name__ == "__main__":      
    print problem314()
    
    