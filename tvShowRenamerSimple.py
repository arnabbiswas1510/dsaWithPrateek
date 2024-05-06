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

files=r"X:\DSA by Kunal Kushwaha\*.mp4"
regex=re.compile("\d+")

fileList = glob.glob(files)
fileList.sort(key=natural_keys)
#print('\n'.join(fileList))
cnt=1
chkCnt=1
for file in fileList:
    if 'S01' not in file:
        f_name, f_ext = os.path.splitext(os.path.basename(file))
        f_dir=os.path.dirname(file)
        #if "S01E"+str(chkCnt) in f_name and chkCnt < 47:
        num = regex.findall(f_name)
        ind = re.search(r'\d.*\w', f_name).start() if re.search(r'\d.*\w', f_name) else 0
        n_name = "S01E"+ str(cnt) + " - "+f_name
        # if "Season" in f_name:
        #     n_name = "S01E"+ num[1] + " - Jai Mahalakshmi"
        # else:
        #     n_name = "S01E"+ num[0] + " - Jai Mahalakshmi"
        cnt+=1
        chkCnt+=1
        new_name = '{}/{}{}'.format(f_dir,n_name, f_ext)
        print('Rename - '+f_name+" -to- "+n_name)
        try:
            shutil.move(file, new_name) #This works across File Systems #Uncomment this line to execute the rename
            pass
        except:
            import sys
            print("Oops!", sys.exc_info()[0], "occurred.")