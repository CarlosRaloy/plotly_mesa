import os
from dotenv import load_dotenv
load_dotenv()


vars = os.getenv('USER_DB')

print(vars)