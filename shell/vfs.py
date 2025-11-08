import json
import os

class VirtualFileSystem:
    def __init__(self, vfs_path=None):
        self.structure = {}
        if vfs_path:
            self.load_vfs(vfs_path)

    def load_vfs(self, path):
        if not os.path.exists(path):
            raise FileNotFoundError(f"VFS file '{path}' not found.")
        with open(path, "r", encoding="utf-8") as f:
            self.structure = json.load(f)

    def _navigate(self, parts):
        node = self.structure.get("root", {})
        for p in parts:
            if not p or p == "~":
                continue
            if p not in node:
                raise FileNotFoundError(f"Path not found: {'/'.join(parts)}")
            node = node[p]
        return node

    def list_dir(self, path_parts):
        node = self._navigate(path_parts)
        if isinstance(node, dict):
            return list(node.keys())
        else:
            raise NotADirectoryError("Not a directory.")
