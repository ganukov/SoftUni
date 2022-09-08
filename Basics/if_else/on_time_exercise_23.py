h_ex = int(input())
m_ex = int(input())
h_ar = int(input())
m_ar = int(input())
total_h_ex = h_ex * 60 + m_ex
total_h_ar = h_ar * 60 + m_ar
diff = abs(total_h_ex - total_h_ar)
hour = diff // 60
minutes = diff % 60

if total_h_ar == total_h_ex:
    print("On time")
elif total_h_ex > total_h_ar:
    if diff <= 30:
        print("On time")
        print(f"{diff} minutes before the start")
    elif 30 < diff <= 59:
        print("Early")
        print(f"{diff} minutes before the start")
    else:
        print("Early")
        print(f"{hour}:{minutes:02d} hours before the start")
elif total_h_ar > total_h_ex:
    print("Late")
    if diff < 60:
        print(f"{diff} minutes after the start")
    else:
        print(f"{hour}:{minutes:02d} hours after the start")


