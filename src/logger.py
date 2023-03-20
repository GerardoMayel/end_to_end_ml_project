import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m-%d-%Y_%H-%M-%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    # best practice:
    format="[ %(asctime)s ] [ %(levelname)s ] [ %(name)s ] [ %(message)s ]",
    level=logging.INFO,
)

# Remove to make the logger tests:
# if __name__ == "__main__":
#     logging.info("Personilized Logger is working!")
