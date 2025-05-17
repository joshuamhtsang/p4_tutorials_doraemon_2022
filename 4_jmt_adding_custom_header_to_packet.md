# Adding a custom header to a packet and modifying its value with an action (Doramon and Dorayaki!)

The approach here is to:

1. Add a custom header called `doraemon` with a field called `dorayaki` to the packet creator script [send.py](./exercises/basic/send.py), which uses the Python library `scapy` to create network packets.

2. Add an action to the P4 file, which tells the switch to modify the value 
of the 'dorayaki' field.

The work here takes place in a modified version of the `basic` exercise, here in this directory: [basic_jmt_expt/](./exercises/basic_jmt_expt/)
Make sure you're in the above directory inside the VM when running the commands below.

## Understand `send.py` and xterms in mininet

The README.md (which one???) explains how to use xterm in mininet to get terminals on the hosts in the mininet network.  In short, to get terminals up for h1 and h3 do:

~~~
> xterm h1 h3
~~~

First we spin up a receiver in `h3`.  In `h3`'s xterm:

~~~
$ python3 receiver.py
~~~

We can then use `send.py` to send a packet from `h1` to `h3`.  In `h1`'s xterm:

~~~
$ python3 send.py 10.0.3.3 "hello"
~~~

You can look inside `pod-topo/pod-topo.png` to see the IP addresses for each host in this demo topology.


## Create the network packet with a new Doraemon layer

The pertinent files are:

1. [myDoraemon_header.py](./exercises/basic_jmt_expt/myDoraemon_header.py): This file defines the Doraemon layer of the packet with the integer dorayaki value.  Uses the `scapy` `Packet` class.
2. [send.py](./exercises/basic_jmt_expt/send.py): This creates the actual packets with the Doraemon layer stacked after the TCP layer (OSI layer 4) and before the payload.  It uses `scapy`'s convenient `/` operator to build and order the layers.


## Modifying the match-actions to increment the dorayaki counter by +1 when ingressed

The pertient file is [basic.p4](./exercises/basic_jmt_expt/basic.p4). There are a few basic sections to the p4 files and each requires modification  to process the doraemon layer:

1. Define the expected headers in the received packet:  Add the `myDoraemon` layer definition and the expected fields in this layer i.e. `bit<32> dorayaki` to the header of the packet.

2. Parse the `myDoraemon` headers:  This means the parser finite state machine should parse the `myDoraemon` header after the TCP layer, and before `accept`.

3. Increment the `dorayaki` counter in the Ingress chain: 

~~~
action ipv4_forward(macAddr_t dstAddr, egressSpec_t port) {
    standard_metadata.egress_spec = port;
    hdr.ethernet.srcAddr = hdr.ethernet.dstAddr;
    hdr.ethernet.dstAddr = dstAddr;
    hdr.ipv4.ttl = hdr.ipv4.ttl - 1;
    hdr.myDoraemon.dorayaki = hdr.myDoraemon.dorayaki + 1;
}
~~~

This section of code is very illustrative of what a conventional switch does before it forwards a packet out of a port.  

Firstly: the ethernet mac layer `hdr.ethernet.srcAddr` must now become the present switch's address i.e. whatever the incoming packet has under `hdr.ethernet.dstAddr`.

Secondly: the outgoing packet must have the destination mac address as that contained in the macAddr to port number table.

Thirdly, the time-to-live (ttl) must be decremented.

Lastly, increment our dorayaki counter (not part of conventional switch operation!)

## Running the demonstration

BLAH



