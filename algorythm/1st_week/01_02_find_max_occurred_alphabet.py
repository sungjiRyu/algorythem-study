
def find_max_occurred_alphabet(string):
    # 이 부분을 채워보세요!
    occurred_alphabet_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        index = ord(char) - ord('a')
        occurred_alphabet_array[index] += 1

    max_alphabet_count = 0
    for count_alphabet in occurred_alphabet_array:
        if count_alphabet > max_alphabet_count:
            max_alphabet_count = count_alphabet

    max_alphabet_index = occurred_alphabet_array.index(max_alphabet_count)

    return chr(ord('a') + max_alphabet_index)


result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))