def generate_diff(file_1, file_2):
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
