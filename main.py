from shell.vfs import VirtualFileSystem
from shell.config import load_config
from shell.repl import Shell

def main():
    # Load configuration
    config = load_config("config.json", None)

    # Initialize Virtual File System
    vfs = VirtualFileSystem(config["vfs_path"])

    # Initialize Shell
    shell = Shell(vfs_name=config["vfs_name"])

    # Attach the VFS to shell state
    shell.state["vfs"] = vfs

    # Run
    shell.run()

if __name__ == "__main__":
    main()
