#ruk.shan@outlook.com
#reading modbus tcp 
#Tested with python 3.8.10
#05-12-2021

#!/usr/bin/python

from pyModbusTCP.client import ModbusClient
from config import read_config

class ReadModbus:

    
    def __init__(self, host,port,register,number_of_regs):
        self.host = host
        self.port  = port
        self.register = register
        self.number_of_regs = number_of_regs 
  
    #connect to UR
    def connect_to_UR(self):
        global modbus_conn
        modbus_conn = ModbusClient(host="192.168.68.116", port=502, auto_open=True)
        print ("connected to modbus")

    #read UR joints
    def read_reg_UR(self):
        global modbus_conn
        reg = modbus_conn.read_holding_registers(206,1)
        return reg

modbus_01 = ReadModbus("192.168.68.116",502,206,1)
modbus_01.connect_to_UR()
print (modbus_01.read_reg_UR())