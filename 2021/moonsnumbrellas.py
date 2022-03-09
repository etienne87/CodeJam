import sys  
sys.setrecursionlimit(10000)
from collections import defaultdict


def get_min_cost(seq, cj, jc):
    memory = dict() 

    xy = defaultdict(int)
    xy['JC'] = jc
    xy['CJ'] = cj
    def helper(i, last=""): 
        nonlocal memory
        nonlocal seq 
        nonlocal xy

        if i == len(seq):
            return 0 

        c = seq[i]
        k = (i,last)
        if k in memory:
            return memory[k]

        if c == '?':
            a = helper(i+1, 'J') + xy[last+'J'] 
            b = helper(i+1, 'C') + xy[last+'C']
            cost = min(a,b)
        else:
            cost = helper(i+1, c) + xy[last+c] 
            
        
        memory[k] = cost 

        return memory[k] 
    
    return helper(0) 



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
        cost = get_min_cost(seq, cj, jc)
        print(f"Case #{case_num}: {cost}")

def main_input():
    num_cases = int(input())
    for case_num in range(1, num_cases+1):
        s = input().split()
        cj = int(s[0])
        jc = int(s[1])
        seq = s[2] 
        cost = get_min_cost(seq, cj, jc)
        print(f"Case #{case_num}: {cost}")
    


if __name__ == '__main__':
    import fire;fire.Fire()
