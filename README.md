# blog-api

A Flask API that serves content for my blog at https://rahulyesantharao.com/blog. The API is hosted at https://api.rahulyesantharao.com/blog-api.

Remember that we also create a systemd unit file at /etc/systemd/system/blogapi.service(https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uwsgi-and-nginx-on-ubuntu-16-04)

## To Use:
First, add the file `post_converter/md_posts/post<#>.md`. Then, add the corresponding data to `post_converter/md_posts/metadata.json`. Then, run `./savepost.sh <#>`.
