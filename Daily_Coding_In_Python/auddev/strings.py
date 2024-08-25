# str1 = str(input())
# d = int(input())
# S = int(input())
# list1 = []
# exs = 0
# for i in range(len(str1)):
#   if(str1[i] == '?'):
#     list1.append(i)
#   else:
#     exs += int(str1[i])
# print(list1)
# print(exs)
      
d = 5
c = 2
sum = 4


def generate_valid_strings(s, d, target_sum):
    question_mark_indices = [i for i, ch in enumerate(s) if ch == '?']
    num_question_marks = len(question_mark_indices)
    valid_strings = []
    
    def backtrack(index, current_sum, current_string):
        if index == num_question_marks:
            if current_sum == target_sum:
                valid_strings.append(''.join(current_string))
            return
        remaining_sum = target_sum - current_sum
        for val in range(d + 1):
            if val > remaining_sum:  
                break
            current_string[question_mark_indices[index]] = str(val)
            backtrack(index + 1, current_sum + val, current_string)

    backtrack(0, sum(int(ch) for ch in s if ch != '?'), list(s))
    return sorted(valid_strings)

s = input().strip()
d = int(input().strip())
target_sum = int(input().strip())
result = generate_valid_strings(s, d, target_sum)
for string in result:
    print(string)





