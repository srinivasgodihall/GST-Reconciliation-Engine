def validate(df):
    if df.isnull().values.any():
        raise ValueError("Null values detected")

    if (df['Taxable_Value'] < 0).any():
        raise ValueError("Negative taxable values detected")

    return True