import pyshark
import pandas as pd
import openpyxl

listFromUser = []
listToUser = []
listStatusCode = []
listCn = []
listPrefix = []

def showResult():
    cap = pyshark.FileCapture("../input/saida.pcap",display_filter="sip")
    for i in cap:
        
        try:
            fromUser = i.sip.from_user
            toUser = i.sip.to_user
            statusCode = i.sip.status_code
            
            listFromUser.append(fromUser)
            listToUser.append(toUser)
            listStatusCode.append(statusCode)

        except Exception as e:
            print(e)
    
def removeSheet():
    wb = openpyxl.load_workbook("../output/teste.xlsx")
    resultSheet = wb["SipResult"]
    wb.remove(resultSheet)
    wb.save("../output/teste.xlsx")

def showCn():
    for cn in listFromUser:
        listCn.append(cn[3:5]) 
        listPrefix.append(cn[5:9])

def createResultFile():
    df = pd.DataFrame(zip(listFromUser,listToUser,listStatusCode,listCn,listPrefix),columns=["FromUser","ToUser","Status","CN","Prefix"])
    df = df.astype(str)

    print(df)

    with pd.ExcelWriter("../output/teste.xlsx", mode="a") as writer:
        df.to_excel(writer,sheet_name="SipResult", index=None)

    print("xlsx criado")
        
def main():
    showResult()
    try:
        removeSheet()
    except Exception as e:
        print(e)

    showCn()
    createResultFile()
main()

