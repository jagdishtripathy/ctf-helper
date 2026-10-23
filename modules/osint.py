#!/usr/bin/env python3

import ipaddress
import os
import socket

import requests
import whois


class OSINT:
    """Small helpers for authorized OSINT lookups."""

    def dns_lookup(self, domain):
        """Resolve a domain to its first IPv4 address."""
        try:
            return socket.gethostbyname(domain)
        except socket.gaierror:
            return f"Unable to resolve domain: {domain}"

    def whois_lookup(self, domain):
        """Perform a WHOIS lookup for a domain."""
        try:
            return whois.whois(domain)
        except Exception as exc:
            return f"Error fetching WHOIS information: {exc}"

    def ip_geolocation(self, ip):
        """Fetch IP geolocation data from ipinfo.io."""
        try:
            ipaddress.ip_address(ip)
        except ValueError:
            return "Invalid IP address."

        try:
            response = requests.get(
                f"https://ipinfo.io/{ip}/json",
                timeout=10,
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException:
            return "Unable to retrieve geolocation data. Check network access and try again."
        except ValueError:
            return "The geolocation service returned invalid JSON."

    def search_shodan(self, ip):
        """Look up a host using SHODAN_API_KEY from the environment."""
        api_key = os.environ.get("SHODAN_API_KEY")
        if not api_key:
            return (
                "Shodan API key not configured. Set the SHODAN_API_KEY "
                "environment variable and try again."
            )

        try:
            ipaddress.ip_address(ip)
        except ValueError:
            return "Invalid IP address."

        try:
            response = requests.get(
                f"https://api.shodan.io/shodan/host/{ip}",
                params={"key": api_key},
                timeout=10,
            )
            if response.status_code == 401:
                return "Shodan rejected the API key. Verify or regenerate it."
            if response.status_code == 404:
                return f"No Shodan host data found for IP: {ip}"
            response.raise_for_status()
            return response.json()
        except requests.RequestException:
            return "Unable to fetch Shodan data. Check network access and the API key."
        except ValueError:
            return "Shodan returned invalid JSON."
