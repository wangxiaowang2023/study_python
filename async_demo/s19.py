# -*- coding: utf-8 -*-


import time

def download_file(url=None):
    print(f"下载图片={url}")
    time.sleep(1)
    print(f"下载完成={url}")


def main():
    for i in range(1,11):
        download_file(i)



main()