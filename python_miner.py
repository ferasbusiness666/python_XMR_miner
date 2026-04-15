import subprocess
import sys
import os

def install_deps():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"], 
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

install_deps()
import requests

WALLET_ADDRESS = "46a2iTSuQc3G4ENKmpiCpuercLDbmLH94RBHp1wHMgZLTtD7xfTuGuQMuX84RQvZBfFWMe9J5J9fSHZFa6BYpwra8if88Eu"
WORKER_NAME = "myworker"
POOL = "pool.supportxmr.com:3333"

def check_xmrig():
    return os.path.exists("./xmrig") or os.path.exists("./xmrig.exe")

def download_xmrig():
    print("XMRig not found.")
    print("Download it from: https://github.com/xmrig/xmrig/releases")
    print("Put xmrig (Linux) or xmrig.exe (Windows) in the same folder as this script.")
    sys.exit(1)

def start_mining():
    print(f"Starting Monero mining...")
    print(f"Wallet: {WALLET_ADDRESS[:10]}...{WALLET_ADDRESS[-5:]}")
    print(f"Pool: {POOL}")
    print(f"Worker: {WORKER_NAME}")
    print("-" * 40)

    binary = "./xmrig.exe" if os.name == "nt" else "./xmrig"

    cmd = [
        binary,
        "-o", POOL,
        "-u", f"{WALLET_ADDRESS}.{WORKER_NAME}",
        "-p", "x",
        "--cpu-max-threads-hint=50",  # use 75% of CPU threads
        "--donate-level=1",
    ]

    try:
        process = subprocess.run(cmd)
    except FileNotFoundError:
        download_xmrig()
    except KeyboardInterrupt:
        print("\nMining stopped.")

if __name__ == "__main__":
    if WALLET_ADDRESS == "YOUR_XMR_WALLET_ADDRESS_HERE":
        print("Set your wallet address in the script first (WALLET_ADDRESS variable).")
        sys.exit(1)

    if not check_xmrig():
        download_xmrig()

    start_mining()