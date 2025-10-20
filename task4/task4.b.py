alist = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    alist.append([name, score])
second_lowest = sorted(set(score for name, score in alist))[1]
names_with_second_lowest = sorted(name for name, score in alist if score == second_lowest)

print('\n'.join(names_with_second_lowest))
