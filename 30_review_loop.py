# Enter your code here. Read input from STDIN. Print output to STDOUT

result_str = ""

T = int(input())
for j in range(T):
    line = str(input())
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
