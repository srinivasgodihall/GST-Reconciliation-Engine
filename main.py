from logger_config import setup_logger
from api_handler import fetch_erp_data
from gst_processor import calculate_gst
from reconciliation import generate_gstr2a, reconcile
from validator import validate
from report_generator import generate_report

def main():
    setup_logger()

    erp_data = fetch_erp_data()
    validate(erp_data)

    erp_processed = calculate_gst(erp_data)

    gstr2a_data = generate_gstr2a(erp_processed)

    reconciliation_df = reconcile(erp_processed, gstr2a_data)

    generate_report(reconciliation_df)

    print("Enterprise GST Reconciliation Completed")

if __name__ == "__main__":
    main()