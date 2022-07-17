#!/bin/bash

#-p  is protocol selection between QUIC and TCP
#-l  defines packet loss in %, it is given within range in comparison.py
#-d  define delay in ms
#-b  bandwidth in mbps

python comparison.py -p QUIC TCP -l 5.0 -d 50  -b 100 --vverbose
python comparison.py -p QUIC TCP -l 5.0 -d 50  -b 40 --vverbose
python comparison.py -p QUIC TCP -l 5.0 -d 50  -b 5 --vverbose

python comparison.py -p QUIC TCP -l 0.0 -d 10  -b 100 -s 1 --vverbose
python comparison.py -p QUIC TCP -l 0.0 -d 10  -b 40 -s 1 --vverbose
python comparison.py -p QUIC TCP -l 0.0 -d 10  -b 5 -s 1 --vverbose

python comparison.py -p QUIC TCP -l 5.0 -d 10  -b 100 -s 1 --vverbose
python comparison.py -p QUIC TCP -l 5.0 -d 10  -b 40 -s 1 --vverbose
python comparison.py -p QUIC TCP -l 5.0 -d 10  -b 5 -s 1 --vverbose

python comparison.py -p QUIC TCP -l 0.0 -d 50  -b 100 -s 1 --vverbose
python comparison.py -p QUIC TCP -l 0.0 -d 50  -b 40 -s 1 --vverbose
python comparison.py -p QUIC TCP -l 0.0 -d 50  -b 5 -s 1 --vverbose

python comparison.py -p QUIC TCP -l 5.0 -d 50  -b 100 -s 1 --vverbose
python comparison.py -p QUIC TCP -l 5.0 -d 50  -b 40 -s 1 --vverbose
python comparison.py -p QUIC TCP -l 5.0 -d 50  -b 5 -s 1 --vverbose
