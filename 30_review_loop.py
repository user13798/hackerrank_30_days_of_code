# Enter your code here. Read input from STDIN. Print output to STDOUT

s="""1
Hacker
Rank"""
# s = str(input().strip())

lines = s.splitlines()
T=int(lines[0])
result_str = ""

for line in lines[1:T+1]:
    evens = ""
    odds = ""
    result_line = ""
    for index in range(len(line)):
        if index % 2 == 0:
            evens += line[index]
        elif index % 2 == 1:
            odds += line[index]
    result_line = f"{evens} {odds}\n"
    result_str += result_line

print(result_str)
