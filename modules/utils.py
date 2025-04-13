#!/usr/bin/env python3

import os
import json

def is_valid_file(filepath):
    """
    Checks if the provided file path exists and is a valid file.
    """
    if os.path.isfile(filepath):
        return True
    else:
        return False

def load_json_file(filepath):
    """
    Loads a JSON file and returns its content.
    """
    if is_valid_file(filepath):
        with open(filepath, 'r') as file:
            return json.load(file)
    else:
        return f"File not found: {filepath}"

def save_json_to_file(data, filepath):
    """
    Saves the provided data (in JSON format) to the specified file.
    """
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)
    return f"Data successfully saved to {filepath}"

def get_ip_from_domain(domain):
    """
    Resolves a domain to its corresponding IP.
    """
    try:
        import socket
        ip = socket.gethostbyname(domain)
        return ip
    except socket.gaierror:
        return f"Unable to resolve domain: {domain}"

def check_network_status():
    """
    Checks if the machine can access the internet by pinging Google's DNS server.
    """
    response = os.system("ping -c 1 8.8.8.8")
    if response == 0:
        return "Network is reachable."
    else:
        return "Network is not reachable."
