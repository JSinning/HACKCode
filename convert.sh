#!/bin/bash

for code64 in $1 ;do

      echo $code64 | base64 -d; echo
done
