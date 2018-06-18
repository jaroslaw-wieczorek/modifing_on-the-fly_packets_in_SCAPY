from scapy.all import *
from netfilterqueue import NetfilterQueue, COPY_PACKET
from scapy.layers.inet import IP, TCP
from scapy.layers.l2 import Ether
from evilpostman.iterface import Window
from evilpostman.pyqt_scapy_item import PyQtScapyTableWidgetItem
import queue
import threading


class Packet_handler(Window):
    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)

    def pkt_hasLayer(self, pkt, layer):
        if pkt.haslayer(layer):
            self.add_row_to_mod_list_packets(pkt)

    def handle_my_packet(self, packet):
        self.add_row_to_cap_list_packets(packet)
        #self.pkt_hasLayer(pkt, TCP)
        return packet