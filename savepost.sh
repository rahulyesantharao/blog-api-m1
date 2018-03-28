#!/bin/sh

if [ $# -eq 2 ]; then
  if [ ! -f "post_converter/md_posts/$1.md" ]; then
    echo "The specified file '$1.md' does not exist"
    exit 1
  fi
else
  echo "Usage $0 [post<#>] [<\"Title\">]"
  exit 1
fi

node post_converter/md_converter.js $1
node post_converter/save_post.js $1 "$2"
