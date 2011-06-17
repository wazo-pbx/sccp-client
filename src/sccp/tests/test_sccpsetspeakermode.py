'''
Created on Jun 14, 2011

@author: lebleu1
'''
import unittest
from sccp.sccpsetspeakermode import SCCPSetSpeakerMode


class TestSccpSetSpeakerMode(unittest.TestCase):


    def testUnPack(self):
        setSpeakerMode = SCCPSetSpeakerMode()
        receivedBuffer = '\x01\x00\x00\x00'
        setSpeakerMode.unPack(receivedBuffer)
        self.assertTrue(setSpeakerMode.speakerOn)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()