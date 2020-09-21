#!/bin/bash
set -eu

read -p "enter full path to project folder : " folder
cd ${folder}

read -p "enter output file name : " output

ls -1 > tmp.txt
cat ./tmp.txt | while read line
do
  if test "${line}" = "${output}"; then
    echo -e "\033[31mERROR : A file with a name same to the one you specified in the output file already exists.\033[00m"
    rm tmp.txt
    exit 1
  fi
done

rsync -a --exclude-from .ignore --exclude '.ignore' ${folder}/* ${folder}/${output}
zip  ${output}.zip -r ${output}/*
rm -rf ${output}
