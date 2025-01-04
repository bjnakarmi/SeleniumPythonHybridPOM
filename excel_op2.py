# Creating a new workbook.

from openpyxl import Workbook, load_workbook

wb = Workbook()
ws = wb.active
ws.title = 'Data'

ws.append(['This', 'Is', 'A', 'Test'])
ws.append(['This', 'Is', 'Another', 'Test'])
ws.append(['This', 'Is', '3rd', 'Test'])

wb.save('Test.xlsx')