# 调用dll测试
# host ip: 122.226.14.236

import ctypes
from ctypes import *

'''
模拟账号：018888027
密码： trader
'''


import win32com.client
from win32com.client import gencache

ZZBCE_ServerIp='122.226.14.236'
ZZBCE_ServerPort=52768


shell = gencache.EnsureDispatch('TradeCOM.Trade')
market = win32com.client.Dispatch("TradeCOM.Market")

trade = win32com.client.Dispatch("TradeCOM.Trade")
# ret = market.Login('122.226.14.236', 52768, '010500001', 'trader123', 60)
ret = market.Login(ZZBCE_ServerIp, ZZBCE_ServerPort, '018888027', 'trader', 60)
if ret == 0:
    print('Login')
if market.Connected:
    print('Server Conneted')


