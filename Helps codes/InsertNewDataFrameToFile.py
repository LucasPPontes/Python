import pandas as pd
import openpyxl

def remove_sheet():

    wb = openpyxl.load_workbook("teste.xlsx")
    numbersSheet = wb["numbers"]
    wb.remove(numbersSheet)
    wb.save("teste.xlsx")


def create_xlsx():

    col1 = ["190","200","210","220","454"]
    col2 = ["90","100","110","120","343"]
    status = ["423","200","100","487","4534"]

    dfAll = pd.DataFrame(list(zip(col1,col2,status)),columns=["Origem","Destino","Status"])
    print(dfAll)

    with pd.ExcelWriter("teste.xlsx",mode="a") as writer:
        dfAll.to_excel(writer, sheet_name="numbers",index=None)


def main():
    try:
        remove_sheet()
    except Exception as e:
        print(e)
    create_xlsx()
main()