#!python3
import argparse
import csv
import sys

base_dir = './'


def argsParser():
    parser = argparse.ArgumentParser(description='提取 csv 中的某一列。')
    parser.add_argument('-i', '--input-file', type=str, help='csv file')
    parser.add_argument('-c', '--column', type=int, help='the column, from index 0')

    args = parser.parse_args()
    if args.input_file == None:
        parser.print_help()
        sys.exit()
    else:
        return args


def colGather(csvfile, column):
    '''
    从列表中提取出某一列，保存为列表
    '''
    with open(csvfile) as f:
        reader = csv.reader(f)
        target_list = [row[int(column)] for row in reader][1:]
        return target_list


def str2file(filename, content):
    '''
    提取出的列表保存到文件
    '''
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)


def main():
    args = argsParser()
    csvfile = base_dir+args.input_file
    column = args.column
    content_list = colGather(csvfile, column)
    content_str = '\n'.join(content_list)
    dest_file = csvfile.replace(csvfile.strip().split('.')[-1:][0], 'txt')
    print(dest_file)
    str2file(dest_file, content_str)


if __name__ == '__main__':
    main()
