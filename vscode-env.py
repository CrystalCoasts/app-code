import subprocess

def is_extension_installed(extension_id):
    """
    Check if a VS Code extension is installed.
    """
    result = subprocess.run(["code", "--list-extensions"], capture_output=True, text=True)
    installed_extensions = result.stdout.splitlines()
    return extension_id in installed_extensions

def install_extension(extension_id):
    """
    Install a VS Code extension.
    """
    print(f"Installing {extension_id}...")
    subprocess.run(["code", "--install-extension", extension_id], capture_output=True)

# Extension IDs for Dart and Flutter
extensions = [
    "Dart-Code.dart-code",
    "Dart-Code.flutter"
]

for extension_id in extensions:
    if not is_extension_installed(extension_id):
        install_extension(extension_id)
    else:
        print(f"{extension_id} is already installed.")
