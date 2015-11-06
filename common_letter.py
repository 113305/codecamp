# Write a function that takes in a string. Your function should return the
# most common letter in the string, and a count of how many times it
# appears.
# string을 가져오는 함수를 입력하세요. 그 함수는 string에서 가장 많이 나타나는 글자를 가져오고, 같은 글자가 몇 번 씩 나타나는지 셉니다.
#
# Difficulty: medium.
# 난이도: 중

def most_common_letter(string):
    char_count = {}
    for c in string:
        if c not in char_count:
            char_count[c]=1
        else:
            char_count[c]+=1
            
    common_letter = ['x', 0]
    
    for c in char_count:
        if common_letter[1] < char_count[c]:
            common_letter[1] = char_count[c]
            common_letter[0] = c

    return common_letter

        



# These are tests to check that your code is working. After writing
# your solution, they should all print true.
# 아래는 코드가 잘 작동되는지 확인하는테스트 입니다. solution을 입력한 뒤에는 모두 true가 나와야 합니다.

print('most_common_letter("abca") == ["a", 2]: ' + str(most_common_letter('abca') == ['a', 2]))

print('most_common_letter("abbab") == ["b", 3]: ' + str(most_common_letter('abbab') == ['b', 3]))
