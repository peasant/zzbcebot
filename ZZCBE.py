# 调用dll测试
# host ip: 122.226.14.236

import ctypes
from ctypes import *
import time


import win32com.client
from win32com.client import gencache

ZZBCE_ServerIp = '122.226.14.236'
#ZZBCE_ServerPort = 52000 #57000 #57000为模拟端口 #57268 # 48095#
#
# '''非模拟账号'''
# TRADER_ID = "010500001"
# TRADER_PSWD = "trader123"
# ZZBCE_ServerPort= 52000

'''模拟账号'''
TRADER_ID = "018888027"
TRADER_PSWD ="trader"
ZZBCE_ServerPort= 57000

connectStatus = 0
data = ''
errorId = 5566
ret = 1  # 失败


# eventobj=win32com.client.getevents("TradeCOM.Trade")
class callBackEvents():
    """ Callback Object for win32com
    """
    #TODO 传递xmldata出去
    def __init__(self,xmldata=''):
        xmldata=''

    def get_params(self,xmldata):
        return self.xmldata

    def OnConnected(self):
        """on connected"""
        print('已连接.')

    def OnDisconnected(self):
        """on disconnected"""
        print('已断开')

    def OnRecvData(self,data ):
        """receive data"""
        self.xmldata=data
        print("RECV :{}".format(data))

# market = win32com.client.Dispatch("TradeCOM.Market")
# marketEvents = win32com.client.WithEvents(market, callBackEvents)
# ret = market.Login(ZZBCE_ServerIp, ZZBCE_ServerPort, TRADER_ID, TRADER_PSWD, 300)

trade = win32com.client.Dispatch("TradeCOM.Trade")
#tradeEvents = win32com.client.WithEvents(trade, callBackEvents)
trade= win32com.client.DispatchWithEvents("TradeCOM.Trade", callBackEvents)
ret = trade.Login(ZZBCE_ServerIp, ZZBCE_ServerPort, TRADER_ID, TRADER_PSWD, 300,)

connectStatus = trade.Connected
time.sleep(0.2)
print(trade.get_params(data))

# if trade.Connected == True:
#     print('服务器已连接')
# else:
#     print('服务器未连接')

data = '<Send ID="2102" WareID="ZPCA1" />'


ret= trade.Execute(data)   # 指令发送成功
time.sleep(0.2)
recvData= trade.get_params(data)

#TODO 解析XML
print (recvData)

if ret ==0:
    print()
else:
    print('lasterror:', trade.LastError)

    #
    # from tkinter import *
    # import time
    #
    #
    # app=Tk()
    # # ret = trade.Login(ZZBCE_ServerIp, ZZBCE_ServerPort, '018888027', 'trader', 60)
    # if connectStatus==True:
    #     status= '已连接'
    # else:
    #     status= '未连接'
    #
    # #time.sleep(2)
    # cnctStatus=Label(app, text=status)
    # cnctStatus.pack()
    #
    #
    #
    # #app.master.title('ZZBCE辅助程序')
    # app.mainloop()

trade.Logout()

