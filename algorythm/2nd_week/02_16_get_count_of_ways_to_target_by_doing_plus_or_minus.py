numbers = [2, 3, 1]
target_number = 0

result = []

# 모든 경우의 수를 다 확인해야함 (규칙이 없음) -> DFS, BFS
def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    all_ways = []

    def get_all_ways_by_doing_plus_or_minus(array, current_index, current_sum):
        if current_index == len(array):
            all_ways.append(current_sum)
            print("End current_index = " + str(current_index) + " current_sum = " + str(current_sum))
            return
        print("current_index = " + str(current_index) + " current_sum = " + str(current_sum))
        get_all_ways_by_doing_plus_or_minus(array, current_index + 1, current_sum + array[current_index])
        get_all_ways_by_doing_plus_or_minus(array, current_index + 1, current_sum - array[current_index])

    get_all_ways_by_doing_plus_or_minus(array, 0,0)

    print(all_ways)
    target_count = 0

    for way in all_ways:
        if target == way:
            target_count += 1

    return target_count

print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!

target = 5
