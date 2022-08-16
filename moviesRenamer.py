import glob, re, os, shutil

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

files="/Volumes/Media/English Movies/BS_WITH_TH_COMPLETE/*.avi"
regex=re.compile("\d+")

fileList = glob.glob(files)
fileList.sort(key=natural_keys)
#print('\n'.join(fileList))
cnt=1
chkCnt=1
for file in fileList:
    f_name, f_ext = os.path.splitext(os.path.basename(file))
    f_dir=os.path.dirname(file)
    num = regex.findall(f_name)
    matches = [(m.start(0), m.end(0), f_name) for m in re.finditer("\d+", f_name)]
    if len(matches) == 2:
        n_name = f_name[:matches[1][0]]+'pt'+f_name[matches[1][0]:]
        new_name = '{}/{}{}'.format(f_dir,n_name, f_ext)
        print('Rename - '+f_name+" -to- "+n_name)
        shutil.move(file, new_name) #This works across File Systems #Uncomment this line to execute the rename