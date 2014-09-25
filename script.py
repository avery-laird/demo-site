import argparse
import os 
from subprocess import call
import subprocess
FNULL = open(os.devnull, 'w')
skipped = 0
exists = 0
nexists = 0
ex = open('exists.txt', 'r+')
with open('requirements.txt', 'r+') as f:
    for package in f:
        if '#' in package:
	    print ("Skipping " + str(package))
            skipped = skipped + 1
        else:
            l = package.partition('=')[0]
            query = subprocess.Popen(['pip', 'install', l], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            d, e = query.communicate()
            if "Could not find any downloads that satisfy the requirement" in d:
                print("[" + str(l) + "]---> Does not exist in PyPi")
                nexists = nexists + 1
            elif "Successfully installed" in d:
                print("[" + str(l) + "]---> Does exist in PyPi")
                print("Successfully installed " + str(package))
                ex.write(package)
                exists = exists + 1
            elif "Requirement already satisfied" in d:
                print("[" + str(l) + "]---> Does exist in PyPi")
                print(str(d))
                ex.write(package)
                exists = exists + 1
            else:
                print("unknown error. Here's what I've got: " + str(d) + str(e))

print(str(skipped) + " Skipped")
print(str(exists) + " Exist")
print(str(nexists) + " Don't Exist")
