import logging   #Bot Created by @REACHING_STAR_OWNER
from logging.handlers import RotatingFileHandler   #Bot Created by @REACHING_STAR_OWNER
   #Bot Created by @REACHING_STAR_OWNER
logging.basicConfig(   #Bot Created by @REACHING_STAR_OWNER
    level=logging.ERROR,   #Bot Created by @REACHING_STAR_OWNER
    format=   #Bot Created by @REACHING_STAR_OWNER
    "%(asctime)s - %(levelname)s - %(message)s [%(filename)s:%(lineno)d]",   #Bot Created by @REACHING_STAR_OWNER
    datefmt="%d-%b-%y %H:%M:%S",   #Bot Created by @REACHING_STAR_OWNER
    handlers=[   #Bot Created by @REACHING_STAR_OWNER
        RotatingFileHandler("Assist.txt", maxBytes=50000000, backupCount=10),   #Bot Created by @REACHING_STAR_OWNER
        logging.StreamHandler(),   #Bot Created by @REACHING_STAR_OWNER
    ],   #Bot Created by @REACHING_STAR_OWNER
)   #Bot Created by @REACHING_STAR_OWNER
logging.getLogger("pyrogram").setLevel(logging.WARNING)   #Bot Created by @REACHING_STAR_OWNER
   #Bot Created by @REACHING_STAR_OWNER
   #Bot Created by @REACHING_STAR_OWNER
logging = logging.getLogger()   #Bot Created by @REACHING_STAR_OWNER
   #Bot Created by @REACHING_STAR_OWNER
