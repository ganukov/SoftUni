def loading_bar(num):
    loading_status = f""
    if num == 100:
        print(f"100% Complete!")
        print("[%%%%%%%%%%]")
    else:
        percent = (num // 10) * "%"
        dots = (10 - (num //10)) * "."

        print(f"{num}% [{percent}{dots}]")
        print("Still loading...")


num = int(input())
loading_bar(num)