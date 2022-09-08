import time

ll = list(range(1024 * 32))
ss = set(ll)
result = False
start = time.time()
for v in ss:
    result = v in ss
end = time.time()
print(f'Set: {end - start} s')

result = False
start = time.time()
for v in ll:
    result = v in ll
end = time.time()
print(f'List: {end - start} s')