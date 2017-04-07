#!/bin/bash
set -e
set -x
JQ="/usr/bin/jq -M"

if [ $# != 1 ]
then
	echo "Usage: $0 [export_file.json]" >&2
	exit 1
fi

i=0
while true
do
	obj="$($JQ ".[$i]" < "$1")"
	test "$obj" = "null" && break

	dir=$($JQ '._type' <<< "$obj" | tr -d \")
	filename=$dir/$($JQ '._id' <<< "$obj" | tr -d \").json

	echo $filename
	mkdir -p $dir
	$JQ '._source' <<< "$obj" > $filename
	i=$(($i + 1))
done
