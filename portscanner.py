import socket

def scan_ports(target):
    # Display a banner for the start of the scan
    print("*" * 40)
    print(f"* Scanning: {target} *")
    print("*" * 40)

    # Iterate through ports (1 to 1024)
    for port in range(1, 1025):
        # Create a socket object for TCP connections
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set a timeout for socket connection attempts to avoid long waits
        s.settimeout(1)

        try:
            # Attempt to connect to the target IP and port
            result = s.connect_ex((target, port))
            
            # Check if the connection attempt is successful (result code 0)
            if result == 0:
                print(f"Port {port}: Open")

        except socket.error as e:
            # Handle any socket errors that may occur during the connection attempt
            print(f"Error while scanning port {port}: {e}")

        finally:
            # Close the socket to release resources
            s.close()

if __name__ == "__main__":
    # Prompt the user to enter an IP address for scanning
    print("Please enter an IP Address to scan.")
    target = input("> ")

    # Call the scan_ports function with the specified IP address
    scan_ports(target)
