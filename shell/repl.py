import getpass
import shlex
from shell.commands import execute_command


class Shell:
    def __init__(self, vfs_name):
        self.username = getpass.getuser()
        self.vfs_name = vfs_name
        self.state = {"running": True, "path": "~"}

    def run(self):
        print(f"Welcome to the Shell Emulator for VFS: {self.vfs_name}\n")

        while self.state["running"]:
            try:
                line = input(f"{self.username}@{self.vfs_name}:{self.state['path']}$ ")
                if not line.strip():
                    continue

                parts = shlex.split(line)
                command = parts[0]
                args = parts[1:]

                result = execute_command(command, args, self.state)
                if result:
                    print(result)

            except KeyboardInterrupt:
                print("\nUse 'exit' to quit.")
            except Exception as e:
                print(f"Unexpected error: {e}")
