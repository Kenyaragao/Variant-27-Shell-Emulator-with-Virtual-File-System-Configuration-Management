# 🧩 Configuration Management — CLI Emulator (Variant №27)

## 🗂 Project Structure
VFS_shell/
├── config.json
├── vfs.json
├── startup.shs
├── main.py
└── shell/
├── init.py
├── repl.py
├── commands.py
├── config.py
├── vfs.py
└── logger.py
Capabilities

- Support for command-line arguments  
- Configuration loading from JSON file  
- CLI parameters take priority over configuration file  
- Implementation of a Virtual File System (VFS)
        
        запуск с параметром CLI ./startup.shs
- `stage_1_repl.shs` — Basic REPL (interactive shell with ls, cd, exit)  
- `stage_2_config.shs` — Added configuration file loading (`config.json`)  
- `stage_3_vfs.shs` — Implemented Virtual File System (`vfs.json`)  
- `stage_4_corecmd.shs` — Added core commands: ls, cd, cat, pwd  
- `stage_5_extended.shs` — Added extra commands: mkdir, touch, help

# ✅ Final Stage — Laboratory completed successfully (Variant 27)
