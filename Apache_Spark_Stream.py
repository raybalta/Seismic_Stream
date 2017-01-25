from __future__ import print_function

import sys
import os

# Append to PYTHONPATH so that pyspark could be found
sys.path.append("C:/Spark/spark-2.1.0-bin-hadoop2.7/python")
sys.path.append("C:/Spark/spark-2.1.0-bin-hadoop2.7/python/lib")
sys.path.append("C:/Spark/spark-2.1.0-bin-hadoop2.7/python/pyspark")
sys.path.append("C:/Spark/spark-2.1.0-bin-hadoop2.7/python/lib/py4j-0.10.4-src.zip")
##import streaming
try:

    from pyspark import SparkConf
    from pyspark import SparkContext
    from pyspark.streaming import StreamingContext
    #import requests

    #requests.packages.urllib3.disable_warnings()
##check if spark is connected
    print("Start apache sparks")
except ImportError as e:
    print("Error importing Spark Modules", e)
    sys.exit(1)

print ("Hello")

os.environ["SPARK_HOME"] = "C:/Spark/spark-2.1.0-bin-hadoop2.7/"
print ("1")
#conf = (SparkConf().setAppName('NetworkWordCount'))
#print(conf)
#sc = SparkContext(conf=conf)


sc = SparkContext("local[4]", "NetworkWordCount")
#sc = SparkContext(appName="PythonStreamingNetworkWordCount")
ssc = StreamingContext(sc, 1)##connects the sc evey 1 secs
print (" Hello World")
# Create a DStream that will connect to hostname:port, like localhost:9999
lines = ssc.socketTextStream("localhost", 9999)
print ("Not here")
# Split each line into words
words = lines.flatMap(lambda line: line.split(" "))
print ("first")
# Count each word in each batch
pairs = words.map(lambda word: (word, 2))
wordCounts = pairs.reduceByKey(lambda x, y: x + y)
print ("second")
# Print the first ten elements of each RDD generated in this DStream to the console
wordCounts.pprint()
print ("third")

ssc.start()             # Start the computation
print ("fourth")
ssc.awaitTermination()  # Wait for the computation to terminate
print ("end of script")