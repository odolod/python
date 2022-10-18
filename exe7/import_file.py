def load_txt_file(filename, delimeter='|'):
    with open(filename, 'r', encoding='utf-8') as file:
        return list(map(lambda x: x.strip().split(delimeter),file))

def load_cvs_file(filename):
    return load_txt_file(filename, ',')

