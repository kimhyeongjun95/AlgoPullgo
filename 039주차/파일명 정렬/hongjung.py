def solution(files):
    files_list = []
    for i in range(len(files)):
        if '.' in files[i]:
            temp1, temp2 = files[i].split('.')
            int_start = 0
            int_end = -1
            is_int = False
            for j in range(len(temp1)):
                if is_int == False and temp1[j].isdigit():
                    int_start = j
                    is_int = True
                elif is_int and temp1[j].isdigit() == False:
                    int_end = j - 1
                    break
            if int_end == -1 and is_int:
                int_end = len(temp1) - 1
            temp1_head = temp1[:int_start].lower()
            temp1_int = int(temp1[int_start:int_end+1])
            files_list.append([temp1_head, temp1_int, i, files[i]])
        else:
            int_start = 0
            int_end = -1
            is_int = False
            for j in range(len(files[i])):
                if is_int == False and files[i][j].isdigit():
                    int_start = j
                    is_int = True
                elif is_int and files[i][j].isdigit() == False:
                    int_end = j - 1
                    break
            if int_end == -1 and is_int:
                int_end = len(files[i]) - 1
            file_head = files[i][:int_start].lower()
            file_int = int(files[i][int_start:int_end+1])
            files_list.append([file_head, file_int, i, files[i]])

    for i in range(len(files_list) - 1):
        for j in range(i + 1, len(files_list)):
            file_i_head = files_list[i][0]
            file_i_num = files_list[i][1]
            file_i_origin_idx = files_list[i][2]
            file_j_head = files_list[j][0]
            file_j_num = files_list[j][1]
            file_j_origin_idx = files_list[j][2]
            if file_i_head == file_j_head:
                if file_i_num > file_j_num:
                    files_list[i], files_list[j] = files_list[j], files_list[i]
                elif file_i_origin_idx > file_j_origin_idx:
                    files_list[i], files_list[j] = files_list[j], files_list[i]
            else:
                temp_list1 = [file_i_head, file_j_head]
                temp_list2 = sorted(temp_list1)
                if temp_list1 != temp_list2:
                    files_list[i], files_list[j] = files_list[j], files_list[i]

    answer = []                
    for file in files_list:
        answer.append(file[-1])
    return answer

print(solution(["img01.png", "IMG01.png"]))
print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG", "img000.JPG"]))
print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))