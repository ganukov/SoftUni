def math_operations(*args, **kwargs):

    for each in range(len(args)):
        if each >= 4:
            args = args[each:] + args[each::]
            each = 0

        for key,value in enumerate(kwargs):

            if key == 0 and each == 0:
                kwargs[value] += args[each]
                break
            elif key == 1 and each == 1:
                kwargs[value] -= args[each]
                break
            elif key == 2 and each == 2:
                if args[each] == 0:
                    break
                kwargs[value] /= args[each]
            elif key == 3 and each == 3:
                kwargs[value] *= args[each]
                break


    return kwargs

print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
