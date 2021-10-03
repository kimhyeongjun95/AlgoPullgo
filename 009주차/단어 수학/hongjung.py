import sys

N = int(sys.stdin.readline())
words = [sys.stdin.readline().rstrip() for _ in range(N)]

max_len = 0
for word in words:
    if len(word) > max_len:
        max_len = len(word)

words_dict = {}
for a in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    words_dict[a] = [0] * max_len

for i in range(max_len-1, -1, -1):
    for word in words:
        try:
            words_dict[word[::-1][i]][max_len-i-1] += 1
        except:
            pass

num_list = []
for l in words_dict.values():
    n = max_len - 1
    if sum(l):
        temp = 0
        for i in l:
            temp += i * (10 ** n)
            n -= 1
        num_list.append(temp)

num_list.sort(reverse=True)
result = 0
n = 9
for l in num_list:
    result += l * n
    n -= 1

print(result)



# import sys 바로 틀림.

# N = int(sys.stdin.readline())
# words = [sys.stdin.readline().rstrip() for _ in range(N)]

# num_cnt_list = [[] for _ in range(10)]
# n = 9
# for i in range(7, -1, -1):
#     for word in words:
#         try:
#             num_cnt_list[i].append(word[::-1][i])
#         except:
#             pass

# word_dict = {}
# n = 9
# for cnt_list in num_cnt_list[::-1]:
#     if cnt_list:
#         temp_list = []
#         for w in cnt_list:
#             if [cnt_list.count(w), w] not in temp_list:
#                 temp_list.append([cnt_list.count(w), w])
#         temp_list.sort(reverse=True)
#         for t in temp_list:
#             if t[1] not in word_dict.keys():
#                 word_dict[t[1]] = n
#                 n -= 1
       
# words_num = []
# for word in words:
#     temp = ''
#     for w in word:
#         temp += str(word_dict[w])
#     words_num.append(int(temp))

# print(sum(words_num))