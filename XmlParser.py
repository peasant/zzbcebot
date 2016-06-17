#xml解析文件

# try:
#     import xml.etree.cElementTree as ET
# except ImportError:
#     import xml.etree.ElementTree as ET
# import sys

xmlData= '<Recv ID="2102"><Data WareID="ZPCA1" WareName="大黄鱼A1" LimitUP="29.38" LimitDown="26.58" EnabledMoney="499393.11" OpenPrice="27.80" NewPrice="27.72" RaiseLose="-0.26" RaiseLose2="-0.9292" HighPrice="27.82" LowPrice="27.70" AvgPrice="27.76" ContNum="261634" HoldNum="139462" Yesterday="27.98" BuyPrice1="27.72" BuyPrice2="27.70" BuyPrice3="27.68" BuyPrice4="0.00" BuyPrice5="0.00" BuyQty1="183" BuyQty2="1253" BuyQty3="98" BuyQty4="0" BuyQty5="0" SalePrice1="27.74" SalePrice2="27.76" SalePrice3="27.78" SalePrice4="0.00" SalePrice5="0.00" SalQty1="708" SalQty2="96" SalQty3="50" SalQty4="0" SalQty5="0" MinUnit="1" MinChgPrice="0.02" SaleNum="261" BuyNum="35" MAXSQty="17905" MAXBQty="17905" CURSHold="261" CURBHold="35" SMaxNum="2000" DepotNum="0" CSaleNum="0" CBuyNum="0" PriceDecimal="2" /></Recv>'

#报文转化为字典
price=xmlData.split('><')[1].strip('<').strip('/>').split(' ')[1:-1]
dPrice={}
for i in price:
    l=i.split('=')
    dPrice[l[0]]=l[1]

print(eval(dPrice['BuyPrice1']))