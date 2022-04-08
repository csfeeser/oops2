#!/usr/bin/env python3

# standard library imports
import shutil   # shell utilities will be used to move files
import os       # provies access to low level os operations (agnostic to flavor of OS)

def main():
    os.chdir('/home/student/mycode/')   # move into this working directory
    shutil.move('raynor.obj', 'ceph_storage/')  # try moving the file raynor.obj into ceph_storage/ dir

    # program will pause while we accept input
    xname = input('What is the new name for kerrigan.obj? ') # collect string input from the user
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)  # moving kerrigan.obj into
                                                                       # ceph_storage/ with new name


main() # this calls our main function
