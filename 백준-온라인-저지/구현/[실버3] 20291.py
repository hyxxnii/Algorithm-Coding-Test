n = int(input())

from collections import defaultdict
files = defaultdict(dict)

for _ in range(n):
    file = input()
    key = file.split(".")[1]
    try:
        files[file.split(".")[1]] += 1
    except:
        files[file.split(".")[1]] = 1
    
keys = list(files.keys())

# sorted 함수: 영어로 됨
keys = sorted(keys)

for k in keys:
    print(k, files[k])