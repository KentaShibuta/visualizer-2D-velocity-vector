#!/bin/sh
echo ファイルのパスを入力:
read input_file_name
output_file_name=`date +"%Y%m%d%H%M%S"`
f_name_crd='_interface'
f_name_v='_v'
awk '/# interface_start/,/# interface_end/' $input_file_name|awk '! /^#/'|awk 'BEGIN{OFS=","} {print $2, $3}'>$output_file_name$f_name_crd.csv
