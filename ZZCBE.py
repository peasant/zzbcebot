# 调用dll测试
# host ip: 122.226.14.236

import ctypes
from ctypes import *
import time

'''
模拟账号：018888027
密码： trader
'''




import win32com.client
from win32com.client import gencache

ZZBCE_ServerIp='122.226.14.236'
ZZBCE_ServerPort=58095 #52768 #

'''非模拟账号'''
TRADER_ID="010500001"
TRADER_PSWD="trade123"

'''模拟账号'''
# TRADER_ID="018888027"
# TRADER_PSWD="trader"
CONNECTSTATUS= 0
data=''
errorId=5566
ret=1 #失败

class callBackEvents(object):
    """ Callback Object for win32com
    """

    def OnConnected(self):
        """on connected"""
        print('Connected.\n')

    def OnDisconnected(self):
        """on disconnected"""
        print('Disconnected\n')

    def OnRecvData(self, xmldata):
        """receive data"""
        print("receive:{}".format(xmldata))

callBackEvents.xmldata=data

tradeEvents= win32com.client.DispatchWithEvents("TradeCOM.Trade",callBackEvents)
#print(win32com.client.getevents("TradeCOM.Trade"))

#trade = gencache.EnsureDispatch('TradeCOM.Trade')
market = win32com.client.Dispatch("TradeCOM.Market")
trade = win32com.client.Dispatch("TradeCOM.Trade")


#ret = market.Login('122.226.14.236', 52768, '010500001', 'trader123', 60)
#ret = market.Login(ZZBCE_ServerIp, ZZBCE_ServerPort, TRADER_ID, TRADER_PSWD, 300)
ret = trade.Login(ZZBCE_ServerIp, ZZBCE_ServerPort, TRADER_ID, TRADER_PSWD,50)
#time.sleep(5)

CONNECTSTATUS= trade.Connected


if CONNECTSTATUS:
    print('服务器已连接')
else:
    print('服务器未连接')

data='<Send ID="1001" />'

if trade.Execute(data) == 0:  #指令发送成功
    print(tradeEvents.OnRecvData(data))
else:
    print('\nlasterror:', trade.LastError)

#print('ErrorID:', errorId)



#
# from tkinter import *
# import time
#
#
# app=Tk()
# # ret = trade.Login(ZZBCE_ServerIp, ZZBCE_ServerPort, '018888027', 'trader', 60)
# if CONNECTSTATUS==True:
#     status= '已连接'
# else:
#     status= '未连接'
#
# #time.sleep(2)
# connectStatus=Label(app, text=status)
# connectStatus.pack()
#
#
#
# #app.master.title('ZZBCE辅助程序')
# app.mainloop()

trade.Logout()