import obspy.clients.seedlink
from obspy.clients.seedlink import EasySeedLinkClient
from obspy.clients.fdsn import Client
from obspy.clients.seedlink.easyseedlink import create_client
import Access_Client
from obspy.core import read
from obspy.realtime import RtTrace as tr
import Access_Data




def handle_data(trace):
   print('Received the following trace:')
   print(trace)
   print trace.data
   #print()
   stream = read(trace)
   stream.write('outfile.ascii', format= 'SLIST')


   #trace.spectrogram(log=True)

   #trace.plot()



#client = create_client('rtserve.iris.washington.edu:18000/#IU_ANMO:BH?', on_data=handle_data)

#print client.get_info('ID')
#print client.capabilities

##stream data from the server

#client.select_stream('IU', 'ANMO', 'BH?')

#client.run()

def New_Client(cl, cl1, cl2, cl3):
   client = create_client(cl, on_data=handle_data)
   client.select_stream(cl1, cl2, cl3)

   client.run()
