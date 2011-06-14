'''
Created on Jun 14, 2011

@author: lebleu1
'''

from struct import unpack
from sccp.sccpmessagetype import SCCPMessageType
from sccp.sccpregisterack import SCCPRegisterAck
from sccp.sccpmessage import SCCPMessage

class MessageFactory():
    '''
    sccp message factory create message from received buffer
    '''


    def __init__(self):
        '''
        '''
    def create(self,buffer):
        messageType = unpack("L",buffer[4:8])[0]
        msg = SCCPMessage(messageType)
        if (messageType == SCCPMessageType.RegisterAckMessage):
            msg = SCCPRegisterAck()
        return msg