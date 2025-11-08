import json
import os

def load_config(config_path=None, cli_vfs=None):
    """Load configuration from file and CLI args, with error handling"""
    config = {"vfs_name": "DefaultVFS", "vfs_path": None}

    if config_path:
        if not os.path.exists(config_path):
            print(f"Warning: Config file '{config_path}' not found. Using defaults.")
        else:
            try:
                with open(config_path, "r", encoding="utf-8") as f:
                    file_data = json.load(f)
                    config.update(file_data)
            except json.JSONDecodeError:
                print(f"Error: Config file '{config_path}' is not valid JSON.")
            except Exception as e:
                print(f"Error reading config file: {e}")

    if cli_vfs:
        config["vfs_path"] = cli_vfs

    if not config["vfs_path"]:
        print("Warning: No VFS path provided. Using in-memory empty structure.")

    return config
