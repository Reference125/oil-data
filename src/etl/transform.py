"""
This module contains the functions that transform the data from the raw format to the
format that is ready to be loaded into the database.


Sample raw data (JSON file):
{
    "response": {
        "warnings": [
            {
                "warning": "incomplete return",
                "description": "The API can only return 5000 rows in JSON format.  Please consider constraining your request with facet, start, or end, or using offset to paginate results."
            }
        ],
        "total": "24596",
        "dateFormat": "YYYY-MM",
        "frequency": "monthly",
        "data": [
            {
                "period": "2024-05",
                "duoarea": "NUS",
                "area-name": "U.S.",
                "product": "EPC0",
                "product-name": "Crude Oil",
                "process": "YCG",
                "process-name": "Refinery Inputs, Average API Gravity",
                "series": "MCRAPUS2",
                "series-description": "U.S. API Gravity (Weighted Average) of Crude Oil Input to Refineries (Degrees)",
                "value": "33.3",
                "units": "D"
            }
        ]
    },
    "request": {
        "command": "/v2/petroleum/pnp/crq/data/",
        "params": {
            "frequency": "monthly",
            "data": [
                "value"
            ],
            "facets": [],
            "start": null,
            "end": null,
            "sort": [
                {
                    "column": "period",
                    "direction": "desc"
                }
            ],
            "offset": 0,
            "length": 1
        }
    },
    "apiVersion": "2.1.7",
    "ExcelAddInVersion": "2.1.0"
}
"""
import json
import pandas as pd

# Carregar os dados do arquivo JSON
with open('oil_data.json', 'r') as file:
    json_data = json.load(file)

# Extrair os dados da resposta
data = json_data['response']['data']

# Criar um DataFrame a partir dos dados
df = pd.DataFrame(data)

# Salvar o DataFrame em um arquivo Excel
df.to_excel('oil_data.xlsx', index=False)
