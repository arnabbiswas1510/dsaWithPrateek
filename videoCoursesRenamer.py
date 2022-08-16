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

path=r"X:\The Complete 2018 Mind Mapping Step-By-Step Mastery Course"
regex=re.compile("\d+")
sCnt=1


def has_sequence(this_parent):
    mp4 = this_parent+"/*.mp4"
    avi = this_parent+"/*.avi"
    files = glob.glob(mp4)
    if not files:
        files = glob.glob(avi)
    prevCnt=None
    if files and len(files) > 1:
        files.sort(key=natural_keys)
        for file in files:
            file = os.path.basename(file)
            thisCnt= int(re.search(r'\d+', file).group()) if re.search(r'\d+', file) else 0
            if prevCnt and thisCnt != (prevCnt+1):
                return False
            else:
                prevCnt = thisCnt
        return True
    return False

def s_cnt(this_parent):
    return re.search(r'\d+', this_parent).group() if re.search(r'\d+', this_parent) else -1

def e_cnt(file):
    m = re.search(r'(\d+)\W+', file)
    if m:
        return m.start(), m.end(), m.group(1)
    else:
        return -1,-1,-1

def adjustForLength(path):
    if len(path) > 255:
        return '\\\\?\\' + path
    else:
        return path

prev_parent=None
sCnt=1

for dirpath, dirnames, filenames in os.walk(path):
    eCnt=0
    filenames.sort(key=natural_keys)
    seq_from_files=False
    for filename in filenames:
        if any(ext in filename for ext in ('mp4', 'avi', 'srt', 'm4v', 'MP4')) and not filename.startswith("."):
            full_path = os.path.join(dirpath, filename)
            this_parent = str(Path(full_path).parent)
            if not prev_parent:
                prev_parent = this_parent
            elif prev_parent != this_parent:
                prev_parent = this_parent
                seq_from_files = has_sequence(this_parent)
                #print(this_parent+", has seq:"+str(seq_from_files))
                this_parent=os.path.basename(this_parent)
                if s_cnt(this_parent) != -1:
                    sCnt = s_cnt(this_parent)
                else:
                    sCnt += 1
            f_name, f_ext = os.path.splitext(os.path.basename(filename))
            s,e,e_Cnt=e_cnt(f_name)
            if s != -1:
                eCnt = e_Cnt
            else:
                eCnt=int(eCnt)+1
            new_path = os.path.join(dirpath, 'S'+str(sCnt)+'E'+str(eCnt)+'--'+f_name+f_ext)
            full_path=adjustForLength(full_path)
            new_path=adjustForLength(new_path)
            print(full_path + " - to - "+ new_path)
            shutil.move(full_path, new_path)
