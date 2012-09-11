#!/usr/bin/env python
import subprocess
    
    
    
def git_default():
    subprocess.call(['git','add','.'])
    subprocess.call(['git','commit','-m','"update"'])
    subprocess.call(['git','push','origin','master'])
    
def git_options():
    pass
    
    
def input():
    x = raw_input("To use default config press enter. Else type 1.")
    if x:
        git_options()
    else:
        git_default()
        
        
        
if __name__ == "__main__":
    input()
    