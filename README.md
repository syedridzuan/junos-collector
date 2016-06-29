# junos-collector
Juniper Collector is python code to collect information for Juniper routers by using CLI

# Requirement
Apart from default python library this code require paramiko, to install paramiko:
```
$ pip install paramiko
````

# Installation
```
git clone https://github.com/syedridzuan/junos-collector
```

# Configuration
Please edit config.ini file, example as below:
```[config]
username : myusername
password : mypass
commands : ["show chassis hardware", "show version" ]
hosts : ["192.168.0.1","192.168.0.2"]
result_folder : result
```
## Configuration details :
1. username : Your router/device username
2. password: You router/devicee password
3. commands: list of command to execute
4. result_folder : your result file will be store here.



