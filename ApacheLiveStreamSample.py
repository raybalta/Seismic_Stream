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
    from pyspark.sql import SparkSession
    from pyspark.sql.functions import explode
    from pyspark.sql.functions import split
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


spark = SparkSession \
    .builder \
    .appName("StructuredNetworkWordCount") \
    .getOrCreate()



# Create DataFrame representing the stream of input lines from connection to localhost:9999
lines = spark \
    .readStream \
    .format("socket") \
    .option("host", "localhost") \
    .option("port", 9999) \
    .load()


print ("Not here")


# Split the lines into words
words = lines.select(
   explode(
       split(lines.value, " ")
   ).alias("word")
)

print ("first")

# Generate running word count
wordCounts = words.groupBy("word").count()

# Print the first ten elements of each RDD generated in this DStream to the console

query = wordCounts \
    .writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

query.awaitTermination()
#

#ssc.awaitTermination()  # Wait for the computation to terminate
print ("end of script")



