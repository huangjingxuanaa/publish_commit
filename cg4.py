
import pandas as pd
import random
import os

if __name__ == '__main__':
    file = open('./comments.txt','r')
    username = 'qinding01';
    email = 'qinding01@cmpanda.com';
    lines = file.readlines()
    starttime = '2021-1-20'
    endtime = '2021-1-30'
    file_list = [
       './add.js'     
    ]
    new_file_list = [
        './cg6.py'
    ]
    os.system('git config --global user.name "'+username+'"')
    os.system('git config --global user.email "'+email+'"')
    e = pd.bdate_range(starttime, endtime,freq='b')
    for riqi in e:
       system_time = (str(riqi.date()))+' '+str(random.randint(10,18))+':'+str(random.randint(10,60))+':'+str(random.randint(10,60))
       comment = lines[random.randint(1,3729)]
       oldfile = open(file_list[random.randint(0,len(file_list)-1)],'r')
       oldfilelines = oldfile.readlines()
       oldfl = len(oldfilelines)
       resultList = random.sample(range(0, oldfl), random.randint(1,8))
       newfile = open(new_file_list[random.randint(0,len(new_file_list)-1)],'a+')
       for l in resultList:
           newfile.write(oldfilelines[l])
       oldfile.close()
       newfile.close()
       os.system('timedatectl set-time "'+system_time+'"')
       os.system('git pull')
       os.system('git add .')
       os.system('git commit -a -m '+comment)
       os.system('git push origin master')

