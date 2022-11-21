def transform(in_f, out_f):
    with(open(out_f, 'w')) as fw:
        with(open(in_f, 'r')) as f:
            lines = f.readlines()
            for line in lines:
                for i in range(len(line)):
                    if line[i] == '}':
                        if ((i-1) > 0):
                            if line[i-1] != ';':
                                fw.write(';\n}\n\n')
                            else:
                                fw.write('\n}\n')
                    elif line[i] == '{':
                        fw.write('\n{\n\t')
                    elif line[i] == ';':
                        fw.write(';\n\t')
                    elif line[i] == ',':
                        fw.write(', ')
                    else:
                        fw.write(line[i])

def cleanup(in_f, out_f):
    with(open(out_f, 'w')) as fw:
        with(open(in_f, 'r')) as fr:
                lines = fr.readlines()
                for line in lines:
                    for i in range(len(line)):
                        if line[0] == ';':
                            fw.write('')
                        else:
                            fw.write(line[i])


if __name__ == '__main__':
    import os
    transform('boa_2.css', 'gen.css')
    cleanup('gen.css', 'boa_2.css')
    os.remove('gen.css')
