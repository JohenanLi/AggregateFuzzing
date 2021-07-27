import os
from BackEnd.settings import BASE_DIR
AFL_PATH = os.path.join(BASE_DIR,"tools/AFL-2.57b")
TORTOISE_PATH = os.path.join(BASE_DIR,"tools/TortoiseFuzz")
MEM_AFL_PATH = os.path.join(BASE_DIR,"tools/memAfl")
COLL_PATH = os.path.join(BASE_DIR,"tools/collafl-master")
AFLPLUSPLUS_PATH = os.path.join(BASE_DIR,"tools/AFLPLUSPLUS")
DRILLER_PATH = os.path.join(BASE_DIR,"tools/driller")

MAX_TIMES = 30          # 24h

                        # fuzz's config for time & mem
TIMEOUT = 1000
MEMSIZE = 1000
ANDAND ="&&"
