
# Compilation of P4 programs and running mininet in the P4 VM

If you've followed the first [note](./1_jmt_vagrant_setup.md), then you should have the `/vagrant/` directory mounted inside the VM. Change directory into the 'basic' tutorial:

~~~
$ cd /vagrant/exercises/basic/
~~~

It is essentially [this](./exercises/basic/) directory.

There is a `README.md` and a `Makefile` here which handles the compilation of the P4 program and running mininet. It references a master Makefile at `../../utils/Makefile`, so look inside here if you want to know the details.  But basically, it compiles the P4 program and runs mininet when you do:

~~~
 $ sudo make run
~~~

and if you observe the outputted logs you see some interesting steps:

1.  'p4c-bm2-ss': This is the P4 compiler for the bmv2 software 
switch.  You will see a few compile warnings saying 'dstAddr' is 
unused etc.  This is because the "basic.p4" in the current directory
has code stumps, and the solution is in the 'solutions/' directory.

2.  `sudo python3 ../../utils/run_exercise.py`: This python script
defines the mininet run.

3.  To stop mininet and exit the BMV2 Mininet CLI do:

~~~
$ sudo make stop
$ sudo make clean
~~~



# Wireshark

You can run Wireshark packet capture within the VM. In the terminal do:

~~~
$ sudo wireshark
~~~

Each of the switches `sX` in mininet will be a NIC in wireshark's 
interface list.










Tutorial slides:
https://docs.google.com/presentation/d/1zliBqsS8IOD4nQUboRRmF_19poeLLDLadD5zLzrTkVc/edit#slide=id.g37fca2850e_6_2090

Useful blog:
https://opennetworking.org/news-and-events/blog/getting-started-with-p4/

