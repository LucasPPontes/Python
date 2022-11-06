import pandas as pd

df = pd.read_excel("Pasta1.xlsx")

nums = []

with open("numbers.txt","r") as numbersfile:
    for line in numbersfile:
        nums.append(line.strip())



num1 = list(df["num1"])
num2 = list(df["num2"])
status = list(df["status"])

with open("result.csv","w") as file2:
    
    for(n1,n2,n3) in zip(num1,num2,status):
        x = range(n1,n2+1)

        for n in nums:
            n_int = int(n)
            if n_int in x:
                file2.write(f"{n},{n3}\n")
