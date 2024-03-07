#!/usr/bin/env bash
#script that sets up your web servers for the deployment of web_static

sudo apt-get update
sudo apt-get -y install nginx

mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared/

echo "\
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" >> /data/web_static/releases/test/index.html

link_path="/data/web_static/current"
target_path="/data/web_static/releases/test/"

ln -sf "$target_path" "$link_path"

sudo chown -R ubuntu:ubuntu /data

sed -i "/server_name _;/a\" "\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tindex index.html;\n\t}" /etc/nginx/sites-available/default

sudo service nginx restart
