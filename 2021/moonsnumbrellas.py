import sys  
sys.setrecursionlimit(10000)
from collections import defaultdict


def get_min_cost_1(seq, cj, jc):
    """recursion method

    Note: I do not like this. It is bulky and very hard to debug.
    It is much better to learn how to do DP using for loops!
    """
    memory = dict() 

    xy = defaultdict(int)
    xy['JC'] = jc
    xy['CJ'] = cj
    def f(i, last=""): 
        nonlocal memory
        nonlocal seq 
        nonlocal xy

        if i == len(seq):
            return 0 

        c = seq[i]
        k = (i,last)
        l = (i,'J' if last == 'C' else 'J')
            
        if k not in memory:

        if c == '?':
            a = f(i+1, 'J') + xy[last+'J'] 
            b = f(i+1, 'C') + xy[last+'C']
            cost = min(a,b)
        else:
            cost = f(i+1, c) + xy[last+c] 
        
        if l in memory:
            cost = min(memory[k], memory[l])

        memory[k] = cost 
        
        

        return memory[k] 
    
    min_cost = f(0) 
    return min_cost 


def get_min_cost_2(seq, x, y):
    """no recursion: taken from winner..."""
    n = len(seq)
    dp = [[1e9 for i in range(2)] for j in range(n+1)]  
    dp[0][0] = 0
    dp[1][0] = 0
    for i in range(1, n + 1):
        for c in range(2):
            if c == 0 and seq[i-1] == 'J': # JJ
                continue
            if c == 1 and seq[i-1] == 'C': # CC
                continue
            for d in range(2):
                cost = 0
                if i > 1:
                    if(d == 0 and c == 1): # CJ
                        cost += x
                    if(d == 1 and c == 0): # JC
                        cost += y
                dp[i][c] = min(dp[i][c], dp[i-1][d] + cost)
    return min(dp[n][0], dp[n][1])



def read_file(f):
    cases = []
    with open(f, 'r') as f:
        num_cases = int(f.readline())
        for case_num in range(1, num_cases+1):
            s = f.readline().strip('\n').split()
            cj = int(s[0])
            jc = int(s[1])
            seq = s[2] 
            cases += [(cj,jc,seq)]
        return cases

def main_file(f):
    cases = read_file(f)
    for case_num, case in enumerate(cases):
        cj, jc, seq = case
        cost = get_min_cost_1(seq, cj, jc)
        cost2 = get_min_cost_2(seq, cj, jc)
        print(f"Case #{case_num}: {cost} {cost2}")
        if cost != cost2:
            import pdb;pdb.set_trace()
            pass

def main_input():
    num_cases = int(input())
    for case_num in range(1, num_cases+1):
        s = input().split()
        cj = int(s[0])
        jc = int(s[1])
        seq = s[2] 
        cost = get_min_cost_1(seq, cj, jc)
        print(f"Case #{case_num}: {cost}")
    


if __name__ == '__main__':
    import fire;fire.Fire()
