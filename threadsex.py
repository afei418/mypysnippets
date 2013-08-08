#!/usr/bin/env python

import threading, zipfile

class AsynZip(threading.Thread):
    def __init__(self, infs, outfs):
        threading.Thread.__init__(self)
        self.infile = infs
        self.outfile = outfs
    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print("Finished background zip of: %s" % self.infile)

bg = AsynZip('mydata.txt', 'mydata.zip')
bg.start()

print('The main program continues to run in frontground')

bg.join()
print('Main program waited until background task to finish')
