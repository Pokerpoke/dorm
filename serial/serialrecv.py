#-*- coding:utf-8 -*-
"""
Raspberry Pi serial receive and write to mysql
"""

import time
import serial
import sqlite3

SER = serial.Serial('/dev/ttyUSB0', 115200, timeout=0, interCharTimeout=0.001)


class RecevData(object):
    """
    recevData
    """

    def __init__(self):
        #              messageType, devID, distance, data,
        #              relay1, relay2, relay3, relay4, relay5):
        self.messageType = 0
        self.devID = 0
        self.distance = 0
        self.data = 0
        self.relay1 = 0
        self.relay2 = 0
        self.relay3 = 0
        self.relay4 = 0
        self.relay5 = 0

    def infoMatch(self, data):
        """
        Match infomation from receive message.

        Data Format:
        information type : 1 Byte (data[0])
        device ID : 2 Byte (data[1:3])
        reservation : 3 Byte (data[3:6])
        distance from terminal : 1 Byte (data[6])
        relay1 ~ relay5 : 1 Byte (data[7] ~ data[11])
        stop : 1 Byte (data[12])
        """
        if ((cmp(data[0], "\xf1") == 0) and
                (cmp(data[12], "\xfe") == 0)):
            # Upstream data
            back = data[1:3] + "FF"
            SER.write(back)
            self.messageType = data[0]
            self.devID = data[1:3]
            self.data = data[3:6]
            self.distance = data[6]
            self.relay1 = data[7]
            self.relay2 = data[8]
            self.relay3 = data[9]
            self.relay4 = data[10]
            self.relay5 = data[11]
            stop = data[12]
            return True
        elif ((cmp(data[0], "\xf3") == 0) and
              (cmp(data[12], "\xfc") == 0)):
            # Ask for network
            back = data[1:3] + "FF"
            SER.write(back)
# TODO(pokerpoke): 7,pointer
            self.messageType = data[0]
            self.devID = data[1:3]
            self.distance = data[6]
            self.relay1 = data[7]
            self.relay2 = data[8]
            self.relay3 = data[9]
            self.relay4 = data[10]
            self.relay5 = data[11]
            stop = data[12]
            return True
        elif ((cmp(data[0], "\xf5") == 0) and
              (cmp(data[12], "\xfa") == 0)):
            # Reservation
            pass
        else:
            return False


def readSerial(serial):
    """
        Read serial and write into mysql
    """
    if SER.inWaiting() < 13:
        return False
    else:
        data = SER.read(13)
        rec = RecevData()
        if rec.infoMatch(data) == True:
            print("distance: " + rec.distance)
            print("dev: " + rec.devID)
            conn = sqlite3.connect('dorm.db')
            return rec
        else:
            return False


if __name__ == '__main__':
    while True:
        readSerial(SER)
        time.sleep(0.0001)
