import os 
import sys 
import logging 


# Log format
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Log directory 
log_dir = "log"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

# Logging setup 
logging.basicConfig(
    level= logging.INFO,
    format= logging_str,
    handlers= [
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("CNNClassifierLogger")