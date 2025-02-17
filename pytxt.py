name=input("Enter name : ")
id1=input("Enter id : ")
basicsalary=int(input("Enter basic salary : "))
allowance=int(input("Enter allowance : "))
bonus=int(input("Enter"))
monthly_salary=basicsalary +allowance
annual_salary=monthly_salary*12+bonus/100*(monthly_salary*12)
print("Employee details are : ")
for i in [name,id1,basicsalary,allowance,bonus,monthly_salary,annual_salary]:
    print(f'%-25s ={i}'%str(i))