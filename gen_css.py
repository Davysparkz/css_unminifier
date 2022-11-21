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
    import sys

    if (len(sys.argv)) == 5 and (sys.argv[1] == '-i') and  (sys.argv[3] == '-o'):
        input_file = sys.argv[2].strip()
        output_file = sys.argv[4].strip()
        if input_file.endswith('.css') and output_file.endswith('.css'):
            transform(input_file, 'gen.css')
            cleanup('gen.css', output_file)
            os.remove('gen.css')
        else:
            print('\n*** USAGE: gen_css.py -i input_file.css -o output_file.css ***\n')
            quit()
    else:
        print('\n*** USAGE: gen_css.py -i input_file.css -o output_file.css ***\n')
