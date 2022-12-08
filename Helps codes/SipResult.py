import pyshark
import pandas as pd
import openpyxl

listResponseTime = []
listResponseRequest = []

listFromUser = []
listToUser = []

listStatusCode = []

listCnFromUser = []
listPrefixFromUser = []

listCnAndPrefix = []

def showResult():
    cap = pyshark.FileCapture("../input/saida.pcap",display_filter="sip")
    for i in cap:
        
        try:
            fromUser = i.sip.from_user
            toUser = i.sip.to_user
            statusCode = i.sip.status_code
            responseTime = i.sip.response_time
            requestFrame = i.sip.response_request

            print(f"{responseTime}, {requestFrame}, {fromUser}, {toUser}, {statusCode}")

            listFromUser.append(fromUser)
            listToUser.append(toUser)
            listStatusCode.append(statusCode)
            listResponseTime.append(responseTime)
            listResponseRequest.append(requestFrame)

        except Exception as e:
            print(e)
    
def removeSheet():
    wb = openpyxl.load_workbook("../output/teste.xlsx")
    resultSheet = wb["SipResult"]
    wb.remove(resultSheet)
    wb.save("../output/teste.xlsx")

def showCn():
    for cn in listFromUser:
        listCnFromUser.append(cn[3:5]) 
        listPrefixFromUser.append(cn[5:9])
        listCnAndPrefix.append(f"{cn[3:5]}{cn[5:9]}")

def createResultFile():
    df = pd.DataFrame(zip(listResponseTime, listResponseRequest, listFromUser,listToUser,listStatusCode,listCnFromUser,listPrefixFromUser,listCnAndPrefix),columns=["ResponseTime(ms)", "ResponseRequest","Origem","Destino","Status","CN_Origem","Prefixo_Origem","Cn + Prefixo"])
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