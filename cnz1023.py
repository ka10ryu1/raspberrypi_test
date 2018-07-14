#!/usr/bin/env python
# -*- coding: utf-8 -*-
help = 'CNZ1023を使用してXXを測定する'
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
    parser.add_argument('-n', '--get_num', type=int, default=100,
                        help='を取得する回数 [default: 100times]')
    return parser.parse_args()


def str2list(data):
    return [1 if i == '1' else 0 for i in data[1:]]

def main(args, i=0):
    ser = serial.Serial(args.serial_port, 9600, timeout=1)
    print('serial port: {}'.format(ser.portstr))
    time.sleep(3)
    while i != args.get_num:
        line = ser.read(4)  # シリアルデータの取得
        val = line.decode()
        if(len(val) < 1):
             time.sleep(1)
             continue

        if(val[0] == '5'):
            print(str2list(val))
        else:
            time.sleep(1)

        i += 1
        #time.sleep(1)

    ser.close()
    print('END')


if __name__ == '__main__':
    main(command())
