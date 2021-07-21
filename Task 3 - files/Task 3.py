import os

path = os.getcwd()
files = ("1.txt", "2.txt", "3.txt")

with open('final_file', 'w', encoding='utf-8') as final_file:
    dict_of_files = {}
    dict_of_lens = {}

    for file_name in files:
        file = open(f"{path}\{file_name}", 'r', encoding='utf-8')
        dict_of_files[file_name] = file.readlines()
        len_of_lines = len(dict_of_files[file_name])
        if len_of_lines in dict_of_lens.keys():
            dict_of_lens[len_of_lines].append(file_name)
        else:
            dict_of_lens[len_of_lines] = [file_name]
        file.close()

    for len_of_lines in sorted(dict_of_lens.keys(), reverse=False):
        for file_name in dict_of_lens[len_of_lines]:
            final_file.write('\n' + file_name + '\n')
            final_file.write(str(len_of_lines)+'\n')
            for line in dict_of_files[file_name]:
                final_file.write(line)
