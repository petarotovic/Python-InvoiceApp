import tkinter as tk
from tkinter import ttk

#create root app (window)
rootApp = tk.Tk()
rootApp.title("Ottoshop")
rootApp.geometry("300x450")

invoiceDialogObj = None

def showInvoiceDialog():
    from invoice import invoiceDialog
    global invoiceDialogObj
    invoiceDialogObj = invoiceDialog(rootApp)
    invoiceDialogObj.renderDialog()

financialDialogObj = None

def showFinancialDialog():
    from financialreport import FinancialDialog
    global financialDialogObj
    financialDialogObj = FinancialDialog(rootApp)
    financialDialogObj.showDialog()

addCompanyDialogObj = None

def showAddCompanyDialog():
    from addcompany import addCompanyDialog
    global addCompanyDialogObj
    addCompanyDialogObj = addCompanyDialog(rootApp)
    addCompanyDialogObj.showAddCompanyDialog()

addClientDialogObj = None

def showAddClientDialog():
    from addclient import addClientDialog
    global addClientDialogObj
    addClientDialogObj = addClientDialog(rootApp)
    addClientDialogObj.renderDialog()

def closeApp():
    rootApp.quit()                                                               
#change window icon
icon = tk.PhotoImage(file='./content/logo.png')
rootApp.wm_iconphoto(True, icon)
# #create each button on starting form
ttk.Button(rootApp, text='Fakturisanje', command=showInvoiceDialog, width=20).pack(padx=30, pady=10)
ttk.Button(rootApp, text='Finansijski Izvestaj', command=showFinancialDialog, width=20).pack(padx=30, pady=10)
ttk.Button(rootApp, text='Bar Kodovi', command=showInvoiceDialog, width=20).pack(padx=30, pady=10)
ttk.Button(rootApp, text='Etikete', command=showInvoiceDialog, width=20).pack(padx=30, pady=10)
ttk.Button(rootApp, text='Dodaj Firmu', command=showAddCompanyDialog, width=20).pack(padx=30, pady=10)
ttk.Button(rootApp, text='Dodaj Klijenta', command=showAddClientDialog, width=20).pack(padx=30, pady=10)
ttk.Button(rootApp, text='Dodaj Proizvod', command=showInvoiceDialog, width=20).pack(padx=30, pady=10)
ttk.Button(rootApp, text='Izmeni Proizvod', command=closeApp, width=20).pack(padx=30, pady=10)
ttk.Button(rootApp, text='Izadji', command=closeApp, width=10).pack(padx=30, pady=30)

# #initiate main form
rootApp.mainloop()