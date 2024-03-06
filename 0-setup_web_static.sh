#!/usr/bin/env bash
# sets up my web servers for the deployment of web_static

mkdir -p /data
mkdir -p /data/web_static
mkdir -p /data/web_static/releases
mkdir -p /data/web_static/shared
mkdir -p /data/web_static/releases/test
echo "<html>
        <head>
        </head>
        <body>
                Holberton School
        </body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
my_web_static="\tlocation \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current\/;\n\t\tautoindex off;\n\t}
"
sed -i "/       server_name _;/ a/$my_web_static" /etc/nginx/sites-enabled/default
service nginx restart
