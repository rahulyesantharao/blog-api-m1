#!/bin/sh

if [ $# -eq 1 ]; then
  if [ ! -f "post_converter/md_posts/post$1.md" ]; then
    echo "The specified file 'post$1.md' does not exist"
    exit 1
  fi
else
  echo "Usage $0 [<post #>] "
  exit 1
fi

node post_converter/md_converter.js $1
node post_converter/save_post.js $1
