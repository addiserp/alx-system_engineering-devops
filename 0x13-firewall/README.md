## Alx Assignment
0x13-firewall

## Author
Mikias Gedlu
AddisERP System Solutions

## Steps Done
1.Open the UFW configuration file:

sudo nano /etc/default/ufw 

Enable packet forwarding: set DROP TO ACCEPT

DEFAULT_FORWARD_POLICY="ACCEPT"

2.Enabling Packet Forwarding

 sudo nano /etc/ufw/sysctl.conf

 uncomment net/ipv4/ip_forward=1

3. Port Forwarding From an External Port to an Internal Port

sudo nano /etc/ufw/before.rules 

add the following code @top or @bottom (not in the middle) 

# Forward traffic from port 8080 to port 80.
*nat
:PREROUTING ACCEPT [0:0]
-A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-port 80

COMMIT

# end of code

4. Add ufw rule

sudo ufw allow 8080/tcp

5. Restart ufw

sudo systemctl restart ufw

 or

sudo ufw disable 
sudo ufw enable 

