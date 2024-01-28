import time


def lowest_v1(value):
    result = 2*value
    rem = False
    while not rem:
        rem = True
        for i in range(value-1, 2, -1):
            if result % i:
                rem = False
                result += value
                break
    return result

def lowest_v2(value):
    result = 2*value
    rem = False
    while not rem:
        rem = True
        for i in range(value-1, 1, -1):
            reminder = result % i
            if reminder:
                rem = False
                if i == value-1:
                    # print(1)
                    result += value*(i-reminder)
                else:
                    # print(2)
                    result += value
                break

    return result

def lowest_v3(value):
    result = 2*value
    rem = False
    while not rem:
        rem = True    
        for i in range(value-1, 1, -1):
            reminder = result % i
            if reminder:
                rem = False
                if i == value-1:
                    # print(1)
                    result += value*(value-1-reminder)
                else:
                    result += value*(value-1)
                break
    return result


def temp(val_in:int, result:int) -> (bool, int):
    for i in range(val_in, 1, -1):
        reminder = result % i
        if reminder:
            if i == val_in:
                result += (val_in+1)*(val_in-reminder)
            else:
                result += (val_in+1)*val_in
            return True, result
    return False, result

def lowest_v4(value:int) -> int:
    val_in = value-1
    result = 2 * value
    rem = True
    while rem:
        rem, result = temp(val_in, result)
    return result


# print(lowest_v4(22))
# print(time.process_time())
# print("____________________________________________________")
# print(lowest_v3(22))
# print(time.process_time())

# print("____________________________________________________")
# print(lowest_v3(25))
# print(time.process_time())
print("____________________________________________________")
print(lowest_v4(25))
print(time.process_time())

