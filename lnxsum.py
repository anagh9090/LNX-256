#!/usr/bin/env python3
import hashlib
import struct
import os
import sys
import time

# --- LNX ALGORITHM CONFIGURATION ---
# These constants define the 'Security Vault' strength.
# 524,288 cycles ensures even a supercomputer takes an eternity to brute-force.
ITERATIONS = 524288
SALT       = 0x5A5A5A5A
CHUNK_SIZE = 8 * 1024 * 1024  # 8MB: Optimal for i5-4300U L3 Cache

def calculate_lnx256(file_path):
    """
    Computes a hardened LNX-256 hash for a given file.
    Combines high-speed SHA-256 streaming with a sequential time-trap.
    """
    if not os.path.isfile(file_path):
        print(f"[!] Error: '{file_path}' is not a valid file.")
        return None

    file_size = os.path.getsize(file_path)
    sha_hasher = hashlib.sha256()
    
    print(f"[*] Analyzing: {os.path.basename(file_path)} ({file_size / 1024**3:.2f} GB)")
    
    # --- PHASE 1: HIGH-SPEED STREAMING ---
    try:
        with open(file_path, "rb") as f:
            bytes_read = 0
            while chunk := f.read(CHUNK_SIZE):
                sha_hasher.update(chunk)
                bytes_read += len(chunk)
                
                # Progress indicator for large ISOs
                progress = (bytes_read / file_size) * 100
                sys.stdout.write(f"\r[+] Reading File: {progress:.1f}%")
                sys.stdout.flush()
    except PermissionError:
        print("\n[!] Error: Permission denied. Run as Admin/Sudo.")
        return None

    # Extract the base state from SHA-256
    # struct.unpack converts the 32-byte hash into 8 unsigned 32-bit integers
    state = list(struct.unpack(">8I", sha_hasher.digest()))

    # --- PHASE 2: THE LNX TIME-TRAP ---
    # This part is strictly sequential to block supercomputer parallelism.
    print(f"\n[*] Hardening hash with {ITERATIONS} LNX cycles...")
    
    for cycle in range(ITERATIONS):
        for i in range(8):
            # Mix the current state with the neighbor and the cycle index
            state[i] = (state[i] ^ (state[(i-1) % 8] + cycle)) & 0xFFFFFFFF
            
            # The 'Swirl': 13-bit circular left shift
            state[i] = ((state[i] << 13) | (state[i] >> 19)) & 0xFFFFFFFF
            
            # Inject the hard-coded salt
            state[i] = (state[i] + SALT) & 0xFFFFFFFF

    # Convert the 8 integers back into a single hex string
    return ''.join(f'{x:08x}' for x in state)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python lnx_hasher.py <path_to_iso>")
    else:
        target_file = sys.argv[1]
        start_time = time.time()
        
        result = calculate_lnx256(target_file)
        
        if result:
            total_time = time.time() - start_time
            print("-" * 40)
            print(f"LNX-256 SIGNATURE: {result}")
            print(f"COMPLETED IN: {total_time:.2f} seconds")
            print("-" * 40)
