finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

# 왜 False 가 나옴?? => 이진탐색은 정렬이 되어있어야 사용할 수 있다.
def is_exist_target_number_binary(target, array):

    # index
    current_min = 0
    current_max = len(array) - 1
    current_guess = (current_max - current_min) // 2

    while current_min <= current_max:
        if array[current_guess] == target:
            return True
        elif array[current_guess] <= target:
            current_min = current_guess + 1
        else:
            current_max = current_guess - 1
        current_guess = (current_max - current_min) // 2

    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)