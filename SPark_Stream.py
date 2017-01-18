from __future__ import print_function

import sys
import os

# Append to PYTHONPATH so that pyspark could be found
sys.path.append("C:/Spark/spark-2.1.0-bin-hadoop2.7/python")
sys.path.append("C:/Spark/spark-2.1.0-bin-hadoop2.7/python/lib")
sys.path.append("C:/Spark/spark-2.1.0-bin-hadoop2.7/python/lib/py4j-0.10.4-src.zip")
##import streaming
try:
    #from pyspark import SparkContext
    from pyspark import SparkConf
    from pyspark import SparkContext
    from pyspark.streaming import StreamingContext
    import requests

    requests.packages.urllib3.disable_warnings()
##check if spark is connected
    print("Start apache sparks")
except ImportError as e:
    print("Error importing Spark Modules", e)
    sys.exit(1)

print ("Hello")

os.environ["SPARK_HOME"] = "C:/Spark/spark-2.1.0-bin-hadoop2.7/"


sc = SparkContext("local[4]", "NetworkWordCount")
ssc = StreamingContext(sc, 1)

lines = ssc.socketTextStream("localhost", 9999)
counts = lines.flatMap(lambda line: line.split(" "))\
                  .map(lambda word: (word, 1))\
                  .reduceByKey(lambda a, b: a+b)
counts.pprint()
ssc.start()
ssc.awaitTermination()
