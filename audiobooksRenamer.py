"""
Requirements:
1. Return tuple with start index and end index of numbers in file if each file has a sequence of numbers in folder
2. If no sequence return -1, -1 and dont modify filename, just add count to E number
"""
import glob, re, os, shutil
from pathlib import Path

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

path=r"Z:\Kenneth Wapnick Audio Workshops (ACIM)"
regex=re.compile("\d+")
sCnt=1

def adjustForLength(path):
    if len(path) > 255:
        return '\\\\?\\' + path
    else:
        return path

track=0

for dirpath, dirnames, filenames in os.walk(path):
    filenames.sort(key=natural_keys)
    seq_from_files=False
    for dirname in dirnames:
        mp3 = dirpath+'/'+dirname+"/*.mp3"
        files = glob.glob(mp3)
        if files:
            print("cd " + dirpath+"\\"+dirname)
            print("mp3wrap " + dirname+".mp3 *.mp3")
