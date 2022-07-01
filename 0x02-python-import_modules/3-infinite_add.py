#!/usr/bin/python3
# 3-infinite_add.py
# Toriola Samuel 

if __name__ == "__main__":
    import sys
    a = int(len(sys.argv))
    sum = 0
    i = 1
    while i < a:
        sum += int(sys.argv[i])
        i += 1
    print(sum)
