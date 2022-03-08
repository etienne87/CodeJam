import numpy as np

def reverse_sort_cost(seq):
    total_cost = 0
    for i in range(len(seq)-1):
        j = i + np.argmin(seq[i:])
        print(f'{i}: argmin {j}')
        total_cost += j-i+1 
        seq[i:j+1] = seq[i:j+1][::-1]
        print(f'total cost: {total_cost}')
        print(f'seq: {seq}')

    return total_cost


"""
num_cases = int(input())
for case_num in range(1, num_cases+1):
    num_elem = int(input())
    seq = list(map(int, input().split()))
    seq = np.array(seq)
    total_cost = reverse_sort_cost(seq)
    
    print(f"Case #{case_num}: {total_cost}")
"""

num_elem = int(input())
worst = 0
for i in range(num_elem):
    j = num_elem-1 if i%2 == 0 else i
    worst += j-i+1
print(worst)
