
from scapy.all import *

#TYPE_MYDORAEMON = 0x1212
#TYPE_IPV4 = 0x0800

class MyDoraemon(Packet):
    name = "MyDoraemon"
    fields_desc = [
        IntField("dorayaki", 0) # Start with 0 dorayaki
    ]


bind_layers(TCP, MyDoraemon, dport=1234)
