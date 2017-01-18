
import Channel


def Single_Ch_Plot(st):

    Channel.Channel(st).plot()

## st is data stream, read on main, col is color of graph, time is in seconds
def Pretty_Plot(st, col, ticks, time):
    dt = Channel.Channel(st)[0].stats.starttime
    Channel.Channel(st).plot(color=col, number_of_ticks=ticks,
                             tick_rotation=5, tick_format='%I:%M %p',
                             starttime=dt + 60*60, endtime=dt + 60*60 + time)

    return dt

def Save_file(m, filename):## pass method call- single file or multi file
    Channel.m(outfile = filename.png)

def three_channel_Plot( st1, st2, st3,size):

    Channel.MultiChannel(st1, st2, st3).plot(size=(size))


def Whole_Day_Plot(st):

    Channel.Channel(st).plot(type = 'dayplot')