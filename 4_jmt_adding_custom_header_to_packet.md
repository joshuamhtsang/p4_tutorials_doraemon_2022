# Adding a custom header to a packet and modifying its value with an action (Doramon and Dorayaki!)

The approach here is to:

1. Add a custom header called `doraemon` with a field called `dorayaki` to the packet creator script [send.py](./exercises/basic/send.py), which uses the Python library `scapy` to create network packets.

2. Add an action to the P4 file, which tells the switch to modify the value 
of the 'dorayaki' field.

The work here takes place in a modified version of the `basic` exercise, here in this directory: [basic_jmt_expt/](./exercises/basic_jmt_expt/)
Make sure you're in the above directory inside the VM when running the commands below.

# Understand `send.py` and xterms in mininet

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


# Create the network packet

# Adding a 'doraemon' layer to a scapy packet with field 'dorayaki' 

Done.



