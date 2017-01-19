from __future__ import print_function
import os
import sys

##path to spark folder
os.environ["SPARK_HOME"] = "C:/Spark/spark-2.1.0-bin-hadoop2.7"
##append pyspark to Python Path
sys.path.append("C:/Spark/spark-2.1.0-bin-hadoop2.7/python/")
sys.path.append("C:/Spark/spark-2.1.0-bin-hadoop2.7/python/lib")
sys.path.append("C:/Spark/spark-2.1.0-bin-hadoop2.7/python/lib/py4j-0.10.4-src.zip")

try:
    from pyspark import SparkContext
    from pyspark import SparkConf

    print ("Successfull imported Spark Modules")

except ImportError as e:
    print ("Error importing Spark Moduls", e)

sc = SparkContext('local')

#words = sc.parallelize(["scala","java","hadoop","spark","akka"])
#print(words.count())
