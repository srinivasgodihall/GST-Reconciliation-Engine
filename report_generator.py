# import pandas as pd
# from datetime import datetime

# def generate_report(recon_df):

#     timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#     file_name = f"output/GST_Reconciliation_{timestamp}.xlsx"

#     summary = recon_df[['Difference']].sum()

#     mismatches = recon_df[recon_df['Mismatch_Flag'] == True]

#     with pd.ExcelWriter(file_name, engine='xlsxwriter') as writer:
#         recon_df.to_excel(writer, sheet_name='Reconciliation_Data', index=False)
#         summary.to_frame(name='Total_Difference').to_excel(writer, sheet_name='Summary')
#         mismatches.to_excel(writer, sheet_name='Exceptions', index=False)


import pandas as pd
from datetime import datetime

def generate_report(recon_df):

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"output/GST_Reconciliation_{timestamp}.xlsx"

    summary = recon_df[['Difference']].sum()
    mismatches = recon_df[recon_df['Mismatch_Flag'] == True]
    category_summary = recon_df.groupby('HSN_Category_ERP')['GST_Amount_ERP'].sum()

    with pd.ExcelWriter(file_name, engine='xlsxwriter') as writer:
        recon_df.to_excel(writer, sheet_name='Reconciliation_Data', index=False)
        summary.to_frame(name='Total_Difference').to_excel(writer, sheet_name='Summary')
        mismatches.to_excel(writer, sheet_name='Exceptions', index=False)
        category_summary.to_frame(name='GST_By_Category').to_excel(writer, sheet_name='Category_Summary')

        workbook = writer.book
        worksheet = writer.sheets['Category_Summary']

        chart = workbook.add_chart({'type': 'column'})

        chart.add_series({
            'name': 'GST by Category',
            'categories': ['Category_Summary', 1, 0, len(category_summary), 0],
            'values': ['Category_Summary', 1, 1, len(category_summary), 1],
        })

        chart.set_title({'name': 'GST Distribution by Category'})
        worksheet.insert_chart('D2', chart)