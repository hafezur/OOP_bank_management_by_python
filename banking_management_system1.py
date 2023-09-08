
class Person:
    list_salary=[]
    def __init__(self,email,password) -> None:
        self.email=email
        self.password=password


class User(Person):
    user_balance=0
    user_list=[]
    def __init__(self, email, password) -> None:
        self.balance=0
        super().__init__(email, password)
    
class Bank(User):
    user_balance=0
    def __init__(self, email, password) -> None:
        super().__init__(email, password)
        self.main_balance=0
        self.loan_amount_main=0
    
    def have_depo(self,amount):
        self.main_balance+=amount
        self.user_balance+=amount
    
    def have_withdraw(self,amount1):
        self.main_balance-=amount1 
        self.user_balance-=amount1 
    
    def have_show(self):
        print("The balance is: ",self.main_balance) 
    
    def take_loan(self,loan_amount):
        #print("sent loan amount,",loan_amount)
        #print("user balance",self.user_balance)
        if loan_amount<=self.user_balance*2:
            self.main_balance-=loan_amount
            self.user_balance-=loan_amount
            self.loan_amount_main+=loan_amount
            #print("The loan amount is: ",self.loan_amount_main)
        else:
            print("insuffecient balance!!! please deposit and try Again:") 

    def show_loan_from_bank(self):
        print("The loan Amount is: ",self.loan_amount_main)

class Admin(Bank):
    admin_list=[]
    def __init__(self, email, password) -> None:
        super().__init__(email, password)
    
    def Check_total_balance(self):
        restore=self.main_balance
        print("the balance is: ",restore)


  

while(True):
    input1=int(input("Press 1 for Create Account As A User:\nPress 2 for Create Account As Admin\nPress 3 for Exit:\n"))
    user1=User('hafiz@gamil.com','111')
    if input1==1:
         email1=input("Enter Your Email: ")
         password1=input("Enter Your Password: ")
         while(True):
            value=int(input("Enter 1 for login:\nEnter 2 for Exit:\n"))
            if value==1:
                print("Conform Your Email And Password For Login:")
                email2=input("Enter Your Email: ")
                password2=input("Enter Your Password: ")
                convert=vars(user1)
                user1.user_list.append(convert)
                call_bank=Bank('hafaffa','ajfkaj')
                if email1==email2 and password1==password2:
                    print("******////******Welcome To Agricultural Bank******\\\\\******")
                    while(True):
                        input2=int(input("Enter 1 for Deposit:\nEnter 2 for Withdraw:\nEnter 3 for Check Balance:\nEnter 4 for Take_loan:\nEnter 5 for Exit:\n"))
                        if input2==1:
                            input_deposit=int(input("Enter Your Amount: "))
                            call_bank.have_depo(input_deposit)
                            user1.user_balance+=input_deposit
                        elif input2==2:
                            input_withdraw=int(input("Enter Amount for withdraw: "))
                            call_bank.have_withdraw(input_withdraw)
                            user1.user_balance-=input_withdraw

                        elif input2==3:
                            call_bank.have_show()
                        elif input2==4:
                            input_loan=int(input("Enter Loan Amount: "))
                            call_bank.take_loan(input_loan)
                        else:
                            break
                else:
                    break
            
            else:
                break
         

    elif input1==2:
        email3=input("Enter Your Email: ")
        password3=input("Enter Your Password: ")
        while(True):
            value1=int(input("Enter 1 for login:\nEnter 2 for Exit:\n"))
            if value1==1:
                print("Conform Your Email And Password For Login:")
                email4=input("Enter Your Email: ")
                password4=input("Enter Your Password: ")
                admin1=Admin('shohag@gmail.com','12drehr')
                con_admin=vars(admin1)
                admin1.admin_list.append(con_admin)
                if email3==email4 and password3==password4:
                    print("******////******Welcome To Agricultural Bank******\\\\\******")
                    while(True):
                        input5=int(input("Enter 1 for Check Total Balance:\nEnter 2 for Check Total Loan:\nEnter 3 for On and Off loan feature:\nEnter 4 for Exit:\n"))
                        if input5==1:
                            call_bank.have_show()
                        
                        elif input5==2:
                            call_bank.show_loan_from_bank()
                        
                        elif input5==3:
                            pass
                        else:
                            break
                else:
                    break
            
            
            else:
                break
    else:
        break