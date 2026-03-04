import pandas as pd
import random

def generate_gstr2a(df):
    gstr2a = df.copy()

    # Introduce artificial mismatches
    for i in range(len(gstr2a)):
        if random.random() < 0.2:
            gstr2a.loc[i, 'Taxable_Value'] *= random.uniform(0.9, 1.1)

    return gstr2a


def reconcile(erp_df, gstr2a_df):

    merged = erp_df.merge(
        gstr2a_df,
        on='Invoice_No',
        suffixes=('_ERP', '_GSTR2A')
    )

    merged['Difference'] = (
        merged['Taxable_Value_ERP'] -
        merged['Taxable_Value_GSTR2A']
    )

    merged['Mismatch_Flag'] = merged['Difference'].abs() > 5

    return merged