
import obspy.clients.seedlink

def handle_data(trace):
    print('Received the following trace:')
    print(trace)
    print()


def Create_Client():
    client = create_client('geofon.gfz-potsdam.de', on_data=handle_data)