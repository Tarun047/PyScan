# PyScan
<b>This is a Cloud-Scanner with very Light Foot-Print, for every programmer coded in Python using VirusTotal API</b>
<br/>
The present anti-virus Software Take a lot of memory and are cumbersome for a programmers environment. The Solution to this is a Cloud Antivirus Software which has it's Database in the cloud and Connects to it reduce the footprint.<br />
This Python Script utilizes the Virus Total API to Scan Files and produce Reports so that the programmer can decide to keep or remove a File.<br />
The Script also uses a database to store the results to imporove the detection process in future<br />
# Usage
First open the PyScan.py using any Text Editor and fill your api key from Virus Total in the \_my_key field.<br />
You can get yourself one by going to this link <a href="https://www.virustotal.com/#/join-us">Virus Total SignUp</a><br/>
Once you have a an account go to Settings ->API KEY 
<p />
Now Use the command line to invoke scanner as <br />
python PyScan.py <file_name>
<br />
The Script first checks Local Database and then the VT Database for the Hash, if not found it automatically uploads the file and gets the results(this takes a bit-time, so be patient)
<br/ >
<b> And Finally the result is on your screen</b><br />
<!-- copy and paste. Modify height and width if desired. --> <a href="https://content.screencast.com/users/Tarun047/folders/Jing/media/239ded93-a826-4966-8cf1-17ae4060d00a/2018-06-13_1552.png"><img class="embeddedObject" src="https://content.screencast.com/users/Tarun047/folders/Jing/media/239ded93-a826-4966-8cf1-17ae4060d00a/2018-06-13_1552.png" width="979" height="512" border="0" /></a>
<br />

![sam](https://user-images.githubusercontent.com/32017154/41347081-39913030-6f26-11e8-9682-40077fda41d5.PNG)

