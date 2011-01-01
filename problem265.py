import math


def add_digit(seq_map, n):
    def branch(subseq_map, seq, digit="0"):
        if seq[-(n-1):] + digit not in subseq_map:
            seq0 = seq + digit
            subseq_map0 = dict(subseq_map)
            subseq_map0[seq0[-n:]] = 1 
            seq_map[seq0] = subseq_map0        

    for seq in seq_map.keys():
        subseq_map = seq_map[seq]
        del seq_map[seq]
        branch(subseq_map, seq, "0")
        branch(subseq_map, seq, "1")
    return seq_map    

    
def problem265():
    """
    2N binary digits can be placed in a circle so that all the N-digit 
    clockwise subsequences are distinct. 

    For N=3, two such circular arrangements are possible, ignoring 
    rotations: 

    For the first arrangement, the 3-digit subsequences, in clockwise order, 
    are: 000, 001, 010, 101, 011, 111, 110 and 100. 

    Each circular arrangement can be encoded as a number by concatenating 
    the binary digits starting with the subsequence of all zeros as the most 
    significant bits and proceeding clockwise. The two arrangements for N=3 
    are thus represented as 23 and 29: 

    00010111?2 = 23 00011101?2 = 29 Calling S(N) the sum of the unique 
    numeric representations, we can see that S(3) = 23 + 29 = 52. 

    Find S(5). 
    """    
    # base string 
    seq_map = {"00000": {"00000":1}}
    n = 5 
    # generate all arrangements 
    for i in range(2**n-n):
        seq_map = add_digit(seq_map, n)

    # filter unique arrangements 
    for k in seq_map.keys():
        subseq_map = seq_map[k]
        for i in range(n-1,0,-1):
            a1 = k[-1:] + k[:(n-i)]
            if a1 in subseq_map:
                del seq_map[k]
                break 
            subseq_map[a1] = 1 

    s_n = sum([int(s, base=2) for s in seq_map])
    return s_n 
    
    
if __name__=="__main__":
    print problem265()