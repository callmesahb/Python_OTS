from PyQt6.QtCore import QObject, pyqtSignal, pyqtSlot
from OpcClient import OpcClient as opc
from workerThread import Worker
import pandas as pd
import os
import sys
import json

class Store(QObject):
    updatevalues = pyqtSignal(dict,list)
    def __init__(self,data,tags):
        super().__init__()
        self.tags = tags
        self.data = data
        current_path = os.getcwd()
        opc_path = os.path.join(current_path,"new opc")
        tags_path = os.path.join(current_path,"data")
        self.tagsfile = os.path.join(tags_path,"tags.json")
        self.certfile = os.path.join(opc_path,"cert.json")
        self.csvpath = os.path.join(opc_path,"tags.csv")
        self.csvfile = pd.read_csv(self.csvpath)
        self.opcSettings = self.read_json_file(self.certfile)
        url = self.opcSettings["endPointUrl"]
        self.opc = opc(url)
        self.getting_names()
        self.gettingvalvedata()
        self.tag = self.ReadingtagsFile()
        self.ReadingTagClient()
        
    def ReadingtagsFile(self) -> list:
        with open(self.tagsfile,"r") as file:
            data = json.load(file)
        return data
    
    def getting_names(self) -> list:
        self.names = []
        for i in self.tags:
            self.names.append(i["name"])
        return self.names
    
    def gettingvalvedata(self) -> dict:
        valves = []
        for i in self.tags:
            if "defaultValue" in i:
                valves.append(i)
        self.valve_value_map = {item['name']: item['initial'] for item in valves}
        return self.valve_value_map
    def setting_valueEV(self,varid):
        return self.valve_value_map.get(varid)
    
    def SettingInitial(self,varid) -> float:
        initial = 0.0
        if varid in self.names:
            varid_dict = next(item for item in self.tags if item['name'] == varid)
            initial = varid_dict["initial"]
        return round(initial,2)
    
    def SettingDetailsofsensor(self,varid:str) -> list:
        min = 0.0
        max = 0.0
        LL = 0.0
        HH = 0.0
        L = 0.0
        H = 0.0
        details = []
        if varid in self.names:
            varid_dict = next(item for item in self.tags if item['name'] == varid)
            min = varid_dict["R"][0]
            max = varid_dict["R"][1]
            LL = varid_dict["HHR"][0]
            HH = varid_dict["HHR"][1]
            L = varid_dict["HR"][0]
            H = varid_dict["HR"][1]
            details.append(min)
            details.append(max)
            details.append(LL)
            details.append(HH)
            details.append(L)
            details.append(H)
        return details
    def GettingUnit(self,varid) -> str:
        unit = ""
        if varid in self.names:
            varid_dict = next(item for item in self.tags if item['name'] == varid)
            unit = varid_dict["unit"]
        return unit

    def GettingControllerDetails(self,varid:str) -> list:
        Varid = varid.replace("OP","")
        sp = Varid + "SP"
        pv = Varid + "PV"
        op = Varid + "OP"
        tv = Varid + "TV"
        spvalue = 0.0
        pvvalue = 0.0
        opvalue = 0.0
        tvvalue = 1.0
        if sp in self.names or pv in self.names or op in self.names:
            varid_dict = next(item for item in self.tags if item['name'] == sp)
            varid_dict1 = next(item for item in self.tags if item['name'] == pv)
            varid_dict2 = next(item for item in self.tags if item['name'] == op)
            varid_dict3 = next(item for item in self.tags if item['name'] == tv)
            spvalue = varid_dict["initial"]
            pvvalue = varid_dict1["initial"]
            opvalue = varid_dict2["initial"]
            tvvalue = varid_dict3["initial"]
        oplist = [spvalue,pvvalue,opvalue , tvvalue]
        return oplist
    
    def ListingDescs(self,index:int) -> dict:
        page = self.data["layout"]["sections"][index]
        return page
    
    def GettingrangesofController(self,varid:str):
        varId = varid + "PV"
        if varId in self.names:
            varid_dict = next(item for item in self.tags if item['name'] == varId)
        

    
    def read_json_file(self,file_path) -> dict:
        with open(file_path,"r") as file:
            data = json.load(file)
        return data

    def ReadingTagClient(self):
        newtags = {i: self.opc.getValue(i) for i in self.csvfile["tag"]}
        # print(type(newtags))
        self.updatevalues.emit(newtags,self.tag)