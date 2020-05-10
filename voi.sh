#!/bin/bash

no_args="true"
OPTIND=1
while getopts ":hv" opt; do
	case $opt in
		h)
			echo "Prints options today from (large) list which have unusual volume/(open interest)"
			echo "Usage: voi.sh [-option]"
			echo -e "-h\t\t Help"
			echo -e "-v\t\t Verbose. Prints the options themselves in addition to the stocks."
			no_args="false"
			;;
		v)
			py voiratio.py asdfdsfa
			no_args="false"
			;;
	esac
done
if [ $no_args = "true" ] ; then
	py voiratio.py
fi

