def save_txt_file(filename, data, delimeter='|'):
    with open(filename, 'w', encoding='utf-8') as file:
        for i in data:
            for j in range(len(i)):
                if j == len(i)-1:
                    file.write(f'{i[j]}\n')
                else:
                    file.write(f'{i[j]}{delimeter}')

def save_cvs_file(filename, data):
    save_txt_file(filename, data, ',')
