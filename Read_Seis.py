from obspy import read



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

