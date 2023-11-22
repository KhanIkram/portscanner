# portscanner
This python script scans for open ports on a specified IP. It prompts the user for the IP, iterates through ports 1 - 1024, attempts a 1-second socket connection for each port. If successful (result code 0), it prints the open port; otherwise, it prints an error. 
