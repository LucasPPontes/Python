import pyshark
import pandas as pd
import openpyxl

listResponseTime = []
listResponseRequest = []

listFromUser = []
listToUser = []

listStatusCode = []
listResultStatus = []

listCnFromUser = []
listPrefixFromUser = []

listCnAndPrefix = []

listCallId = []
listViaBranch = []

def showResult():
    cap = pyshark.FileCapture("../input/saida.pcap",display_filter="sip")
    for i in cap:
        
        try:
            fromUser = i.sip.from_user
            toUser = i.sip.to_user
            statusCode = i.sip.status_code
            responseTime = i.sip.response_time
            requestFrame = i.sip.response_request
            callId = i.sip.call_id
            viaBranch = i.sip.via_branch

            print(f"{responseTime}, {requestFrame}, {fromUser}, {toUser}, {statusCode}, {callId}")

            listFromUser.append(fromUser)
            listToUser.append(toUser)
            listStatusCode.append(statusCode)
            listResponseTime.append(responseTime)
            listResponseRequest.append(requestFrame)
            listCallId.append(callId)
            listViaBranch.append(viaBranch)

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

def showResponseStatusResult():
    for status in listStatusCode:
        if status[0] == "2":
            listResultStatus.append("OK")
        elif status[0] == "4":
            listResultStatus.append("NOK")
        else:
            listResultStatus.append("Trying")


def createResultFile():

    dfResult = pd.DataFrame(zip(listResponseTime, listResponseRequest, listFromUser,listToUser,listStatusCode,listResultStatus,listCallId,listViaBranch,listCnFromUser,listPrefixFromUser,listCnAndPrefix),columns=["ResponseTime(ms)", "ResponseRequest","Origem","Destino","Status","Response","Call Id","Via Branch","CN_Origem","Prefixo_Origem","Cn + Prefixo"])

    dfResult["Cn + Prefixo"]=dfResult["Cn + Prefixo"].astype(int)

    dfPrefix = pd.read_excel("../output/teste.xlsx",sheet_name="Prefixo")
    dfPrefix.drop(["CN","Prefixo"],axis=1,inplace=True)

    df = pd.merge(dfResult,dfPrefix,on="Cn + Prefixo")
    df = df.drop_duplicates(subset=["Origem","Destino","Status"])

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
    showResponseStatusResult()
    createResultFile()
main()