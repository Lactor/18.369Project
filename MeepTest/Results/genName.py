import sys
import os

pre = sys.argv[1]
n = sys.argv[2]
field = sys.argv[3]

S =  "h5topng -RZc dkbluered -C "+pre+"-eps-"+n+"*.h5 " + pre+"-"+field+"-" + n + "*.h5; convert " + pre + "-" + field + "-" + n + "*.png " + pre + "-"+field + ".gif; rm *.png; eog " + pre + "-"+field + ".gif;"

print S
os.system(S)
