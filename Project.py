import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from os import system
from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits, punctuation

class BankManagement :
    
    # region command for login button page 2  (not finished)
    def show_login_page(self):
    
        self.label_mainpage.grid_forget()
        self.button_login.grid_forget()
        self.button_registry.grid_forget()

        self.label_login.grid(row=1, column=0, padx=300)
        self.label_username_page2.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.entry_username_page2.grid(row=2, column=1, padx=10, pady=10, sticky='w')
        self.label_password_page2.grid(row=4, column=0, padx=10, pady=10, sticky='w')
        self.entry_password_page2.grid(row=4, column=1, padx=10, pady=30, sticky='w')
        self.button_enter.grid(row=5, column=0, padx=300, sticky='w')
        self.button_back_page2.grid(row=5, column=1, padx=100, sticky='w')





    #endregion

   
    # region command for back button page 2
    def back_to_main_page(self):

        self.label_login.grid_forget()
        self.label_username_page2.grid_forget()
        self.entry_username_page2.grid_forget()
        self.label_password_page2.grid_forget()
        self.entry_password_page2.grid_forget()
        self.button_enter.grid_forget()
        self.button_back_page2.grid_forget()

        self.label_mainpage.grid(row = 1, column = 0, padx = 300)
        self.button_login.grid(row = 2, column = 0, padx=150, sticky='w') 
        self.button_registry.grid(row = 2, column = 0)

    #endregion


    # region registry button

    def registry_page(self):
        
        self.label_mainpage.grid_forget()
        self.button_login.grid_forget()
        self.button_registry.grid_forget()

        self.label_registration.grid(row=1, column=0, padx=300)
        self.label_name.grid(row=2, column=0)
        self.entry_name.grid(row=2, column=1)
        self.label_family.grid(row=3, column=0)
        self.entry_family.grid(row=3, column=1)
        self.label_nationalcode.grid(row=4, column=0)
        self.entry_nationalcode.grid(row=4, column=1)
        self.label_dateofbirth.grid(row=5, column=0)
        self.entry_dateofbirth.grid(row=5, column=1)
        self.label_email.grid(row=6, column=0)
        self.entry_email.grid(row=6, column=1)
        self.label_password.grid(row=7, column=0)
        self.entry_password.grid(row=7, column=1)
        self.label_confirmpassword.grid(row=8, column=0)
        self.entry_confirmpassword.grid(row=8, column=1)
        self.button_submit.grid(row=9, column=1)
        self.button_back_page3.grid(row=9, column=2)
    
    #endregion


    # region command for submit button page3 (not finished)
    def login(self):
        
        self.name = self.entry_name.get()
        self.family = self.entry_family.get()
        self.nationalcode = self.entry_nationalcode.get()
        self.dateofbirth = self.entry_dateofbirth.get()
        self.email = self.entry_email.get()
        self.password = self.entry_password.get()
        self.confirmpassword = self.entry_confirmpassword.get()

        if self.name and self.family and self.nationalcode and self.dateofbirth and self.email and self.password and self.confirmpassword == '' :
            messagebox.showerror('Error:', 'Please complete all the required items!!!')

        elif len(self.password)<8:
            messagebox.showerror('Error:',"Your Password must have more than 8 characters.")

        elif self.password.intersection(ascii_lowercase):
            messagebox.showerror('Error:',"Your Password must have at least a lower character. ")

        elif self.password.intersection(ascii_uppercase):
            messagebox.showerror('Error:',"Your Password must have at least a capital character.")  

        elif self.password.intersection(digits):
            messagebox.showerror('Error:',"Your Password must have at least one number.")  

        elif self.password.intersection(punctuation):
            messagebox.showerror('Error:'," Your Password must have at least a Punctuation character.")  

        else:
            self.password.difference(ascii_letters+digits+punctuation)
            messagebox.showerror('Error:',"Character error")

        if self.password == self.confirmpassword :
                    
            def save_to_file(self, data, filename='data.txt'):                
                    with open(filename, 'a') as file:
                        self.file.write(f"Name: {data['Name']}, Family: {data['Family']}, Age: {data['Age']}, Email: {data['Email']}, Password: {data['Password']}\n")
        
            user_info = {
                'Name': self.name,
                'Family': self.family,
                'Age': self.dateofbirth,
                'Email': self.email,
                'Password' : self.confirmpassword
            }
        
            self.save_to_file(user_info)  

        self.label_mainpage.grid_forget()
        self.button_login.grid_forget()
        self.button_registry.grid_forget()

        self.label_registration.grid_forget()
        self.label_name.grid_forget()
        self.entry_name.grid_forget()
        self.label_family.grid_forget()
        self.entry_family.grid_forget()
        self.label_nationalcode.grid_forget()
        self.entry_nationalcode.grid_forget()
        self.label_dateofbirth.grid_forget()
        self.entry_dateofbirth.grid_forget()  
        self.label_email.grid_forget()
        self.entry_email.grid_forget()  
        self.label_password.grid_forget()
        self.entry_password.grid_forget()  
        self.label_confirmpassword.grid_forget()
        self.entry_confirmpassword.grid_forget()
        self.button_submit.grid_forget()
        self.button_back_page3.grid_forget()

        self.label_login.grid(row=1, column=0, padx=300)
        self.label_username_page2.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.entry_username_page2.grid(row=2, column=1, padx=10, pady=10, sticky='w')
        self.label_password_page2.grid(row=4, column=0, padx=10, pady=10, sticky='w')
        self.entry_password_page2.grid(row=4, column=1, padx=10, pady=30)
        self.button_enter.grid(row=5, column=0, padx=100, sticky='w')
        self.button_back_page2.grid(row=5, column=1, padx=100, sticky='w')


        










    #endregion
    






    #____________________________________________________________________________________________ 
    def __init__(self):
        self.main_page()

    # MAIN PAGE
    def main_page(self):
        
        self.app = ttk.Window(themename = 'solar')
        self.app.geometry('600x600')
        self.app.title('Bank Management App')
        
        self.label_mainpage= ttk.Label(self.app, text = 'Bank Manegment Project', font =('arial', 18))
        self.label_mainpage.grid(row = 1, column = 0, padx = 300)
        
        
        self.button_login = ttk.Button(self.app, text = 'Login', style = SUCCESS, command=self.show_login_page) #command = page2
        self.button_login.grid(row = 2, column = 0, padx=150, sticky='w') 
        
        self.button_registry = ttk.Button(self.app, text = 'Registry', style = SUCCESS, command=self.registry_page)  #command = registery_user_page3
        self.button_registry.grid(row = 2, column = 0)
        
        
        
        # PAGE 2(UI): just for login 

        self.label_login = ttk.Label(self.app, text= 'Login', font=('arial', 20, 'bold'))
        self.label_login.grid(row=1, column=0, padx=300)
        self.label_login.grid_forget()
        
        self.label_username_page2 = ttk.Label(self.app, text= 'User name', font= ('arial', 15, 'bold'))
        self.label_username_page2.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.label_username_page2.grid_forget()
        
        self.entry_username_page2 = ttk.Entry(self.app)
        self.entry_username_page2.grid(row=2, column=1, padx=10, pady=10, sticky='w')
        self.entry_username_page2.grid_forget()
        
        self.label_password_page2 = ttk.Label(self.app, text= 'Password', font=('arial', 15, 'bold'))
        self.label_password_page2.grid(row=4, column=0, padx=10, pady=10, sticky='w')
        self.label_password_page2.grid_forget()
        
        self.entry_password_page2 = ttk.Entry(self.app)
        self.entry_password_page2.grid(row=4, column=1, padx=10, pady=30)
        self.entry_password_page2.grid_forget()
        
        self.button_enter = ttk.Button(self.app, text = 'Enter', style = SUCCESS) #command = vorood be app
        self.button_enter.grid(row=5, column=0, padx=100, sticky='w')
        self.button_enter.grid_forget()

        self.button_back_page2 = ttk.Button(self.app, text = 'Back', style = SUCCESS, command=self.back_to_main_page) #command = back to main page
        self.button_back_page2.grid(row=5, column=1, padx=100, sticky='w')
        self.button_back_page2.grid_forget()


        # PAGE 3(UI): just for Registry

        self.label_registration = ttk.Label(self.app, text= 'Registration', font=('arial', 18, 'bold'))
        self.label_registration.grid(row=1, column=0, padx=300)
        self.label_registration.grid_forget()

        self.label_name = ttk.Label(self.app, text='Name', font=('arial', 15, 'bold'))
        self.label_name.grid(row=2, column=0)
        self.label_name.grid_forget()

        self.entry_name = ttk.Entry(self.app)
        self.entry_name.grid(row=2, column=1)
        self.entry_name.grid_forget()

        self.label_family = ttk.Label(self.app, text='Family',font=('arial', 15, 'bold'))
        self.label_family.grid(row=3, column=0)
        self.label_family.grid_forget()

        self.entry_family = ttk.Entry(self.app)
        self.entry_family.grid(row=3, column=1)
        self.entry_family.grid_forget()

        self.label_nationalcode = ttk.Label(self.app, text='National Code',font=('arial', 15, 'bold'))
        self.label_nationalcode.grid(row=4, column=0)
        self.label_nationalcode.grid_forget()

        self.entry_nationalcode = ttk.Entry(self.app)
        self.entry_nationalcode.grid(row=4, column=1)
        self.entry_nationalcode.grid_forget()

        self.label_dateofbirth = ttk.Label(self.app, text='Date Of Birth',font=('arial', 15, 'bold'))
        self.label_dateofbirth.grid(row=5, column=0)
        self.label_dateofbirth.grid_forget()

        self.entry_dateofbirth = ttk.Entry(self.app)
        self.entry_dateofbirth.grid(row=5, column=1)
        self.entry_dateofbirth.grid_forget()    

        self.label_email = ttk.Label(self.app, text='E-mail', font=('arial', 15, 'bold'))
        self.label_email.grid(row=6, column=0)
        self.label_email.grid_forget()

        self.entry_email = ttk.Entry(self.app)
        self.entry_email.grid(row=6, column=1)
        self.entry_email.grid_forget()    

        self.label_password = ttk.Label(self.app, text='Password', font=('arial', 15, 'bold'))
        self.label_password.grid(row=7, column=0)
        self.label_password.grid_forget()

        self.entry_password = ttk.Entry(self.app)
        self.entry_password.grid(row=7, column=1)
        self.entry_password.grid_forget()  

        self.label_confirmpassword = ttk.Label(self.app, text='Confirm Password',font=('arial', 15, 'bold'))
        self.label_confirmpassword.grid(row=8, column=0)
        self.label_confirmpassword.grid_forget()

        self.entry_confirmpassword = ttk.Entry(self.app)
        self.entry_confirmpassword.grid(row=8, column=1)
        self.entry_confirmpassword.grid_forget()

        self.button_submit = ttk.Button(self.app, text = 'Submit', style = SUCCESS, command=self.login) #command = go next page
        self.button_submit.grid(row=6, column=1)
        self.button_submit.grid_forget()
        
        self.button_back_page3 = ttk.Button(self.app, text = 'Back', style = SUCCESS) #command = back to main page 
        self.button_back_page3.grid(row=6, column=1)
        self.button_back_page3.grid_forget()











        
    
        
        
        
        self.app.mainloop()
                
object = BankManagement()
