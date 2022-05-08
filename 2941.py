import sys

read = lambda: sys.stdin.readline().rstrip()

croatia_alphabets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

S = read()

for alphabet in croatia_alphabets:
    S = S.replace(alphabet, '*')

print(len(S))