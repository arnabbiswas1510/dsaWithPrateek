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

files="/Volumes/Media/Religious Videos/SRI KRISHNA/*.avi"
regex=re.compile("\d+")

fileList = glob.glob(files)
fileList.sort(key=natural_keys)
#print('\n'.join(fileList))
cnt=1
chkCnt=1
for file in fileList:
    f_name, f_ext = os.path.splitext(os.path.basename(file))
    f_dir=os.path.dirname(file)
    #if "S01E"+str(chkCnt) in f_name and chkCnt < 47:
    num = regex.findall(f_name)
    #ind = re.search(r'\d \w', f_name).start()
    #n_name = "S01E"+ num[0] + " - Sri Krishna - "+f_name[ind+2:]
    n_name = "S01E"+ num[0] + " - Sri Krishna"
    cnt+=1
    chkCnt+=1
    new_name = '{}/{}{}'.format(f_dir,n_name, f_ext)
    print('Rename - '+f_name+" -to- "+n_name)
    shutil.move(file, new_name) #This works across File Systems #Uncomment this line to execute the rename