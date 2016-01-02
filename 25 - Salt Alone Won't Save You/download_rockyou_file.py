import urllib.request
import shutil

# http://stackoverflow.com/a/7244263/3281097

url = "http://scrapmaker.com/data/wordlists/dictionaries/rockyou.txt"
file_name = url.split("/")[-1]

# Download the file from `url` and save it locally under `file_name`:
with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
    shutil.copyfileobj(response, out_file)
