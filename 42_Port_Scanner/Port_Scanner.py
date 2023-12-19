import socket
import subprocess
import platform


## gets systems own ip adress and then finds the subnet ip
def Find_IP_Range():
    # Get Hostname and IP of the local device
    hostname = socket.gethostname()
    ip_Addr = socket.gethostbyname(hostname)

    ip_Parts = ip_Addr.split(".")
    ip_Parts[3] = 0
    return ip_Parts


##used to ping devices on the network
def Ping_Device(host):
    # Determine the appropriate ping command based on the operating system
    if platform.system().lower() == "windows":
        command = ["ping", "-n", "1", host]
    else:
        command = ["ping", "-c", "1", host]

    try:
        # Run the ping command
        subprocess.check_output(
            command, stderr=subprocess.STDOUT, universal_newlines=True
        )
        return True
    except subprocess.CalledProcessError:
        return False


##Gets the MAC uses ARP for this
def Get_MAC_Address(ip_address):
    if platform.system().lower() == "windows":
        command = ["arp", "-a", ip_address]
    else:
        command = ["arp", "-n", ip_address]

    try:
        result = subprocess.check_output(
            command, stderr=subprocess.STDOUT, universal_newlines=True
        )
        # Parse the MAC address from the result
        mac_address = result.split()[3]
        return mac_address
    except subprocess.CalledProcessError:
        return None


##Gets device name by reverse DNS lookup
def Get_Device_Name(ip_address):
    try:
        host_name, _, _ = socket.gethostbyaddr(ip_address)
        return host_name
    except socket.herror:
        return None


##final to print all of the ip adresses
def Print_Results():
    addr_Range = Find_IP_Range()
    dot = "."
    for i in range(255):
        ip_To_Scan = (
            addr_Range[0] + dot + addr_Range[1] + dot + addr_Range[2] + dot + str(i)
        )
        result = Ping_Device(ip_To_Scan)
        if result:
            print("\n")
            print(f"{ip_To_Scan} is reachable")
            mac_address = Get_MAC_Address(ip_To_Scan)
            if mac_address:
                print(f"MAC Address for {ip_To_Scan}: {mac_address}")
            else:
                print(f"Failed to retrieve MAC Address for {ip_To_Scan}")
            device_name = Get_Device_Name(ip_To_Scan)
            if device_name:
                print(f"Device Name for {ip_To_Scan}: {device_name}")
            else:
                print(f"Failed to retrieve Device Name for {ip_To_Scan}")


Print_Results()
