from obspy.clients.seedlink.easyseedlink import create_client
from obspy import read
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

#print style.available


def handle_data(trace):
   print('Received the following trace:')
   print (trace)

   return trace
client = create_client('rtserve.iris.washington.edu:18000/#IU_ANMO:BH?', on_data=handle_data)

print client.get_info('ID')
print client.capabilities

##stream data from the server

client.select_stream('IU', 'ANMO', 'BH?')

client.run()

style.use('classic')
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    #graph_data = open("C:\Users\Owner-Pc\Documents\iris\samplefile.txt", "r").read()
    graph_data = read(handle_data())
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(x)
            ys.append(y)

    ax1.clear()
    ax1.plot(xs, ys)

ani = animation.FuncAnimation(fig, animate, interval=1000)

plt.show()




