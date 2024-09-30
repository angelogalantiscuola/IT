# connect to ssh from cmd on windows
ssh x@10.40.71.199

# run code-server
code-server --bind-addr 0.0.0.0:9999 ~/temp

# open port on firewall
sudo firewall-cmd --zone=public --add-port=9999/tcp --permanent
sudo firewall-cmd --reload

# open code-server in browser
# http://10.40.71.199:9999/

