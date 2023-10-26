import subprocess
import os

powershell_path = r'C:\Program Files\PowerShell\7\pwsh.exe'

def get_hash(filepath):
    #process = subprocess.Popen([powershell_path, '-Command', r"& '7z' h -scrcSHA256 \'" + filepath + r" | Select-String -Pattern 'names:'"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    process = subprocess.Popen([powershell_path, '-Command', f"& '7z' h -scrcSHA256 \"{filepath}\" | Select-String -Pattern 'names:'"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    result = process.communicate()[0]
    return str(result)


def compare_folders(folder1, folder2):
    file_path1 = os.path.normpath(folder1)
    file_path2 = os.path.normpath(folder2)

    # MAKE THESE RUN IN PARALLEL
    hash1 = get_hash(file_path1)
    hash2 = get_hash(file_path2)

    return hash1, hash2, (hash1 == hash2)