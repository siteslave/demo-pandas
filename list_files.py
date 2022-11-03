import os
from zipfile import ZipFile
import string
import random

path = "./tmp"
dir_list = os.listdir(path)

for x in os.listdir(path):
    if x.endswith(".zip"):
        # print(os.path.abspath(x))
        zip_file = os.path.join(path, os.path.basename(x))
        with ZipFile(zip_file, 'r') as myzip:
            letters = string.ascii_lowercase
            str_random = ''.join(random.choice(letters) for i in range(10))
            tmp_path = os.path.join("extract", str_random)
            myzip.extractall(tmp_path)
