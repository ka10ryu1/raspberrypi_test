#!/usr/bin/env python
# -*- coding: utf-8 -*-
help = 'HC-SR04を使用して距離を測定する'
#

import time
import serial
import datetime
import numpy as np
import argparse


def command():
    parser = argparse.ArgumentParser(description=help)
    parser.add_argument('-s', '--serial_port',  default='/dev/ttyACM0',
                        help='使用するシリアルポート（$ dmesg | grep ttyACM0）')
    parser.add_argument('-n', '--get_num', type=int, default=20,
                        help='距離を取得する回数 [default: 20times]')
    return parser.parse_args()


def queue(src, a):
    dst = np.roll(src, -1)
    dst[-1] = a
    return dst


def view(data):
    ave = np.average(data)
    sigma = np.std(data)
    sn = 20 * np.log10(ave/sigma)
    print('TIME: {}'.format(datetime.datetime.today()))
    print('DIST(S/N): {0:6.2f}[cm]({1:5.2f}[dB])'.format(data[-1], sn))


def main(args, i=0):
    data = np.zeros(10)
    ser = serial.Serial(args.serial_port, 9600, timeout=1)
    print(ser.portstr)
    time.sleep(2)
    while i != args.get_num:
        line = ser.readline()  # シリアルデータの取得
        line = line.decode()  # byte -> string
        dist = line.rstrip()  # 行終端コード削除
        data = queue(data, float(dist))
        view(data)
        i += 1

    ser.close()
    print('END')


if __name__ == '__main__':
    main(command())
