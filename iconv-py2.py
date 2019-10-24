# -*- coding: utf-8 -*-
import argparse
import logging
import sys

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def convert(from_code, to_code, input, output):
    """Convert File Encoding"""
    # 读取源文件
    try:
        f = open(input, 'rb')
    except IOError as e:  # 源文件或它的目录不存在时
        logging.error(e)
        sys.exit(1)
    content_bytes = f.read()  # 接收字节序列

    try:
        content_unicode = unicode(content_bytes, encoding=from_code)  # 按 from_code 解码成 Unicode code points
    except UnicodeDecodeError as e:
        logging.error('Encoding of input is wrong: %s' % e)
        sys.exit(1)
    f.close()

    # 写入目标文件
    try:
        f = open(output, 'wb')
    except IOError as e:  # 目标文件或它的目录不存在时
        logging.error(e)
        sys.exit(1)

    try:
        f.write(content_unicode.encode(to_code))  # 写入按 to_code 编码后的字节序列
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
