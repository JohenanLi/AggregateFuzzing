import os
from BackEnd.settings import BASE_DIR
AFL_PATH = os.path.join(BASE_DIR,"/tools/aflGithub")
TORTOISE_PATH = os.path.join(BASE_DIR,"/tools/TortoiseFuzz")
EMEM_AFL_PATH = os.path.join(BASE_DIR,"/tools/afl")

MAX_TIMES = 30          # 24h

                        # fuzz's config for time & mem
TIMEOUT = 1000
MEMSIZE = 1000

