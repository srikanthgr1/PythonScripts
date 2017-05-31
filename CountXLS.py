from win32com.client import Dispatch

xl= Dispatch("Excel.Application")
xl.Visible = True 

wb = xl.Workbooks.Open(r'c:\users\....')
print "Numero di fogli:", wb.Sheets.Count
for sh in wb.Sheets:
    print sh.Name
wb.Close()
xl.Quit()

#python count.py
