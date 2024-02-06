# Author: Ikram Khan
# v1.0 - 11/22/2023
# v1.1 - 01/08/2024 - added comments and improved code. 

import socket

def scan_ports(target):
    # Display a banner for the start of the scan
    # '35' multiplied by '*' creates a string consisting of 40 asterisk characters.
    # F-string helps in creating a dynamic banner where the IP address being scanned ('target').
    print("*" * 35)
    print(f"* Scanning: {target} *")
    print("*" * 35)

    # Iterate through ports (1 to 2048)
    for port in range(1, 2049):
        # Create a socket object for TCP connections
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set a timeout for socket connection attempts to avoid long waits. This time is 1s = 1000ms.
        s.settimeout(1)

        # The 'try' keyword is used to begin a block of code where errors might occur. 
        try:
            # Attempt to connect to the target IP and port. The 'connect_ex' method is specifically used for
            # non-blocking socket connections.
            result = s.connect_ex((target, port))
            
            # Check if the connection attempt is successful (result code 0)
            if result == 0:
                print(f"Port {port}: Open")
            # If the connection attempt is NOT successful, no message is printed. 

        except socket.error as e:
            # Handle any socket errors that may occur during the connection attempt.
            # Prints an error message including a specific error code.
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
