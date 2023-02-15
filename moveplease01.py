#!/usr/bin/env python3

#Importing additional code to run the script.
import shutil
import os

def main():
    #Start in the home directory.
    os.chdir('/home/student/mycode/')

    #moving rayno.obj to ceph_storage
    shutil.move('raynor.obj', 'ceph_storage/')

    #Pause program while we prompt the user for kerrigan.obj's new name. 
    xname = input('What is the new name for kerrigan.obj? ') # collects string
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname) #moves file and renames it with user input. 


main() #calls main function
