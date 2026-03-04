# import streamlit as st
# import pandas as pd
# from api_handler import fetch_erp_data
# from gst_processor import calculate_gst
# from reconciliation import generate_gstr2a, reconcile

# st.title("GST Reconciliation Dashboard")

# gst_rate = st.slider("Select GST Rate", 0.05, 0.28, 0.18)

# if st.button("Run Reconciliation"):

#     erp_data = fetch_erp_data()
#     erp_processed = calculate_gst(erp_data)

#     gstr2a_data = generate_gstr2a(erp_processed)
#     recon_df = reconcile(erp_processed, gstr2a_data)

#     st.subheader("Reconciliation Data")
#     st.dataframe(recon_df)

#     st.subheader("Mismatch Summary")
#     st.metric("Total Mismatches", recon_df['Mismatch_Flag'].sum())

#     st.bar_chart(
#         recon_df.groupby('HSN_Category_ERP')['GST_Amount_ERP'].sum()
#     )


import streamlit as st
import pandas as pd
from api_handler import fetch_erp_data
from gst_processor import calculate_gst
from reconciliation import generate_gstr2a, reconcile

st.set_page_config(page_title="GST Reconciliation Engine", layout="wide")

st.title("Enterprise GST Reconciliation Dashboard")

gst_rate = st.slider("Select GST Rate", 0.05, 0.28, 0.18)

if st.button("Run Reconciliation"):

    erp_data = fetch_erp_data()
    erp_processed = calculate_gst(erp_data)

    gstr2a_data = generate_gstr2a(erp_processed)
    recon_df = reconcile(erp_processed, gstr2a_data)

    total_invoices = len(recon_df)
    total_mismatches = recon_df['Mismatch_Flag'].sum()
    total_difference = recon_df['Difference'].sum()

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Invoices", total_invoices)
    col2.metric("Total Mismatches", total_mismatches)
    col3.metric("Net Tax Difference", round(total_difference, 2))

    st.subheader("Reconciliation Data")
    st.dataframe(recon_df)

    st.subheader("GST by Category")
    st.bar_chart(
        recon_df.groupby('HSN_Category_ERP')['GST_Amount_ERP'].sum()
    )