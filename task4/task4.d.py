def min_paint_balloons(s):
    amber_count = s.count('a')
    brass_count = s.count('b')
    min_paint = min(amber_count, brass_count)
    return min_paint

T = int(input("Enter the total test cases: "))
for i in range(T):
    s = input().strip()
    print(min_paint_balloons(s))
