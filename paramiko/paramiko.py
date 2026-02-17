import paramiko

host  = "loacalhost"
port = 22
username = "Muskan Mishra"
password = 2002
# create an obj and connect to remote machines
client = paramiko.SSHClient()
# set the rulr to handle the unknown host keys, or the first time dconnecting host keys
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect(
    hostname = host,
    port = port,
    username = username,
    password = password
)
stdin, stdout, stderr = client.exec_command("whoami")
print(stdout.read().decode())
client.close()