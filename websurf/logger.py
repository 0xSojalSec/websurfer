#!/usr/bin/env python3

name = "Websurfer"

def error(msg):
    print(f"\x1B[90m[\x1B[93m{name}\x1B[90m] " + 
        f"[\x1B[31m-\x1B[90m]\x1B[0m {msg}")

def success(msg):
    print(f"\x1B[90m[\x1B[93m{name}\x1B[90m] " + 
        f"[\x1B[32m+\x1B[90m]\x1B[0m {msg}")

def message(msg):
    print(f"\x1B[90m[\x1B[93m{name}\x1B[90m] " + 
        f"[\x1B[34m*\x1B[90m]\x1B[0m {msg}")

def warning(msg):
    print(f"\x1B[90m[\x1B[93m{name}\x1B[90m] " + 
        f"[\x1B[33m!\x1B[90m]\x1B[0m {msg}")