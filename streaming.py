from pyspark import SparkContext
from pyspark.streaming import StreamingContext
import sys

# Create a local StreamingContext with two working thread and batch interval of 1 second
sc = SparkContext("local[2]", "News")
ssc = StreamingContext(sc, 2)
# Create a DStream that will connect to hostname:port, like localhost:9999
lines = ssc.socketTextStream("localhost", 9999)

#errors = lines.filter(lambda l: "water" in l.lower())
line1 = lines.filter(lambda l: "hartal" in l.lower()) 
line2 = lines.filter(lambda l: "strike" in l.lower())
line3 = lines.filter(lambda l: "shooting" in l.lower()) 
line4 = lines.filter(lambda l: "attack" in l.lower())
line5 = lines.filter(lambda l: "terrorist" in l.lower())
line6 = line5.union(line4.union(line3.union(line1.union(line2))))
line6.pprint(15)


ssc.start()             # Start the computation
ssc.awaitTermination()  # Wait for the computation to terminate



