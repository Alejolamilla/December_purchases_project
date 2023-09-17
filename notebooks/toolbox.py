import pandas as pd 

def read_sheets(data, skip_rows, sheets_list):
    
    sheets = {}
    #sheets = { sheet_name: pd.read_excel(data, sheet_name=sheet_name, skiprows=skip_rows) for sheet_name in list(sheets_list)}
    for sheet_name in list(sheets_list):
        
        df = pd.read_excel(data, sheet_name=sheet_name, skiprows=skip_rows)
        df["SHEET"] = sheet_name

        sheets[sheet_name] = df

    return sheets
