import pickle
import os
import time
import stat

# --- CONFIGURATION ---
PICKLE_PATH = '/home/osboxes/shared-folder/HoneypotProject/honypot/cowrie/cowrie_data/etc/fs.pickle'
HONEYFS_DIR = '/home/osboxes/shared-folder/HoneypotProject/honypot/cowrie/cowrie_data/honeyfs'

# Cowrie Constants
A_NAME, A_TYPE, A_UID, A_GID, A_SIZE, A_MODE, A_CTIME, A_CONTENTS, A_TARGET, A_REALFILE = range(10)
T_DIR, T_FILE = 1, 2

def load_fs():
    with open(PICKLE_PATH, 'rb') as f:
        return pickle.load(f)

def save_fs(fs):
    with open(PICKLE_PATH, 'wb') as f:
        pickle.dump(fs, f)

def find_or_create_path(fs, path, is_dir=False, real_size=0):
    parts = [p for p in path.split('/') if p]
    current = fs
    for i, part in enumerate(parts):
        found = False
        for item in current[A_CONTENTS]:
            if item[A_NAME] == part:
                current = item
                found = True
                break
        
        if not found:
            is_last = (i == len(parts) - 1)
            actual_is_dir = is_dir if is_last else True
            
            # IMPORTANT: Cowrie needs the S_IFDIR (0o40000) or S_IFREG (0o100000) bits
            if actual_is_dir:
                mode = stat.S_IFDIR | 0o755
                size = 4096
                contents = []
            else:
                mode = stat.S_IFREG | 0o644
                size = real_size
                contents = b"" # Content is read from honeyfs folder by Cowrie

            new_entry = [part, T_DIR if actual_is_dir else T_FILE, 0, 0, size, mode, int(time.time()), contents, "", ""]
            current[A_CONTENTS].append(new_entry)
            current = new_entry
            print(f" [+] Added to pickle: {path} ({'DIR' if actual_is_dir else 'FILE'})")
    return current

def sync():
    if not os.path.exists(HONEYFS_DIR):
        print(f"Error: HoneyFS directory not found at {HONEYFS_DIR}")
        return

    fs = load_fs()
    print(f"--- Starting Sync from {HONEYFS_DIR} ---")
    
    for root, dirs, files in os.walk(HONEYFS_DIR):
        rel_root = os.path.relpath(root, HONEYFS_DIR)
        if rel_root == ".": rel_root = ""
        
        for d in dirs:
            path = os.path.join(rel_root, d)
            find_or_create_path(fs, path, is_dir=True)
            
        for f in files:
            path = os.path.join(rel_root, f)
            real_file_path = os.path.join(root, f)
            size = os.path.getsize(real_file_path)
            find_or_create_path(fs, path, is_dir=False, real_size=size)
            
    save_fs(fs)
    print("--- Sync Complete! Restart Cowrie now. ---")

if __name__ == "__main__":
    sync()

