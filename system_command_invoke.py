import multiprocessing
import os
import os.path
import pathlib
import subprocess
import sys
from time import sleep

#  python command line :  http://takuya-1st.hatenablog.jp/entry/2016/04/11/044313 
# pathlib.Path("yourPathGoesHere").suffix



def func(cmd):
    proc = subprocess.Popen(cmd , shell=True)

def type2():
    
    processes = []
    tooladdr = "C:/Users/shikw/Downloads/ffmpeg-20180227-fa0c9d6-win64-static/ffmpeg-20180227-fa0c9d6-win64-static/bin/ffmpeg.exe"
    sourcedir = "C:/Users/shikw/Documents"
    curlist = os.listdir(sourcedir)
    mp4list = list(filter(lambda x: x.endswith(".mp4") or x.endswith(".mkv") , curlist))
    
    for i in range(0,len(mp4list)):
        filefullname = mp4list[i]
        fileinfo = os.path.splitext(mp4list[i])
        cmd = tooladdr+" -i {0} -b:v 32k {1}/{2}.mp3 ".format(os.path.join(sourcedir,filefullname),sourcedir, fileinfo[0])
        processes.append(multiprocessing.Process(target=func, args=(cmd,)))
    

    
    
    for process in processes:
        process.start() #Start the processes
    for process in processes:
        process.join()  #wait for each process to terminate  
    
    print("over....")


def type1():
    tooladdr = "C:/Users/shikw/Downloads/ffmpeg-20180227-fa0c9d6-win64-static/ffmpeg-20180227-fa0c9d6-win64-static/bin/ffmpeg.exe"
    sourcedir = "C:/Users/shikw/Documents"
    curlist = os.listdir(sourcedir)
    mp4list = list(filter(lambda x: x.endswith(".mp4") or x.endswith(".mkv") , curlist))
    
    for i in range(0,len(mp4list)):
        filefullname = mp4list[i]
        fileinfo = os.path.splitext(mp4list[i])
        cmd = tooladdr+" -i {0} -b:v 32k {1}/{2}.mp3 ".format(os.path.join(sourcedir,filefullname),sourcedir, fileinfo[0])
        proc = subprocess.Popen(cmd , shell=True)
        proc.wait()
    #     subprocess.run(cmd , shell=True)
    
    # sleep(50000)
if __name__ == '__main__':
    type2()
