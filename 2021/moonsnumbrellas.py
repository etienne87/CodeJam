from collections import defaultdict


def get_min_cost(seq, cj, jc):
    mem_c = dict() 
    mem_j = dict() 
    def helper(i, curr_cost=0, last=None):
        nonlocal mem_c
        nonlocal mem_j
        nonlocal seq 
        nonlocal cj
        nonlocal jc

        if i == len(seq):
            return curr_cost

        c = seq[i]
        total = curr_cost
        if c == 'C': 
            res = jc if last == 'J' else 0
            total = helper(i+1, curr_cost + res, 'C')
        elif c == 'J':
            res = cj if last == 'C' else 0
            total = helper(i+1, curr_cost + res, 'J')
        elif c == '?':
            if i not in mem_j:
                res = cj if last == 'C' else 0
                mem_j[i] = helper(i+1, curr_cost + res, 'J')
            if i not in mem_c:
                res = jc if last == 'J' else 0
                mem_c[i] = helper(i+1, curr_cost + res, 'C')
            total = min(mem_c[i], mem_j[i])

        return total 
    
    return helper(0) 
    

def read_file(f):
    cases = []
    with open(f, 'r') as f:
        num_cases = int(f.readline())
        for case_num in range(1, num_cases+1):
            s = f.readline().strip('\n')
            cj, jc = list(map(int, s[:4].split()))
            seq = s[4:] 
            cases += [(cj,jc,seq)]
        return cases
            



def main(f):
    cases = read_file('moonsumbrellas_file.txt')
    for case_num, case in enumerate(cases):
        cj, jc, seq = case
        cost = get_min_cost(seq, cj, jc)
        print(f"Case #{case_num} {case}: {cost}")

if __name__ == '__main__':
    import fire;fire.Fire(main)
