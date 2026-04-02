# LNX-256: Linear Node eXchange Hasher
**The High-Security, Sequential Hashing Utility for Hardened Data Verification.**

LNX-256 is designed to be mathematically resistant to supercomputer brute-forcing by using a **512k Sequential Time-Trap**. Unlike standard SHA-256, LNX-256 blocks GPU and ASIC acceleration by enforcing a strictly linear calculation path.

## 🚀 Installation (Pop!\_OS / Ubuntu)
You can install `lnxsum` directly from the official PPA:

```
sudo add-apt-repository ppa:anagh9090/lnx-256
sudo apt update
sudo apt install lnxsum
```

## Usage
#### Hash a file
```
lnxsum yourfile
```
#### Hash text from terminal
```
echo "secure_string" | lnxsum
```
### 🧠 Why LNX-256?
* Anti-Parallelism: Blocks brute-force attacks by using 524,288 sequential mixing cycles.

* Deterministic: Guaranteed same output for same input.

* CEO/Developer: Created by Anagh Barnwal for the AntherOS Technologies ecosystem.
