import win32com.client
#import shutil
import win32com.client as win32
# Begin communication with Excel
Xlsx = win32.DispatchEx('Excel.Application')

# Launch Excel
Xlsx.DisplayAlerts = True
Xlsx.Visible = True

# Load file (change path to where the spreadsheet is located)
book = Xlsx.Workbooks.Open('path\\to\\excel\\sheet')

# Refresh the spreadsheet from DrillingInfo
book.RefreshAll()

# Not exactly sure what this does, but don't delete it
Xlsx.CalculateUntilAsyncQueriesDone()

# Save the updated spreadsheet and close the file, then quit Excel
book.Save()
book.Close()
Xlsx.Quit()
del book
del Xlsx
print("Finished excel")

