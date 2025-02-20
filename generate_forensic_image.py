import os
import subprocess
from datetime import datetime

def create_disk_image():
    # Create a 10MB disk image
    subprocess.run(['dd', 'if=/dev/zero', 'of=files/forensic_image.dd', 'bs=1M', 'count=10'])
    
    # Create a temporary directory to store our files
    os.makedirs('temp_files', exist_ok=True)
    
    # Create some dummy files including our flag
    with open('temp_files/secret.txt', 'w') as f:
        f.write('flag{forensics_investigation_success_2024}')
    
    with open('temp_files/readme.txt', 'w') as f:
        f.write('This is a dummy file to make the investigation more interesting')
    
    # Create a file system in the disk image
    subprocess.run(['mkfs.ext4', 'files/forensic_image.dd'])
    
    # Mount the disk image
    os.makedirs('mount_point', exist_ok=True)
    subprocess.run(['sudo', 'mount', 'files/forensic_image.dd', 'mount_point'])
    
    # Copy files to the mounted disk image
    subprocess.run(['sudo', 'cp', '-r', 'temp_files/*', 'mount_point/'])
    
    # Delete the flag file (but it's still recoverable)
    subprocess.run(['sudo', 'rm', 'mount_point/secret.txt'])
    
    # Unmount the disk image
    subprocess.run(['sudo', 'umount', 'mount_point'])
    
    # Clean up
    subprocess.run(['rm', '-rf', 'temp_files'])
    subprocess.run(['rm', '-rf', 'mount_point'])
    
    print("Forensic disk image created at files/forensic_image.dd")

if __name__ == "__main__":
    # Ensure the files directory exists
    os.makedirs('files', exist_ok=True)
    create_disk_image() 