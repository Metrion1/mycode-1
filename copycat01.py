#!/usr/bin/env python3
"""W.Pfau | TLG Learning
   Moving stuff around using shutil and os from the standard library"""

#Importaing additional code to complete task.
import shutil
import os


def main():
    #Force python to start in home directory.
    os.chdir("/home/student/mycode/")


    # Copy a file to make a duplicate. 
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

    # Copy a "5G Research" directory to make a back up called "5g_research_backup/"
    os.system("rm -rf /home/student/mycode/5g_research_backup/")
    shutil.copytree("5g_research/", "5g_research_backup/")

main()
