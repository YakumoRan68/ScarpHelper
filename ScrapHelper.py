import io
import re
from os import listdir
from os.path import isfile, join

INPUT_DIRECTORY = "./input"
OUTPUT_DIRECTORY = "./output"

files = [f for f in listdir(INPUT_DIRECTORY) if isfile(join(INPUT_DIRECTORY, f))]

for filename in files :
    Document = ""
    with io.open(INPUT_DIRECTORY + "/" + filename, 'r', encoding = 'utf-8') as file:
        Document = file.read()
        
    with io.open(OUTPUT_DIRECTORY + "/" + filename, 'w+', encoding = 'utf-8') as file :
        filter_keywords = re.compile("\[\d*\]")

        output = re.sub(filter_keywords, '', Document)

        file.write(output)
    
