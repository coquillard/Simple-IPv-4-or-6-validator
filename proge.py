import re

n = []  # List of strings waiting for checking.

# IP finding regex patterns, the program will look for.

ipv6 = r"\b(([\da-f]{1,4}):){7}[\da-f]{1,4}\b"
ipv4 = r"\b((25[0-5]|2[0-4][\d]|1[\d][\d]|[1-9][\d]|[1-9])\.){3}(25[0-5]|2[0-4][\d]|1[\d][\d]|[1-9][\d]|[1-9])\b"

# Iterating through the list (n)

for i in range(len(n)):

    strin = n[i]  # strin = string you want to check

    if re.match(ipv6, strin):
        print("IPv6")  # If it has found an IPv6, it prints IPv6.
        print(n[i])  # And prints the IP.

    elif re.findall(ipv4, strin):
        print("IPv4")  # If it has found an IPv4, it prints IPv4.
        print(n[i])  # And prints the IP.

    else:
        print("Neither")  # When neither was found, it prints neither.


