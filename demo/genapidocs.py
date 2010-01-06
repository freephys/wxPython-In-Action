#coding: UTF8
"""
Generate API documentation for the project
"""

import os
import subprocess

NAME = "AgileDevelopment" # DRY violation!
DOT_PATH = os.path.abspath("C:\Program Files\Graphviz2.24\bin\dot.exe")

def clean_dir(directory):
    """Remove all prior fields from the directory"""

    print "Cleaning directory", directory
    from os.path import join
    for root, dirs, files in os.walk(directory, topdown=False):
        for name in files:
            os.remove(join(root, name))
        for name in dirs:
            os.rmdir(join(root, name))
            
def run_command(command):
    """Runs the command line, asserts success"""

    proc = subprocess.Popen(command,
                            shell=True, 
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE
                           )

    for line in proc.stdout:
        print line.strip()

    for line in proc.stderr:
        print line.strip()

    assert not proc.returncode
def gen_api_docs():
    """Generates documentation files"""
    
    print
    print "*" * 30
    print "Generating documentation..."
    base_dir = os.path.dirname(__file__)
    api_dir = os.path.join(base_dir, "apidocs")
    
    # Get rid of the old documentation
    clean_dir(api_dir)
    
    os.chdir(base_dir)

    run_command(' '.join([r'python C:\Python25\Scripts\epydoc.py',
                               '--html',
                               '-v',
                               r'-o "%s"' % api_dir,
                               '--name=%s' % NAME,
                               '--graph all',
                               r'--dotpath "%s"' % DOT_PATH,
                               '--top=TestProject.main',
                               r'"%s"' % base_dir]))

    print "Finished generating documentation!"
    print "*" * 30
    print

if __name__ == "__main__":
    gen_api_docs()