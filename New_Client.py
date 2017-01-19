import obspy.clients.seedlink
from obspy.clients.seedlink import EasySeedLinkClient
#from obspy.clients.fdsn import Client
from obspy.clients.seedlink.easyseedlink import create_client
import Access_Client




def handle_data(trace):
   print('Received the following trace:')
   print(trace)
   print()

client = create_client('rtserve.iris.washington.edu:18000/#IU_ANMO:BH?', on_data=handle_data)

print client.get_info('ID')
print client.capabilities

##stream data from the server

client.select_stream('IU', 'ANMO', 'BH?')

client.run()