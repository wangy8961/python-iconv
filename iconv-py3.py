import argparse
import logging
import sys

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def convert(from_code, to_code, input, output):
    """Convert File Encoding"""
    # 读取源文件
    try:
        f = open(input, 'r', encoding=from_code)
    except FileNotFoundError as e:  # 源文件或它的目录不存在时
        logging.error(e)
        sys.exit(1)

    try:
        content = f.read()  # Python 自动根据 from_code 将接收到的字节序列解码成 str 对象
    except UnicodeDecodeError as e:
        logging.error('Encoding of input is wrong: %s' % e)
        sys.exit(1)
    f.close()

    # 写入目标文件
    try:
        f = open(output, 'w', encoding=to_code)
    except FileNotFoundError as e:  # 目标文件或它的目录不存在时
        logging.error(e)
        sys.exit(1)

    try:
        f.write(content)  # 首先，Python 自动根据 to_code 将 str 对象编码成字节序列，然后再写入目标文件中
    except UnicodeEncodeError as e:
        logging.error('Encoding of output is wrong: %s' % e)
        sys.exit(1)
    f.close()

    logging.info('Convert done.')


if __name__ == '__main__':
    # 解析命令行参数
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f', '--from-code',
        metavar='NAME',
        required=True,
        help='encoding of original text'
    )
    parser.add_argument(
        '-t', '--to-code',
        metavar='NAME',
        required=True,
        help='encoding for output'
    )
    parser.add_argument(
        '-i', '--input',
        metavar='FILE',
        required=True,
        help='input file'
    )
    parser.add_argument(
        '-o', '--output',
        metavar='FILE',
        required=True,
        help='output file'
    )
    parser.add_argument(
        '-v', '--version',
        action='version',
        version='%(prog)s 1.0.0',
    )
    args = parser.parse_args()

    # 调用转换函数
    convert(args.from_code, args.to_code, args.input, args.output)
