from obspy import read ##needed to read stream data
from obspy.core import UTCDateTime
from obspy.clients.fdsn import Client


import Read_Seis
import Access_Data
import Channel
import Plotting
import Access_Client

st = read('http://examples.obspy.org/RJOB_061005_072159.ehz.new')
st1 = read('https://examples.obspy.org/COP.BHE.DK.2009.050')
st2 = read('https://examples.obspy.org/COP.BHN.DK.2009.050')
st3 = read('https://examples.obspy.org/COP.BHZ.DK.2009.050')
size = (800,600)

#print Test.Hello()
#print Read_Seis.Read(st)
#print Read_Seis.Stats(st)
#print Read_Seis.Station(st)
#print Access_Data.Data(st)
#Access_Data.Plot_data(st)
#print Channel.Channel(st1)
#print Channel.MultiChannel(st1, st2, st3)
#Channel.Channel(st1).plot() ## plot data coming from a single channel
#Plotting.Pretty_Plot(st2,"blue", 10, 360)## send stream, number of ticks, color and time covered in seconds
#Plotting.three_channel_Plot(st1, st2, st3, size)
#Plotting.Whole_Day_Plot(st1)
#print Access_Client.Client_Name("Iris")
#Access_Client.URl_Map()
Access_Client.Get_Wavefronts("IRIS","2015-02-12","IU","ANMO","LHZ",60, 60)# 60*30 60 secs by 30 min