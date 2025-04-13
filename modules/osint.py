#!/usr/bin/env python3

import requests
import socket
import whois

class OSINT:
    def __init__(self):
        pass

    def dns_lookup(self, domain):
        """
        Performs a DNS lookup for the given domain.
        """
        try:
            ip = socket.gethostbyname(domain)
            return ip
        except socket.gaierror:
            return f"Unable to resolve domain: {domain}"

    def whois_lookup(self, domain):
        """
        Performs a WHOIS lookup for the given domain.
        """
        try:
            w = whois.whois(domain)
            return w
        except Exception as e:
            return f"Error fetching WHOIS information: {str(e)}"

    def ip_geolocation(self, ip):
        """
        Uses an external API to fetch geolocation information for the given IP address.
        """
        url = f"https://ipinfo.io/{ip}/json"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return f"Unable to retrieve geolocation for IP: {ip}"

    def search_shodan(self, ip):
        """
        Uses the Shodan API to search for services and vulnerabilities related to the given IP.
        You would need a Shodan API key for this to work.
        """
        # Ensure that you replace 'YOUR_SHODAN_API_KEY' with an actual Shodan API key.
        api_key = "cFfC25HDsLNW4TaaPIk4Vekjgpk4P522"
        url = f"https://api.shodan.io/shodan/host/{ip}?key={api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return f"Unable to fetch Shodan data for IP: {ip}"

