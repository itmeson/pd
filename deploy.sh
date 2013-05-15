#!/bin/bash

if [ $# -ne 1 ]; 	then

	echo 'need directory to deploy, relative to application base'
	exit 1
fi
rsync -avz $1/ user@host.com:~/webapps/web2py/web2py/applications/courselib/$1
