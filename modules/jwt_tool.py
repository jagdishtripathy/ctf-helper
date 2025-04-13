import base64
import json
import hmac
import hashlib

def base64url_decode(data):
    padding = '=' * (4 - len(data) % 4)
    return base64.urlsafe_b64decode(data + padding)

def decode_jwt(token):
    try:
        header_b64, payload_b64, signature = token.split('.')
        header = json.loads(base64url_decode(header_b64))
        payload = json.loads(base64url_decode(payload_b64))

        print("[+] Header:", json.dumps(header, indent=4))
        print("[+] Payload:", json.dumps(payload, indent=4))
        print("[+] Signature:", signature)

        if header.get("alg", "").lower() == "none":
            print("[!] Warning: Token uses 'none' algorithm, potentially vulnerable!")

    except Exception as e:
        print(f"[!] Failed to decode JWT: {e}")

def brute_force_jwt(token, wordlist_path):
    try:
        header_b64, payload_b64, signature = token.split('.')
        header = json.loads(base64url_decode(header_b64))

        if not header.get("alg", "").startswith("HS"):
            print("[!] Brute force is only supported for HMAC (HS256/HS512) tokens.")
            return

        print(f"[+] Attempting brute-force with wordlist: {wordlist_path}")
        with open(wordlist_path, 'r') as f:
            for secret in f:
                secret = secret.strip()
                data = f"{header_b64}.{payload_b64}"
                hashed = hmac.new(secret.encode(), data.encode(), hashlib.sha256).digest()
                sig_check = base64.urlsafe_b64encode(hashed).decode().rstrip("=")
                if sig_check == signature:
                    print(f"[+] Secret key found: {secret}")
                    return
        print("[!] Secret key not found.")
    except Exception as e:
        print(f"[!] Brute-force failed: {e}")
