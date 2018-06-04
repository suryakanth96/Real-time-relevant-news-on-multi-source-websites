# Real-time-relevant-news-on-multi-source-websites
A big data project to obtain real time relevant news from multiple websites.

Computing Framework- Apache Spark
Language- Python
API- PySpark

The project involves the following steps:-

1.Web Scraping
===============
Scraping of real time news from multiple sources related to a specific topic.

2.Spark Streaming
==================
The real time news scraped from multiple websites in the previous step is passed to spark streaming via TCP sockets. Spark streaming reads in the live data as discretized streams(DStreams).

3.Filtering
===========
Spark Streaming filters out the input DStreams using transformation functions filter() and union() to obtain the relevant news.

To run
======
1.Run news.py in a terminal using
python news.py {topic} | nc -lk 9999

2.Run streaming.py in another terminal using 
spark-submit streaming.py | cat > {filename}

Note: cat > {filename} is used to store the results in a file.

eg: python news.py kerala | nc -lk 9999 in one terminal

    spark-submit streaming.py | cat > file.txt in another terminal
    
The filtering keywords can be changed in streaming.py
