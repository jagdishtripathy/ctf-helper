import jwt
from tqdm import tqdm

def jwt_brute_force(token, wordlist_path):
    try:
        header = jwt.get_unverified_header(token)
    except jwt.exceptions.DecodeError:
        print("[!] Invalid JWT token format.")
        return

    if header.get("alg") != "HS256":
        print("[!] Only HS256 algorithm is supported for brute-force.")
        return

    print("[*] Starting brute-force on the JWT token using HS256...")
    with open(wordlist_path, 'r', encoding='latin-1') as f:
        passwords = f.read().splitlines()

    for password in tqdm(passwords, desc="Brute-forcing"):
        try:
            decoded = jwt.decode(token, password, algorithms=["HS256"])
            print(f"[+] Secret found: {password}")
            print(f"[+] Decoded Payload: {decoded}")
            return
        except jwt.InvalidTokenError:
            continue

    print("[-] Secret not found in wordlist.")
