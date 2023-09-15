import pandas as pd 

def read_sheets(data, skip_rows, sheets_list):
    
    sheets = dict

    sheets = { sheet_name: pd.read_excel(data, sheet_name=sheet_name, skiprows=skip_rows) for sheet_name in list(sheets_list)}

    return sheets