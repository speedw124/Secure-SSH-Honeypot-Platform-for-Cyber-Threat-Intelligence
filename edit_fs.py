import pickle
import os
import time

# Configuration
PICKLE_PATH = '/home/osboxes/shared-folder/HoneypotProject/honypot/cowrie/cowrie_data/etc/fs.pickle'

# Cowrie Constants
A_NAME, A_TYPE, A_UID, A_GID, A_SIZE, A_MODE, A_CTIME, A_CONTENTS, A_TARGET, A_REALFILE = range(10)
T_DIR, T_FILE = 1, 2

def load_fs():
    with open(PICKLE_PATH, 'rb') as f:
        return pickle.load(f)

def save_fs(fs):
    with open(PICKLE_PATH, 'wb') as f:
        pickle.dump(fs, f)
    print(f"Successfully saved changes to {PICKLE_PATH}")

def find_path(fs, path):
    parts = [p for p in path.split('/') if p]
    current = fs
    for part in parts:
        found = False
        for item in current[A_CONTENTS]:
            if item[A_NAME] == part:
                current = item
                found = True
                break
        if not found: return None
    return current

def list_dir(path="/"):
    fs = load_fs()
    target = find_path(fs, path)
    if not target or target[A_TYPE] != T_DIR:
        print("Directory not found.")
        return
    print(f"\nContents of {path}:")
    print(f"{'MODE':<10} {'UID':<5} {'GID':<5} {'SIZE':<8} {'NAME'}")
    for item in target[A_CONTENTS]:
        t = "d" if item[A_TYPE] == T_DIR else "-"
        mode = oct(item[A_MODE])[-3:]
        print(f"{t}{mode:<9} {item[A_UID]:<5} {item[A_GID]:<5} {item[A_SIZE]:<8} {item[A_NAME]}")

def update_file(path, new_content):
    fs = load_fs()
    target = find_path(fs, path)
    if not target or target[A_TYPE] != T_FILE:
        print("File not found.")
        return
    target[A_CONTENTS] = new_content.encode() + b'\n'
    target[A_SIZE] = len(target[A_CONTENTS])
    save_fs(fs)
    print(f"Updated {path} content.")
def add_new_file(path, is_dir=False):
    fs = load_fs()
    # Split path into directory and filename
    parts = [p for p in path.split('/') if p]
    filename = parts[-1]
    parent_path = "/" + "/".join(parts[:-1])
    
    parent = find_path(fs, parent_path)
    if not parent:
        print(f"Parent directory {parent_path} not found in pickle.")
        return

    # Check if already exists
    for item in parent[A_CONTENTS]:
        if item[A_NAME] == filename:
            print(f"{path} already exists in pickle.")
            return

    # Create new entry [name, type, uid, gid, size, mode, ctime, contents, target, realfile]
    new_entry = [
        filename, 
        T_DIR if is_dir else T_FILE, 
        0, 0, 0, 
        0o755 if is_dir else 0o644, 
        int(time.time()), 
        [] if is_dir else b"", 
        "", ""
    ]
    
    parent[A_CONTENTS].append(new_entry)
    save_fs(fs)
    print(f"Added {path} to pickle.")

if __name__ == "__main__":
    # --- PART 1: Update existing files ---
    update_file("/etc/hostname", "db-server-backup")
    update_file("/etc/issue", "Debian GNU/Linux 11 \\n \\l\nWelcome to DB-BACKUP-SERVER")
    update_file("/etc/hosts", "127.0.0.1\tlocalhost\n127.0.1.1\tdb-server-backup")

    # --- PART 2: Add your NEW HoneyFS files here ---
    # Example: If you have a file in honeyfs/home/sysadmin/notes.txt
    # add_new_file("/home/sysadmin/notes.txt", is_dir=False)
    
    # Example: If you have a folder in honeyfs/var/www
    # add_new_file("/var/www", is_dir=True)

    # --- PART 3: View the results ---
    list_dir("/etc")

