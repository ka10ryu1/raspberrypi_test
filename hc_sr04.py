#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import serial
import datetime
import numpy as np

def queue(src, a):
    dst = np.roll(src, -1)
    dst[-1] = a
    return dst

def console_print(data):
    ave = np.average(data)
    sigma = np.std(data)
    sn = 20 * np.log10(ave/sigma)
    print('TIME: {}'.format(datetime.datetime.today()))
    print('DIST(S/N): {0:6.2f}[cm]({1:5.2f}[dB])'.format(data[-1], sn))

def main():
    i = 0
    data = np.zeros(10)
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    print(ser.portstr)
    time.sleep(3)
    while i != 20:
        line = ser.readline()
        line = line.decode()
        dist = line.rstrip()
        data = queue(data, float(dist))
        console_print(data)
        i += 1

    ser.close()
    print('END')

if __name__ == '__main__':
    main()
