import subprocess
import sys

def install_packages(packages):
    """
    Checks and installs the specified packages, handling version conflicts by reinstalling the specified version.
    """
    installation_details = {}
    errors = []

    for package in packages:
        # Using subprocess.run() to capture output more reliably
        result = subprocess.run([sys.executable, '-m', 'pip', 'install', package], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.returncode == 0:  # Successful installation
            installation_details[package] = 'Successfully installed'
        else:  # There was an error
            error_message = f"Failed to install {package}: {result.stderr.strip()}"
            installation_details[package] = 'Installation failed'
            errors.append(error_message)

    return installation_details, errors

# List of required packages with specific versions
required_packages = [
    'requests==2.31.0',
    'pytube==15.0.0',
    'tqdm==4.66.1',
    'mutagen==1.47.0',
    'inquirer==3.1.4',
    'questionary==1.9.0',
    'pygame==2.0.1'
]

# Perform the installations
installation_results, installation_errors = install_packages(required_packages)

# Output the installation details
for package, status in installation_results.items():
    print(f"{package}: {status}")

# Output any errors that occurred
if installation_errors:
    print("\nErrors during installation:")
    for error in installation_errors:
        print(error)