import multiprocessing as mp
import subprocess
import os
import math


cmd_get_video = "ls /dev/* | grep video"
proc = subprocess.Popen(cmd_get_video, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
ret, error = proc.communicate()

video_list = ret.decode('utf8').rstrip('\n').split('\n')

if len(video_list) == 0:
    print('no video available')
    exit(1)

def sleep(i):
    cmd = './sleep5.sh'
    print('start', i)
    subprocess.check_output(cmd)
    return 'test'

def capture(device):
    output = 'tmp/' + os.path.basename(device) + '.jpg'
    cmd = 'fswebcam -q -S 20 --no-banner -d %s %s' % (device, output)
    print('start: ', cmd)
    return subprocess.call(cmd.split(" "))

cpu_count = mp.cpu_count()
proc = cpu_count * math.ceil(len(video_list) / cpu_count)
pool = mp.Pool(proc)

# callback = pool.map(sleep, video_list)
callback = pool.map(capture, video_list)
print(callback)
