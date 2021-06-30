import pandas as pds
excel_file = 'SOFTSKILLS1.xls'

excel_data_df = pds.read_excel('SOFTSKILLS1.xls')

# print whole sheet data
print(excel_data_df)