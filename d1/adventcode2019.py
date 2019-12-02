input = open('input.txt', 'r')
arr = []
tot = []
i = 0
tot_el = 0


for row in input:
    arr.append(row)
    print(arr)

while i < len(arr):
    for el in arr:
        tot_el = (int(el)//3) - 2
        tot.append(tot_el)
        i += 1

print(sum(tot))
