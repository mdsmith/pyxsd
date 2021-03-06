from transform import Transform
from pyxsd.writers.xmlTreeWriter import XmlTreeWriter
import sys, tempfile

"""

============================
Transform Library: Displayer
============================

:Author: Karl Norby <knorby@uchicago.edu>
:Date: Fri, 1 Sept 2006
:Category: Computational Materials Science
:Description: Library containing functions to help print data
:Copyright: pyXSD License

"""

class Displayer(Transform):

    #============================================================
    #
    def openFile(self, fileName=None): #uses stdout if filename is None
        if fileName == None or fileName == 'stdout':
            return sys.stdout
        return open(fileName, 'w')

    #============================================================
    #
    def writeTree(self, file):
        XmlTreeWriter(self.root, file)

    #============================================================
    #
    def makeTempFileOfTree(self):
        newTree = tempfile.TemporaryFile()
        self.writeTree(newTree)
        return newTree
    