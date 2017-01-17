from obspy import read ##needed to read stream data
from obspy.core import UTCDateTime

import Read_Seis
import Access_Data


st = read('http://examples.obspy.org/RJOB_061005_072159.ehz.new')

#print Test.Hello()
#print Read_Seis.Read(st)
print Read_Seis.Stats(st)
#print Read_Seis.Station(st)
#print Access_Data.Data(st)
#Access_Data.Plot_data(st)


