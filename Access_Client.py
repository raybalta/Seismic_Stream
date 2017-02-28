from obspy.clients.fdsn import Client
from obspy.clients.fdsn.header import URL_MAPPINGS
from obspy import UTCDateTime
#from mpl_toolkits.basemap import Basemap

def Client_Name(client):

    client = Client(client)

    return client

def URl_Map():
    for key in sorted(URL_MAPPINGS.keys()):
        print("{0:<7} {1}".format(key, URL_MAPPINGS[key]))

def Get_Wavefronts(client,date,SN, Ch, Ch2, timerange, timerange2): ##client is client = ex IRIS date in UTC format, SN is seismic network ie IU, Ch is channel ex ANMO, Ch2 local channel of a channelex LHZ timerange = 60 * 60 duration of stream
    t = UTCDateTime(date)
    st = Client_Name(client).get_waveforms(SN, Ch, "00", Ch2, t, t + timerange* timerange2 )
    st.plot()
    print st

## gets catalog

def Get_Events(start_time, end_time, client, magnitude, catalog):##pass start date and end date client name (IRIS) and catalog, then print the catalog and plot - can get from def URL
    starttime = UTCDateTime(start_time)
    endtime = UTCDateTime(end_time)
    cat = Client_Name(client).get_events(starttime=starttime, endtime=endtime,
                                         minmagnitude= magnitude, catalog= catalog)

    inventory = Client_Name(client).get_stations(network="IU", station="A*",
                                    starttime=starttime,
                                    endtime=endtime)

    print(cat)
    print (inventory)

    #cat.plot()