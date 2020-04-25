#-*-coding:utf-8-*-

"""
DGIST ARTIV LAB
IONIQ Vehicle - CAN Communication Tool.

Target devide : Kvaser Leaf Light
Author : Gwanjun Shin, Hoyeong Hoyeong

Using CAN database format *dbc file to match frame
"""

import argparse
import os
from canlib import canlib, kvadblib


bitrates = {
    '1M': canlib.canBITRATE_1M,
    '500K': canlib.canBITRATE_500K,
    '250K': canlib.canBITRATE_250K,
    '125K': canlib.canBITRATE_125K,
    '100K': canlib.canBITRATE_100K,
    '62K': canlib.canBITRATE_62K,
    '50K': canlib.canBITRATE_50K,
    '83K': canlib.canBITRATE_83K,
    '10K': canlib.canBITRATE_10K,
}



def printframe(db, frame):
    try:
        bmsg = db.interpret(frame)
    except kvadblib.KvdNoMessage:
        #print("<<< No message found for frame with id %s >>>" % frame.id)
        return
        pass

    if not (frame.id == 82 ):#or frame.id == 82): # or frame.id == 84):
        #print("Rogue data !!!!!", frame.id)
        return

    os.system('cls' if os.name == 'nt' else 'clear')


    msg = bmsg._message



    print(msg.name)

    if msg.comment:
        print(msg.comment)

    for bsig in bmsg:
        print(bsig.name + ':', bsig.value, bsig.unit)

    data += bsig.name + ':', bsig.value, bsig.unit + '\n'

    #print('┗')

class capsule:
    def __init__(self):
        dataCapsule = {}
        import pprint

    def manual_update(self, key, value):
        dataCapsule.update({key, value})

    def db_update(self, db, frame):
        try:
            bmsg = db.interpret(frame)
        except kvadblib.KvdNoMessage:
            #print("<<< No message found for frame with id %s >>>" % frame.id)
            return
        for signal in bmsg:
            self.manual_update(signal.name, signal.value)


    def pprint(self):
        pprint.pprint(dataCapsule)

    def __str__(self):
        return pprint.pfromat(dataCapsule)
    def __repr__(self):
        return pprint.pfromat(dataCapsule)


def monitor_channel(channel_number, db_name, bitrate, ticktime):
    db = kvadblib.Dbc(filename=db_name)
    dbCap = capsule()
    ch = canlib.openChannel(channel_number, canlib.canOPEN_ACCEPT_VIRTUAL)
    ch.setBusOutputControl(canlib.canDRIVER_NORMAL)
    ch.setBusParams(bitrate)
    ch.busOn()

    timeout = 0.5
    tick_countup = 0
    if ticktime <= 0:
        ticktime = None
    elif ticktime < timeout:
        timeout = ticktime

    print("Listening...")
    while True:
        try:

            frame = ch.read(timeout=int(timeout * 1000))
            #printframe(db, frame)
            dbCap.db_update(db, frame)
            dbcap.pprint()
        except canlib.CanNoMsg:
            if ticktime is not None:
                tick_countup += timeout
                while tick_countup > ticktime:
                    print("tick")
                    tick_countup -= ticktime
        except KeyboardInterrupt:
            print("Stop.")
            break
        except Exception:
            pass



if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Listen on a CAN channel and print all signals received, as specified by a database.")
    parser.add_argument('--channel', type=int, default=0, nargs='?', help=(
        "The channel to listen on."))
    parser.add_argument('--db', default="cankingDB_ioniq_dgist_mod.dbc", help=(
        "The database file to look up messages and signals in."))
    parser.add_argument('--bitrate', '-b', default='500K', help=(
        "Bitrate, one of " + ', '.join(bitrates.keys())))
    parser.add_argument('--ticktime', '-t', type=float, default=0, help=(
        "If greater than zero, display 'tick' every this many seconds"))
    args = parser.parse_args()

    monitor_channel(args.channel, args.db, bitrates[args.bitrate.upper()], args.ticktime)
