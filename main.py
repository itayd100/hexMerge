'''
    File name: main.py
    Author: Itay Dagan
    Date created: 06/01/2019
    Python Version: 3.7
'''


import kivy
kivy.require("1.10.0")

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
import os

class mergehexGridLayout(GridLayout):

    # Function called when equals is pressed
    def calculate(self, calculation):
        if calculation:
            try:
                # Solve formula and display it in entry
                # which is pointed at by display
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "Error"

    '''
    def open(self, path, filename):
        #with open(os.path.join(path, filename[0])) as f:
        #    print (f.read())
        try:
            #print (path)
            print (filename[0])
        except:
            pass
    '''

    def selected(self, filename):
        print ("selected: %s" % filename[0])

    def selectBoot(self, path, filename):
        print ("select boot")
        try:
            print (filename[0])
            filenameBoot = filename[0]
            print ("chose bootloader")
        except:
            pass

    def selectApp(self, path, filename):
        print ("select App")
        try:
            print (filename[0])
            print (filename)
            filenameApp = filename[0]
            print ("chose App")
        except:
            pass

    def selectDes(self, path, filename):
        print ("select Des")
        try:
            print (filename[0])
            filenameDes = path
            print ("chose Des")
        except:
            pass

    def merge(self, filenameBoot, filenameApp, filenameDes):

        #print ("printing...")
        #print (filenameBoot)
        filenameBootClean = (str(filenameBoot))[2:-2]
        print (filenameBootClean)
        #print (filenameApp)
        filenameAppClean = (str(filenameApp))[2:-2]
        #print (filenameDes)

        print ("srec_cat.exe " + str(filenameBootClean) + " -Intel " + str(filenameAppClean) + " -Intel " + " -o " + "merge.hex" + " -Intel")
        os.system("srec_cat.exe " + str(filenameBootClean) + " -Intel " + str(filenameAppClean) + " -Intel " + " -o " + "merge.hex" + " -Intel")

        return ("done!")


    def printit(self, it):
        print ("printit: ")
        print (it)

#    def selectBootloader(self, bootPath):
#            self.bootPath =

class mergehexApp(App):

    filenameBoot = ''
    filenameApp = ''
    filenameDes = ''
    def build(self):
        return mergehexGridLayout()



mergehexApp = mergehexApp()
mergehexApp.run()
