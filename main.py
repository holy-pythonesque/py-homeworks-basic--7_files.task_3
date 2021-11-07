filenames = ['1.txt', '2.txt', '3.txt']


def get_lines_num(file_info):
    return file_info['lines_num']

files_info = []
for filename in filenames:
    with open(filename, 'r') as file:
        lines = file.readlines()
        files_info.append({
            'name': filename,
            'lines': lines,
            'lines_num': len(lines)
        })

sorted_files_info = sorted(files_info, key=get_lines_num)

for file_info in sorted_files_info:
    print(file_info['name'])
    print(file_info['lines_num'])
    for line in file_info['lines']:
        print(line.strip())