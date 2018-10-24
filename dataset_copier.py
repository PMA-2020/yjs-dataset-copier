"""YJ's Dataset Grabber
Grabs files that look like the following:
- PMA2015_CDR4_Kinshasa_HHQFQ_v3_20Aug2018.dta
- PMA2015_ETR5_HHQFQ_v3_20Aug2018.dta
Saves somewhere else as:
- CDR4_HHQFQ.dta
- ETR5_HHQFQ.dta"""
import glob
import re
import shutil
import os.path
# temp = []
 
for name in glob.glob(r"C:\\Users\\YoonJoung Choi\\Dropbox (Gates Institute)\\PMA*_Datasets\\Round*\\Final*\\HH*\\*\\*.dta"):
    # Get the file name only, without directory path
    filename = os.path.split(name)[1]
    search = r"(PMA20\d\d_)(.*?)(_.*)"
    hhqfq = "_HHQFQ"
    dta = ".dta"
    find = re.search(search,filename)
    if find:
        rename = r"C:\\Users\\YoonJoung Choi\\Dropbox (Gates Institute)\\ychoi\\PMA\\PMAdata_YJ\\rawHHQFQ\\" + find.group(2)+ hhqfq+ dta
        # temp.append(rename)
        # shutil.copy(name,rename)
 
# from pdb import set_trace; set_trace()
