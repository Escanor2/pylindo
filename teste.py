import subprocess

program_path = r"C:\Wemade\Mir4Global\Mir4Launcher\Mir4Launcher1.exe"

subprocess.run(["runas", "/user:Administrator", program_path])
