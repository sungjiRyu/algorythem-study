input = "abadabac"

def find_not_repeating_first_character(string):
    alphbet = [0]*26
    alphbet_count = []

    for char in string:
        alphbet[ord(char) - ord('a')] += 1
    for index in range(len(alphbet)):
        if alphbet[index] == 1:
            alphbet_count.append(chr(index + ord('a')))

    for char in string:
        if char in alphbet_count:
            return char

    return "_"


result = find_not_repeating_first_character
# print("정답 = d 현재 풀이 값 =", result("abadabac"))
# print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))