#!/bin/bash

function tfrecord2hash()
{
  for i in $@; do
    mv "${i}" "frame-$(sha512sum ${i} | awk '{print $1}' | cut -c -32).tfrecord"
  done
}

if [ -d "$1" ]; then
  echo "cd $1"
  cd "$1"
else
  echo "give a directory name"
fi

tfrecord2hash *.tfrecord
