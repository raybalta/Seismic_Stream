from obspy.core import read

## access server and reac batch files rather than save streamed files
stream = read('https://examples.obspy.org/RJOB20090824.ehz')
stream.write('Putfile.csv', format='TSPAIR')