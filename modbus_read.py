#ruk.shan@outlook.com
#reading modbus tcp 
#Tested with python 3.8.10
#05-12-2021

#!/usr/bin/python

from pyModbusTCP.client import ModbusClient
from config import read_config

class ReadModbus():

    def __init__(self,modbus_label):
        config_data =  read_config()
        modbus_config = config_data[modbus_label]
        self.host = modbus_config["modbus_client_ip"]
        self.port = modbus_config["modbus_port_number"]
        self.register  =  modbus_config["modbus_reg_number"] 
        self.number_of_regs = modbus_config["number_of_reg_to_read"]
        self.status_msg = ""

    #connect to UR
    def connect_to_UR(self):
        try:
            self.modbus_conn = ModbusClient(self.host, self.port, auto_open=True,auto_close=True)
            print (self.modbus_conn)
            self.status_msg = "connected to modbus"
        except ValueError: 
            print ("connection error")
            self.status_msg = "connection error"

    #read UR joints
    def read_reg_UR(self):
        reg = self.modbus_conn.read_holding_registers(self.register,self.number_of_regs)
        return reg
 

# modbus_01 = ReadModbus("robot_joints")
# modbus_01.connect_to_UR()
# print (modbus_01.read_reg_UR())