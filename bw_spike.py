#!/usr/bin/python
import os
import os.path
import time


netemBwChange = "sudo tc qdisc change dev lo parent 1: handle 2: tbf rate xxxmbit burst 256kbit latency 1000ms mtu 1500"
spikeDrop = 0.1


def Bandwidth_spike(params):
    if params.bandwidth:
        netemBWReduce = netemBwChange.replace(
            "xxx", str(params.bandwidth * spikeDrop))

    BwRestore = netemBwChange.replace(
        "xxx", str(params.bandwidth))

    time.sleep(params.spikedelay)

    os.system(netemBWReduce)
    params.spikestart = startTime = time.time()

    print("Spike started:")
    print(netemBWReduce)

    time.sleep(2)
    os.system(BwRestore)
    elapsedTime = time.time() - startTime

    print("Spike ended (duration: " + str(elapsedTime) + ", spikestart=" + str(params.spikestart) + ") :")
    print(BwRestore)