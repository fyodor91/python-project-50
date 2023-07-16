import json


def generate_diff(first_file, second_file):
    file_1 = json.load(open(first_file))
    file_2 = json.load(open(second_file))
    result = []
    set_1 = set((k, v) for k, v in file_1.items())
    set_2 = set((k, v) for k, v in file_2.items())
    for line in sorted(set_1 | set_2, key=lambda x: (x[0], x in set_2)):
        if line in set_1-set_2:
            result.append(f'- {line[0]}:{line[1]}')
        elif line in set_2-set_1:
            result.append(f'+ {line[0]}:{line[1]}')
        else:
            result.append(f'  {line[0]}:{line[1]}')
    return '{\n' + '\n'.join(result) + '\n}'
