Denial of Service (DoS attack) is a cyber attack that aims to temporarily or indefinitely disrupt the services of an internet-connected host, making a machine or network resources inaccessible to actual users. It is usually performed in the form of making the target system unable to respond to incoming requests due to overload due to overloading the target machine or resource with unnecessary requests.The attackers can use amplification techniques for attacks with higher bandwidth than they have and the DNS Protocol statistically has been used/exploited much more than the other protocols.


1. Why is this type of attack preferred, especially in the DNS protocol? Please explain briefly.
**In this kind of DOS attack, attacker spoof the victim's ip address so the DNS response is going to send to the victim and attacker also try to find a domain with many DNS records, So this way with each short DNS query that attacker send to the DNS server, the DNS server replies with a larger response to victim. So small Dns request from attacker results in large replies from the DNS servers to the victim machine, so it amplifies the attack that is why it is preferred.**

2. In DNS Amplification Attacks, are there any technical limitations or disadvantages for the attacker?
**Because the DNS replays never came to attackers and goes directly to victim, they do not have much information about the response, they can't be sure if victim drops or accepts the packets (maybe victim uses firewall to drop known and unkwon dns servers or limits the rate of dns packets). beside that the ISP (Internet Service Provider) of the attacker might reject any internal traffic with spoofed IP addresses.(If a packet is being sent from inside the network with a source address that makes it appear like it originated outside the network, it’s likely a spoofed packet and can be dropped.)**

3. Please find a suitable IP address for amplification attacks in DNS protocol and explain step by step how to find such servers easily.
**First of all we need to find some domains with many DNS records so this way amplification is implemented much more effectively, Then we need to send the request to some DNS server which is more likely not to be blocked by the victim.**

The source files of a sample application are attached as a .zip file. Please unzip the zip file
in a directory. The code in the app.py file in the unzipped directory contains several OWASP
Top 10:2021 vulnerabilities. Please review the code, identify contained vulnerabilities, and
suggest possible mitigations to resolve the identified vulnerabilities. Each area has to
include:

● What is the vulnerability?
● Why does the vulnerability arise (what is the reason for the vulnerability)?
● What is your mitigation suggestion to close the vulnerability?

Note 1: 10 areas are given below to write your answers. However, the application may or
may not include 10 vulnerabilities.

Note 2: Applicants can run the sample application using docker with the “docker-compose
up” command if necessary.

## Vulnerability 1 & Mitigation:

**injection**
specifically the sql injection. I did notice the two line code inside app.py and immidetly found that web app is vulnerable to the sql injection.
Problem :
    - statement = "SELECT username,password from users where username = '"+username+"' and password='"+password+"'"
    - cursor.execute(statement)
I can become admin with out knowing the password by injection sql commands into url :
    - http://172.17.0.2:5000/login/admin/' or 1=1 --'
    - http://172.17.0.2:5000/login/admin/' or '1'='1

To Mitigate injection : 
    - we need to validate and filtered the username and password provided by the user.
    - we can create Allow-list and say that input must be in range of some specific character list.
    - use Object Relational Mapping Tools (ORMs).



## Vulnerability 2 & Mitigation:
**Cryptographic Failures**

Problem:
    - First of all, the password and username is transmitted in http GET method which is open and in clear text
    - DES (Data Encryption Standard) is used as the encryption algorithm and is currently considered as a legacy algorithm (means it is old). Since the key used in des is only 56 bits, it creates a 2^56 keyspace (even less if we remove some special cases)
    - No certificate used
    - the given key and salt to the encrytion algorithm is always the same and is reused every time the encryption algorithm is used.
    - md5 waek hash function is used.
    - base64 encoding is used which can be decode by anyone.

To Mitigate cryptographic failures:
    - the password is sensitive data so it is better to trasmit the password at least using POST method
    - Use https
    - Use AES (Advance Encrytion Standard) or some other up-to-date encrytion algorithms that use bigger keys. for example AES uses 128, 192 and 256 bit keys.
    - Encrypt all data in transit with secure protocols such as TLS
    - Use cryptographically secure pseudo random number generator for salt values and also use proper key management.
    - Use Strong hashing fucntions such as scrypt and SHA3


## Vulnerability 3 &Mitigation:
**broken access control**

Problem:
    - When a user like admin logs in, a token will be generated and pushed to the "tokens" database and after that the generated token will be set as the "session_id" cookie for the user admin. This token will not be removed after the admin logs out. So if any one get access to that token and set a cookie as : "session_id"="admin_token" will be log in as admin 
    - Bypassing access control checks by modifying the token and cookie.
  
To Mitigate broken access control:
    - remove tokens from database after certain time, or after a user logs out.

GET /index HTTP/1.1
Host: 172.17.0.2:5000
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
DNT: 1
Connection: close
Cookie: session_id=admin.5MgMB6Oo5OOTFCOD3shaA1w3/U4sdLIxLGCV7VOySSZDkWeaYUGDTg==
Upgrade-Insecure-Requests: 1
Cache-Control: max-age=0



Vulnerability 4 & Mitigation:
**Identification and Authentication Failures**

Problem :
    - We can use automated attacks to brute force and find the password or username of the user. for example i used ffuf tool to burte force admin account. 
    - "ffuf -u http://172.17.0.2:5000/admin/FUZZ -w ./wordlist.txt"
    - As explained it also does not correctly invalidate Session IDs.
 
To Mitigate identifictation and authetication failures :
    - Use strong passwords
    - Limit login attempts for users, and block a user for a certain period of time if he/she enter wrong passwrod more than the limited value.
    - Use CAPCHAS
    - Use multi-factor authentication.


Vulnerability 5 & Mitigation:
**Security Logging and Monitoring**

Problem :
    - Auditable events, such as logins and failed logins, are not written to a log file for later inspection.

To Mitigate security logging and monitoring :
    - write the logs of all login, access control, user and server side input failures for later review and use them to identify suspicious or malicious activity

Vulnerability 6 & Mitigation:
**Insecure Design**

Problem :
    - the code is not securely desined and is vulnerable to known attacks such as sql injection and brute-force.

To Mitigate insecure design :
    - 
You are using pip version 22.0.4; however, version 22.1.1 is available.


Vulnerability 7 & Mitigation:
**Security Misconfiguration**

Problem : 
    - no token will not be removed from database and this way we will have some unnecessary tokens. In the long run this can cause the database to grow and slow down a lot.
    - The security settings in the database application server is not set to secure values (weak password)

To Mitigate security misconfiguration :
    - Remove the unused tokens from the database.
    - Use strong passwords for the database server 











    A05 Security Misconfiguration
    A06 Vulnerable and Outdated Components
    A08 Software and Data Integrity Failures


