shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]

# 답안
def get_max_discounted_price(prices, coupons):
    # 쿠폰과 가격을 내림차순으로 정렬
    prices.sort(reverse=True)
    coupons.sort(reverse=True)

    price_index = 0
    coupon_index = 0
    max_discounted_price = 0

    # 쿠폰과 가격을 매칭시켜 할인된 가격을 더해준다.
    while price_index < len(prices) and coupon_index < len(coupons):
        discounted_price = prices[price_index] * (100 - coupons[coupon_index]) / 100
        max_discounted_price += discounted_price
        price_index += 1
        coupon_index += 1

    # 쿠폰과 매칭되지 않는 가격을 더해준다.
    while price_index < len(prices):
        max_discounted_price += prices[price_index]
        price_index += 1


    return max_discounted_price

# 다른 풀이
def get_max_discounted_price(prices, coupons):
    # 쿠폰과 가격을 내림차순으로 정렬
    prices.sort(reverse=True)
    coupons.sort(reverse=True)

    max_discounted_price = 0

    # 가격의 갯수만큼 루프
    for i in range(len(prices)):
        if i < len(coupons):
            discounted_price = prices[i] * (100 - coupons[i]) / 100
            max_discounted_price += discounted_price
        else:
            max_discounted_price += prices[i]

    return max_discounted_price


print("정답 = 926000 / 현재 풀이 값 = ", get_max_discounted_price([30000, 2000, 1500000], [20, 40]))
print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], [10, 70, 30, 20]))
print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], []))
print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price([20000, 100000, 1500000], [10, 10, 10]))