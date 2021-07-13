import os
from BackEnd.settings import BASE_DIR
AFL_PATH = os.path.join(BASE_DIR,"tools/AFL-2.57b")
TORTOISE_PATH = os.path.join(BASE_DIR,"tools/TortoiseFuzz")
MEM_AFL_PATH = os.path.join(BASE_DIR,"tools/afl-2.52b")

MAX_TIMES = 30          # 24h

                        # fuzz's config for time & mem
TIMEOUT = 1000
MEMSIZE = 1000
ANDAND ="&&"
