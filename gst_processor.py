from config import GST_RATE

def calculate_gst(df):
    df = df.copy()
    df['GST_Amount'] = df['Taxable_Value'] * GST_RATE
    df['CGST'] = df['GST_Amount'] / 2
    df['SGST'] = df['GST_Amount'] / 2
    df['Total_Invoice_Value'] = df['Taxable_Value'] + df['GST_Amount']
    return df

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