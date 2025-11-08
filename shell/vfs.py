import json
import os

class VirtualFileSystem:
    def __init__(self, vfs_path=None):
        self.structure = {}
        if vfs_path:
            self.load_vfs(vfs_path)

    def load_vfs(self, path):
        """Load the virtual file system from a JSON file."""
        if not os.path.exists(path):
            raise FileNotFoundError(f"VFS file '{path}' not found.")
        try:
            with open(path, "r", encoding="utf-8") as f:
                self.structure = json.load(f)
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format in VFS file.")

    def _navigate(self, parts):
        """Navigate through the VFS structure using a list of path parts."""
        node = self.structure.get("root", {})
        for p in parts:
            if not p or p == "~":
                continue
            if p not in node:
                raise FileNotFoundError(f"Path not found: {'/'.join(parts)}")
            node = node[p]
        return node

    def list_dir(self, path_parts):
        """List all files and directories in the current path."""
        node = self._navigate(path_parts)
        if isinstance(node, dict):
            return list(node.keys())
        else:
            raise NotADirectoryError("Cannot list a non-directory path.")
# Stage 4: Implemented Virtual File System
