import logging
import os
from datetime import datetime

# Create logs directory if it doesn't exist
os.makedirs('logs', exist_ok=True)

# Set up logging configuration
log_filename = datetime.now().strftime('logs/log_%Y-%m-%d.log')
logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
