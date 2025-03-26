import win32com.client as win32
import os

class Aspen:
    def __init__(self):
        super().__init__()
        self.sims = []
        path = os.getcwd()
        self.simdir = os.path.join(path, "sim")
        self.message = ""
        self.lasterr = ""
        self.OpenSimulationFile()
    
    def OpenSimulationFile(self):
        try:
            self.app = win32.GetObject(os.path.join(self.simdir,"DynamicsU407C2De.dynf"))
            self.message = "Simulation Openned"
            return True
        except:
            self.lasterr = "Cannot Open Simulation"
            return False
            

    def Visible(self):
        self.app.Application.Visible = True