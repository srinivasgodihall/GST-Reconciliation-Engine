import logging

def setup_logger():
    logging.basicConfig(
        filename='gst_engine.log',
        level=logging.INFO,
        format='%(asctime)s | %(levelname)s | %(message)s'
    )
    logging.info("GST Reconciliation Engine Started")