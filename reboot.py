#!/usr/bin/env python

import paramiko;
import time;

def seccp(server, port, username, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, username, password)
    return client
server = seccp("host", 22, "username", "password");
server.exec_command("Tomcat/bin/shutdown.sh");
print "Rebooting...\n";
time.sleep(10);
server.exec_command("Tomcat/bin/startup.sh");
print "Rebooted";
server.close();