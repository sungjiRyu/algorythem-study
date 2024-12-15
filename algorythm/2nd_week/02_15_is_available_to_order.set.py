shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]

# set 사용 (set은 해시 테이블을 기반으로 구현되어 있어 시간 복잡도가 O(1))
def is_available_to_order(menus, orders):
    # O(N) + O(M) * O(1) = O(N + M)
    menus_set = set(menus) # O(N)
    for order in orders: # M -> O(M)
        if order not in menus_set: # O(1)
            return False
    return True

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


result = is_available_to_order(shop_menus, shop_orders)
print(result)

