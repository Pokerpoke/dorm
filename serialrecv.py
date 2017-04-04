#-*- coding:utf-8 -*-
"""
Raspberry Pi serial receive and write to mysql
"""

import time
import serial
import sqlite3
import binascii

SER = serial.Serial('/dev/ttyUSB0', 115200, timeout=0, interCharTimeout=0.001)


class RecevData(object):
    """
    recevData
    """

    def __init__(self):
        self.messageType = 0
        self.devID = 0
        self.devName = 0
        self.devStatus = 0
        self.nRelays = 0
        self.router = 0
        self.data = 0
        self.relay = 0
        self.stop = 0

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
            self.nRelays = data[6]
            self.stop = data[12]
            return True
        elif ((cmp(data[0], "\xf3") == 0) and
              (cmp(data[12], "\xfc") == 0)):
            # Ask for network
            ptr = 0
            # Get the number of relays
            for i in data[7:12]:
                if i != '\xf6':
                    ptr = ptr + 1
            # Send devID + 'FF' to device to comform received
            back = data[1:3] + "FF"
            SER.write(back)
            # Get infomation matched
            self.messageType = binascii.hexlify(data[0])
            self.devID = binascii.hexlify(data[1:3])
            self.devStatus = binascii.hexlify(data[3:6])
            self.relay = binascii.hexlify(data[7:12])
            # calcualte the router
            # replace data[7+ptr] with devID
            self.router = binascii.hexlify(
                data[7:7 + ptr] + data[4] + data[8 + ptr:12])
            if data[3] == '0':
                ansF4Relay(data,ptr)
            else:
                ansF4(data)
            return True
        elif ((cmp(data[0], "\xf5") == 0) and
              (cmp(data[12], "\xfa") == 0)):
            # Reservation
            pass
        else:
            return False


def ansF4Relay(data, ptr):
    """
    Answer \xf4 ... \xfb data to relay
    replace data[7:12] with router
    """
    back = "\xf4" + "FF" + data[3:6] + "\x07" + \
        data[7:7 + ptr] + data[4] + data[8 + ptr:12] + "\xfb"
    print('back:   ',binascii.hexlify(back))
    SER.write(back)
    return True


def ansF4(data):
    back = "\xf4" + "FF" + data[3:6] + "\x07" + data[7:12] + "\xfb"
    SER.write(back)
    return True


def readSerial(serial):
    """
        Read serial and write into mysql
    """
    if SER.inWaiting() < 13:
        return False
    else:
        data = SER.read(13)
        print('receive:',binascii.hexlify(data))
        SER.flushInput()
        rec = RecevData()
        if rec.infoMatch(data) == True:
            conn = sqlite3.connect('db.sqlite3')
            cursor = conn.cursor()
            # cursor.execute("insert into dormdb_dorm (devID,\
            #         devName,devStatus,nRelays,relay1,relay2,\
            #         relay3,relay4,relay5,time)\
            #         values (", rec.devID, ",", rec.devName, ",", rec.devStatus,
            #                ",", rec.distance, ",", rec.relay1, ",", rec.relay2,
            #                ",", rec.relay3, ",", rec.relay4, ",", rec.relay5,
            #                ", datetime('now','localtime'))")
            cursor.execute("insert into dormdb_dorm (devID,\
                    devStatus,nRelays,relay,time)\
                    values ('" + str(rec.devID) +
                           "','" + str(rec.devStatus) +
                           "','" + str(rec.nRelays) +
                           "','" + str(rec.relay) +
                           "',datetime('now','localtime'))")
            cursor.close()
            conn.commit()
            conn.close()
            return rec
        else:
            return False


if __name__ == '__main__':
    while True:
        readSerial(SER)
        time.sleep(0.0001)
