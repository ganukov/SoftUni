from collections import deque

price_bullet = int(input())
size_gun_barrel = int(input())
bullets = [int(x) for x in input().split()]
locks = [int(y) for y in input().split()]
value = int(input())
counter = 0
bullets_st = []
locks_q = deque()
for each in bullets:
    bullets_st.append(each)
for i in locks:
    locks_q.append(i)

while True:

    current_lock = locks_q.popleft()
    current_bullet = bullets_st[-1]
    counter += 1

    if current_lock >= current_bullet:
        bullets_st.pop()
        print('Bang!')
    else:
        locks_q.appendleft(current_lock)
        bullets_st.pop()
        print('Ping!')

    if counter % size_gun_barrel == 0:
        if bullets_st:
            print('Reloading!')
    if not bullets_st:
        if locks_q:
            print(f"Couldn't get through. Locks left: {len(locks_q)}")
            break
        else:
            print(f"{len(bullets) - counter} bullets left. Earned ${value -  (counter * price_bullet)}")
            break
    if bullets_st:
        if not locks_q:
            print(f"{len(bullets) - counter} bullets left. Earned ${value - (counter * price_bullet)}")
            break
