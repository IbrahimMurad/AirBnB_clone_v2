#!/usr/bin/env bash
# sets up my web servers for the deployment of web_static

sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
echo "<html>
	<head>
	</head>
	<body>
		Holberton School
	</body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
my_web_static="location /hbnb_static/ {
	alias /data/web_static/current/;
	autoindex off;
}
"
sed -i "/	server_name _;/ a\	$my_web_static" /etc/nginx/sites_enabled/default
