import logging   ##any execution happens we should able to log  all those information in txt file and track it
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  ## used notation and framework
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)   ## cwd-current working directory
os.makedirs(logs_path,exist_ok=True)       ## even if there is a file it will keep on showing
 
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(         ## to overwrite the functionaity or log
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s", ##this format mess will formed
    level=logging.INFO,


)

##if __name__=="__main__":                     ### to check everything working or not
##    logging.info("Logging has Started")