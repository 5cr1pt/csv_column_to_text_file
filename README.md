# csv_column_to_text_file

提取 csv 文件中的特定列，保存到 txt 文件。

![](https://shields.io/badge/license-GPL-blue)![](https://img.shields.io/badge/Python-3.6%2B-blue)

## Quick Start

```bash
$ python3 column2txt.py -h
usage: column2txt.py [-h] [-i INPUT_FILE] [-c COLUMN]

提取 csv 中的某一列。

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_FILE, --input-file INPUT_FILE
                        csv file
  -c COLUMN, --column COLUMN
                        the column, from index 0
$ python3 column2txt.py -i example.csv -c 0
$ ls
LICENSE       README.md     column2txt.py example.csv   example.txt

```