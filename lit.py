import hashlib
import time
import game

def switch(version):
    hash = hashlib.sha256(bytes(version, "utf8")).digest()
    if hash[0] % 4 != 0:
        game.write("Unknown version.")
        return
    game.write("Downloading version...")
    size = int.from_bytes(hash[:3])
    for i in range(0, size, 42643):
        game.write(f"{i} / {size} files", end="\r")
        time.sleep(0.05)
    game.write(f"{size} / {size} files")
    game.write("On version " + version)