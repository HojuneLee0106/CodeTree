
import sys

binary_list = list(sys.stdin.readline().strip())
changed = False
for i in range(len(binary_list)):
    if binary_list[i] == '0':
        binary_list[i] = '1'
        changed = True
        break 
if not changed:
    binary_list[-1] = '0'
binary_str = "".join(binary_list)
print(int(binary_str, 2))