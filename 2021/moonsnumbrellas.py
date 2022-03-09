import sys  
sys.setrecursionlimit(10000)
from collections import defaultdict


def get_min_cost(seq, cj, jc):
    memory = dict() 

    xy = defaultdict(int)
    xy['JC'] = jc
    xy['CJ'] = cj
    def helper(i, last=""): #, result=""):
        nonlocal memory
        nonlocal seq 
        nonlocal xy

        #w = result + last 
        
        if i == len(seq):
            return 0 

        c = seq[i]
        lc = last + c
        res = xy[lc] 

        k = (i,last)
        if k in memory:
            return memory[k]

        if c == '?':
            ra = xy[last+'J']
            rb = xy[last+'C']
            a = helper(i+1, 'J') + ra
            b = helper(i+1, 'C') + rb
            cost = min(a,b)
            #w = w + 'J' if a > b else w + 'C'
        else:
            cost = helper(i+1, c) + res
            
        
        memory[k] = cost 

        return memory[k] 
    
    return helper(0) 


#def get_min_cost(seq, cj, jc):
    
    


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
