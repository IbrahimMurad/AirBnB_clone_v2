# Redo the task #0 but by using Puppet

exec { 'setup':
  provider => shell,
  command  => "apt-get update; apt-get install -y nginx; mkdir -p /data; mkdir -p /data/web_static; mkdir -p /data/web_static/releases; mkdir -p /data/web_static/shared; mkdir -p /data/web_static/releases/test; echo '<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>' > /data/web_static/releases/test/index.html; ln -sf /data/web_static/releases/test/ /data/web_static/current; chown -R ubuntu:ubuntu /data/; my_web_static='\tlocation \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current\/;\n\t\tautoindex off;\n\t}\n'; sed -i '/	server_name _;/ a\ $my_web_static' /etc/nginx/sites-enabled/default; service nginx restart;",
}
