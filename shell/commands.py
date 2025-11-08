def execute_command(command, args, shell_state):
    """Execute shell commands using the VFS structure."""
    vfs = shell_state["vfs"]
    path = shell_state["path"]

    try:
        if command == "ls":
            contents = vfs.list_dir(path.split("/"))
            return "\n".join(contents)

        elif command == "cd":
            if len(args) != 1:
                return "Usage: cd <path>"
            new_path = args[0].strip("/")
            vfs._navigate(new_path.split("/"))  # validate path
            shell_state["path"] = new_path
            return f"Changed directory to /{new_path}"

        elif command == "cat":
            if len(args) != 1:
                return "Usage: cat <file>"
            node = vfs._navigate(args[0].strip("/").split("/"))
            if isinstance(node, str):
                return node
            return "Error: Not a file."

        elif command == "pwd":
            return f"/{path}"

        elif command == "mkdir":
            if len(args) != 1:
                return "Usage: mkdir <directory>"
            vfs.make_dir(path.split("/"), args[0])
            return f"Directory '{args[0]}' created."

        elif command == "touch":
            if len(args) != 1:
                return "Usage: touch <filename>"
            vfs.create_file(path.split("/"), args[0], "")
            return f"File '{args[0]}' created."

        elif command == "help":
            return get_help_text()

        elif command == "exit":
            shell_state["running"] = False
            return "Exiting shell..."

        else:
            return f"Unknown command: {command}"

    except Exception as e:
        return f"Error: {e}"


def get_help_text():
    """Return a string with all available commands."""
    return (
        "Available commands:\n"
        "ls      - List directory contents\n"
        "cd      - Change current directory\n"
        "cat     - Display file contents\n"
        "pwd     - Show current directory path\n"
        "mkdir   - Create a new directory\n"
        "touch   - Create a new empty file\n"
        "help    - Show available commands\n"
        "exit    - Exit the shell"
    )
# Stage 5: Added shell commands and logging
