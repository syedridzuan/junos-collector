import paramiko,socket
from ConfigParser import SafeConfigParser
import json
import os
import datetime


#SSH Function
def sshConnect(ip, username, password, commands):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(ip, username=username, password=password)
        list_counter = 0
        result = []
        for item in commands:
            print item
            stdin, stdout, stderr = client.exec_command(item)
            # print stderr
            result_before = stdout.read()
            # print result_before
            result_command = [item, result_before]
            result.append(result_command)
        print "Success!! connection",
    except paramiko.AuthenticationException:
        print "Authentication problem"
        result = None
    except socket.error, e:
        print "Comunication problem "
        result = None
    client.close()
    return result

#write result to file
def createFiles(result, host, result_folder_abs, current_date_time ):
    print "Opening the file..."
    filename = result_folder_abs + "/" + host + ".txt"
    print filename
    target = open(filename, 'a+')
    for item in result:
        command = "----------------------------- %s-----------------------------\n" % item[0]
        target.write(str(command))
        mytime = "Server's Current Date & Iime is: %s\n" % current_date_time
        target.write(mytime)
        target.write(str(item[1]))
    target.close

#create result folder
def createFolder(result_folder_abs):
    if not os.path.exists(result_folder_abs):
        os.makedirs(result_folder_abs)


#main function
def main():
    config = SafeConfigParser()
    current_date_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    config.read('../config.ini')
    #load configuration
    username = config.get('config', 'username')
    password = config.get('config', 'password')
    hosts = json.loads(config.get('config', 'hosts'))
    command = json.loads(config.get('config', 'commands'))
    result_folder = config.get('config', 'result_folder')
    result_folder_abs = os.path.join(os.path.dirname(__file__), os.path.abspath('..'), result_folder )
    print "Result will be store in %s \n" % result_folder_abs

    #iterate trough hosts
    for host in hosts:
        result = sshConnect( host  , username , password,  command)

        #check if result return valid value and write if result available
        try:
            result[0]
            createFolder(result_folder_abs)
            createFiles(result, host, result_folder_abs, current_date_time)
        except TypeError:
            print "index error"

if __name__ == "__main__":
    main()
