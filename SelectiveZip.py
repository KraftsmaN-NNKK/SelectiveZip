import os
import shutil
import glob
import sys

work_dir = input("enter full path to project folder : ")
os.chdir(work_dir)

output_name = input("enter output file name : ")

files = glob.glob("*")
for file in files:
    if file == output_name:
        print("\033[31mERROR : A file with a name same to the one you specified in the output file already exists.\033[0m")
        sys.exit()

if os.path.isfile(".ignore") == False:
    print("\033[31mERROR : can not find the file:'.ignore'.\033[0m")
    sys.exit()

shutil.copytree("./", "./" + output_name)
os.remove("./" + output_name + "/" + ".ignore")

line = open(".ignore", "r").readline()
while line:
    line = line.strip()
    if line[:1] == "/":
        os.rmtree("./" + output_name + line)
    
    else
        os.remove("./" + output_name + line)

    line = open(".ignore", "r").readline()

shutil.make_archive('./' + output_name, 'zip', root_dir= './' + output_name)

shutil.rmtree("./" + output_name)