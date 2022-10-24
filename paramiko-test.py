"""#paramiko - SSH wrapper
import paramiko
import time

# create new SSH client object
conn_params = paramiko.SSHClient()
conn_params.connect(
    hostname='192.168.234.3',
    username='test',
    password='Test123'
)

#we need to create ssh session with invoke shell function
conn = conn_params.invoke_shell()
conn.send("show ip interface brief\n")
#we get output in bytes, we need to convert from bytes to readable text
output = conn.recv(65535)
""" 
import time 
import paramiko

#create function and wait for 1 second for command to be proceeded
def send_cmd(conn,command):
    #connection -> send function -> command + ENTER
    conn.send(command + "\n")
    time.sleep(1.0)

def get_output(conn):
    #return conn encoded with utf-8
    return conn.recv(65535).decode("utf-8")


def main():
    #main function
     host_dict = {
        "192.168.234.2": "show running-config",
     }

     for hostname, show_command in host_dict.items():
        #invoke new ssh client
        conn_params = paramiko.SSHClient()
        #ignore ssh keys 
        conn_params.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #add parameters to connections
        conn_params.connect(
            hostname=hostname,
            port=22,
            username='test',
            password='Test123',
            look_for_keys=False,
            allow_agent=False,
        )
        #create new connection and sleep for 1 sec, then print if successful
        conn = conn_params.invoke_shell()
        time.sleep(1.0)
        print(f"Logged into {get_output(conn).strip()} successfully")
        #create commands we want to push to the device
        commands = [
            "enable",
            "terminal length 0",
            "show version | include Software",
            show_command,
        ]

        for command in commands: 
            #we need to send each command to the current SSH session
            send_cmd(conn,command)
            print(get_output(conn))
        
        conn.close()

#calls main fucntion only when script is invoked from shell
if __name__ == "__main__":
    main()