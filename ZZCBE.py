# 调用dll测试
# host ip: 122.226.14.236

import ctypes
from ctypes import *
import time

import win32com.client
from win32com.client import gencache

ZZBCE_ServerIp = '122.226.14.236'
# ZZBCE_ServerPort = 52000 #57000 #57000为模拟端口 #57268 # 48095#
#
# '''非模拟账号'''
# TRADER_ID = "010500001"
# TRADER_PSWD = "trader123"
# ZZBCE_ServerPort= 52000

'''模拟账号'''
TRADER_ID = "018888027"
TRADER_PSWD = "trader"
ZZBCE_ServerPort = 57000

connectStatus = 0
data = ''
errorId = 5566
ret = 1  # 失败
global recvData


# eventobj=win32com.client.getevents("TradeCOM.Trade")
class callBackEvents():
    """ Callback Object for win32com
    """

    # TODO 连接状态
    # TODO 多线程
    def __init__(self, xmldata=''):
        xmldata = ''

    def get_params(self, xmldata):
        return self.xmldata

    def OnConnected(self):
        """on connected"""
        print('已连接.')

    def OnDisconnected(self):
        """on disconnected"""
        print('已断开')

    def OnRecvData(self, data):
        """receive data"""
        self.xmldata = data
        print("RECV :{}".format(data))


# market = win32com.client.Dispatch("TradeCOM.Market")
# marketEvents = win32com.client.WithEvents(market, callBackEvents)
# ret = market.Login(ZZBCE_ServerIp, ZZBCE_ServerPort, TRADER_ID, TRADER_PSWD, 300)

trade = win32com.client.Dispatch("TradeCOM.Trade")
# tradeEvents = win32com.client.WithEvents(trade, callBackEvents)
trade = win32com.client.DispatchWithEvents("TradeCOM.Trade", callBackEvents)
ret = trade.Login(ZZBCE_ServerIp, ZZBCE_ServerPort, TRADER_ID, TRADER_PSWD, 300, )

connectStatus = trade.Connected
time.sleep(0.2)
print(trade.get_params(data))

# if trade.Connected == True:
#     print('服务器已连接')
# else:
#     print('服务器未连接')

data = '<Send ID="2102" WareID="ZPCA1" />'

ret = trade.Execute(data)  # 指令发送成功
time.sleep(0.2)
recvData = trade.get_params(data)

if ret == 0:
    print()
else:
    print('lasterror:', trade.LastError)


#解析XML，存入字典
# price=recvData.split('><')[1].strip('<').strip('/>').split(' ')[1:-1]
# dPrice={}
# for i in price:
#     l=i.split('=')
#     dPrice[l[0]]=l[1]
# print(dPrice)
# print(len(dPrice))
def raw2Dict(data):
    item = data.split('><')[1].strip('<').strip('/>').split(' ')[1:-1]
    retDict={}
    for i in item:
        l=i.split('=')
        retDict[l[0]]=l[1]
    return(retDict)

dPrice=raw2Dict(recvData)

#窗口
from tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.geometry('800x600')
        self.pack()
        self.createWidgets()


    def createWidgets(self):
        self.safeRateLabel=Label(self, text= "安全率："+ self.showSafeRate().strip('\"'))
        self.safeRateLabel.pack()
        self.warename=Label(self, text='最新报价: '+dPrice['NewPrice'].strip('\"'))
        self.warename.pack()
        self.quitButton= Button(self, text="Quit", command= self.quit())
        self.quitButton.pack()

    def showSafeRate(self):
        trade.Execute('<Send ID="1004"/>')
        time.sleep(0.2)
        return raw2Dict(trade.get_params(data))['SaftRate']




app= Application()
app.master.title("ZZBCE辅助程序")
app.mainloop()

