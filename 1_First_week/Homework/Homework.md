1. What is the IP of the organization&DNS server/s?
    > tshark -r patika_2.pcap -Y "dns.flags.response==0 " -T fields -e "dns.qry.name" | sort -u
        amazon.com
        google.com

    To find DNS server's ip address :
    > tshark -r patika_2.pcap -Y "dns.flags.response==1" -T fields -e "dns.qry.name" -e "ip.src" | sort -u
            amazon.com      172.16.1.10
            amazon.com      8.8.4.4
            google.com      172.16.1.10
            google.com      8.8.4.4
    
    I'am not sure what is going on here be honest. Do they exchange ip:) ???

    To find http host and servers :
    > tshark -r patika_2.pcap -Y "http.request method==GET"
    192.168.1.55 → 192.168.1.10 HTTP 439 GET /index.html HTTP/1.1 
    192.168.1.55 → 192.168.1.10 HTTP 506 GET /page876475/wp-admin/admin-ajax.php?action=mec_load_single_page&time=2)+AND+(SELECT+7710+FROM+(SELECT(SLEEP(5)))ondl)+AND+(9419%3d9419 HTTP/1.1 
    10.10.10.108 → 192.168.1.10 HTTP 342 GET /166530/dotnettojs.hta HTTP/1.1 
    127.0.0.1 → 127.0.0.1    HTTP 381 GET /166530/dotnettojs.hta HTTP/1.1 
    192.168.1.10 → 192.168.1.55 HTTP 452 GET /heartbeat-1652561296.html HTTP/1.1 
    192.168.1.10 → 192.168.1.55 HTTP 448 GET /764796-1652561297.exe HTTP/1.1 
    192.168.1.55 → 192.168.1.10 HTTP 356 GET /page451444/printenv.shtml?%3Cscript%3EaIert(%27xss%27)%3C/script%3E HTTP/1.1 


    From here we found some interesting data. In second line we can see that 192.168.1.55 tried to perform sql injection. 764796-1652561297.exe is also interesting which is downloaded by 192.168.1.10 . At last line 192.168.1.55 tried to test if page is vulnerable to xxs vulnerability.

--- 

2. What is the name of the malicious file/s downloaded by the accountant? *
    As we found out in First part 192.168.1.55 donwloaded 764796-1652561297.exe file which might be the malicous file that we are looking for. we download the file.

---
 
3. What is the sha256 hash of the downloaded malicious file/s? *
> file 764796-1652561297.exe 
    764796-1652561297.exe: PE32 executable (GUI) Intel 80386 (stripped to external PDB), for MS Windows, UPX compressed

    From PE32 we undrestand that it is Portable Executable 32-bit. 
   
> sha256sum 764796-1652561297.exe 
77a398c870ad4904d06d455c9249e7864ac92dda877e288e5718b3c8d9fc6618  

---

4. What is the name of the malware/s, according to BitDefender? *
I don't use windows so BitDefender is not installed on my computer. But By searching the hash value in www.virustotal.com website, I found alot of details about the malware. Bitdefender analysis it as "Generic.Ransom.Hive.A.3532D023",But in the Details tab we can see the name of the malware is mentioned as "encryptor_win32.exe".

---

5. What is the malware type of the malicious file/s? *
From www.virustotal.com website I found that it is a Ransomware.

---

6. What is the malware family of the malicious file/s? *

---

7. What are the used TTP/s according to the MITRE ATT&CK framework for malicious file/s? *

---

8. What are the payload/s for web application threats? *
"dotnettojs.hta" contained some interesting code, I am not sure if it is what we are looking for, but I tried to decode  it from base64, but could not do it successfully. 

"""System.DelegateSerializationHolder.....Delegate.target0.method0...0System.DelegateSerializationHolder+DelegateEntry"System.DelegateSerializationHolder/System.Reflection.MemberInfoSerializationHolder	....	....	.........0System.DelegateSerializationHolder+DelegateEntry.....type.assembly.target.targetTypeAssembly.targetTypeName
methodName
delegateEntry.......0System.DelegateSerializationHolder+DelegateEntry...../System.Runtime.Remoting.Messaging.HeaderHandler.....Kmscorlib, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089......target0	.....	....System.Delegate.
...
DynamicInvoke
....."System.DelegateSerializationHolder.....Delegate.target0.method0...0System.DelegateSerializationHolder+DelegateEntry./System.Reflection.MemberInfoSerializationHolder	....	....	
......../System.Reflection.MemberInfoSerializationHolder.....Name.AssemblyName	ClassName	Signature
MemberType.GenericArguments.......
System.Type[]	
...	....		........,System.Object DynamicInvoke(System.Object[])....
.............. System.Xml.Schema.XmlValueGetter.....MSystem.Xml, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089......target0	..........System.Reflection.Ass"""

this is all i can extract

---

9. What are the affected product/s for web application threat/s? *

---

10. If it exists for web application threats, what are the CVE and CWE number/s of the webapplication threats?