'''
This script loads the data into the Google Sheet.
'''

import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
from gspread_dataframe import set_with_dataframe

# Configurações de autenticação
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = Credentials.from_service_account_file('credentials.json', scopes=scope)
client = gspread.authorize(creds)

# Lendo dados do Excel
data = pd.read_excel('oil_data.xlsx')

# Abrindo a planilha (cria uma nova se não existir)
spreadsheet = client.open_by_key('1HsxwfeZA4Dh_K_0slyt0xda-1rKfyTE3jxomgv39tUw')
sheet = spreadsheet.get_worksheet(1)

# Carregando dados no Google Sheets
set_with_dataframe(sheet, data)

# Obtendo e imprimindo a URL da planilha
spreadsheet_url = f"https://docs.google.com/spreadsheets/d/{sheet.spreadsheet.id}"
print(spreadsheet_url)