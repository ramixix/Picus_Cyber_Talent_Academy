## Default firewall block

Firewall default behaviour is opposite of default behaviour of anivirus programs. An antivirus takes an input and then try to match that to one of the signature that it contains. if it finds it finds and match it will detect the input as virus and block the input otherwise it will allow the input. The firewall is opposite it will look for match and if it finds a match it will allow the input otherwise it will block the input.

## difference between firewall and antivirus programs

|firewall|antivirus|
|---|---|
|Defalt Block|Default Allow|
|More Secure|Less Secure|
|Less Convenient|More Convenient|



## Ftp protocol
ftp server works on two ports 20 and 21. the 20 is used to get the commands and the 21 is used for data communication. When an clinet wants to download something from ftp server it first send the command to port 20 and tells the server what ports client will be listening to receive the file that it wants to download, then server goes to that port and send the data back to client using port 21. (this make a security problem because attacker can change the port that client is listening on the data would sent to another application of get lost.)

## how they fix the problem with ftp protocol
they redesign it. Now when client wants anything it send it's command to port 20 on server and then server response with a packet than contains a port number that server will be listen on. then client use that port to download or upload the desire file. **This is called the PASV Mode of ftp.**

## Application proxy filtering
the firewall can do three things with the packets. 
1. Allow the packet : permit it to go through in or out of the network
2. Drop : drop the packet from going in or out.
3. Forward : redirect a packet to a application proxy witch as user for more information before allow the packet or drop it.

Every firewall kind of use the froward option sends the not known packet to the a proxy and inspect the packet or ask more information before any next decision.

## forward and reveres proxies
- Forward proxy to protect the clients.
- Reverse proxy to protect the servers.