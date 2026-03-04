import requests
import pandas as pd

def fetch_erp_data():
    url = "https://fakestoreapi.com/products"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("ERP API Fetch Failed")

    df = pd.DataFrame(response.json())

    df.rename(columns={
        'id': 'Invoice_No',
        'price': 'Taxable_Value',
        'category': 'HSN_Category'
    }, inplace=True)

    return df[['Invoice_No', 'Taxable_Value', 'HSN_Category']]