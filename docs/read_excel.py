import openpyxl

wb = openpyxl.load_workbook('mapping_emails.xlsx')
ws = wb.active

print('Sheet name:', ws.title)
print('Dimensions:', ws.dimensions)
print('\nFirst 10 rows:')
for i, row in enumerate(ws.iter_rows(values_only=True), 1):
    print(row)
    if i >= 10:
        break
