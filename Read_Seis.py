from obspy import read
from obspy.core import UTCDateTime



##read stream
def Read(st):



    return st, len(st)


## access metadata of stream
def Stats(st):

    tr = st[0]

    return tr.stats

def Station(st):

    tr = st[0]

    return tr.stats.station

def Time(st):

    print

