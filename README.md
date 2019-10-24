# python-iconv

Convert file encoding with python 2 or python 3

```bash
[root@CentOS ~]# python iconv-py2.py -f gbk -t utf-8 -i gbk.txt -o a.txt
2019-10-24 22:00:48,712 - root - INFO - Convert done.

[root@CentOS ~]# python3 iconv-py3.py -f gbk -t utf-8 -i gbk.txt -o a.txt
2019-10-24 22:00:18,076 - root - INFO - Convert done.
```

- [Unicode 字符集与 UTF-8 编码系统](https://madmalls.com/blog/post/unicode-and-utf8/)
- [Python 陷阱｜第1章：字符编码问题](https://madmalls.com/blog/post/encoding-in-python/)