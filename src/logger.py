#This file contains info for log file
'''
A log file is a text file where a program records information about its operations while it’s running. It's mainly used for:

 Tracking what the program is doing

 Debugging errors or issues

 Monitoring performance or activity

 Recording important events for security or audits

 Imagine your program is writing a diary entry every time something important happens. For example:

"Started running at 3:00 PM"

"User clicked the button"

"Error: Could not connect to database"

"Completed task successfully"
'''
import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
'''This creates a log file name using the current date and time.

    Example output: "04_16_2025_14_32_10.log"'''

#create path for logs
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
#create path for log directory
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)

#To check if we have successfully done the task of logging
'''
if __name__=="__main__":
    logging.info("Logging has started")
    '''


