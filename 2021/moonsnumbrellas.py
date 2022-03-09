from collections import defaultdict


def get_min_cost(seq, cj, jc):
    memory = dict() 
    def helper(i, last="", result=[]):
        nonlocal memory
        nonlocal seq 
        nonlocal cj
        nonlocal jc

        w = list(result) + [last] 
        

        if i == len(seq):
            return 0 

        c = seq[i]
        def res_fun(l,c):
            lc = l+c
            if lc == 'CJ':
                return cj
            elif lc == 'JC':
                return jc
            else:
                return 0

        res = res_fun(last, c) 

        total = 0
        if c == 'C': 
            total = helper(i+1, 'C', w) + res
        elif c == 'J':
            total = helper(i+1, 'J', w) + res
        elif c == '?':
            ra = res_fun(last, 'J') 
            rb = res_fun(last, 'C') 
            a = helper(i+1, 'J', w) + ra
            b = helper(i+1, 'C', w) + rb
            total = min(a,b)
            

        memory[i] = total 

        return total 
    
    return helper(0) 
    

def read_file(f):
    cases = []
    with open(f, 'r') as f:
        num_cases = int(f.readline())
        for case_num in range(1, num_cases+1):
            s = f.readline().strip('\n')
            cj, jc = list(map(int, s[:4].split()))
            seq = s[5:] 
            cases += [(cj,jc,seq)]
        return cases
            



def main_file(f):
    cases = read_file(f)
    for case_num, case in enumerate(cases):
        cj, jc, seq = case
        cost = get_min_cost(seq, cj, jc)
        print(f"Case #{case_num} {case}: {cost}")

def main_input():
    num_cases = int(input())
    for case_num in range(1, num_cases+1):
        s = input()
        cj, jc = list(map(int, s[:5].split()))
        seq = s[5:] 
        print('seq: ', seq)
        cost = get_min_cost(seq, cj, jc)
        print(f"Case #{case_num}: {cost}")
    


if __name__ == '__main__':
    import fire;fire.Fire()
