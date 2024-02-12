import os
import requests
import json
import stat

def get_directory_size(directory):
    """Get the total size of all files in the directory."""
    total_size = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            total_size += os.path.getsize(filepath)
    return total_size

def get_directory_permissions(directory):
    """Get the permissions of the directory."""
    permissions = stat.filemode(os.stat(directory).st_mode)
    return permissions

def post_to_registry(directory_info, registry_url):
    """Post the directory information to the data registry."""
    headers = {"Content-Type": "application/json"}
    response = requests.post(registry_url, headers=headers, data=json.dumps(directory_info))
    return response

def main():
    # Update this path to the path of your cloned sample data repository
    directory_to_scan = "/path/to/cloned/WEHI-demo-dataset"

    # Update this URL to the local URL of your teammate's sample web app
    registry_url = "http://localhost:8000/api/datasets"

    # Extract directory information
    directory_info = {
        "path": directory_to_scan,
        "size": get_directory_size(directory_to_scan),
        "permissions": get_directory_permissions(directory_to_scan)
    }

    response = post_to_registry(directory_info, registry_url)
    if response.status_code == 200:
        print(f"Successfully registered directory {directory_info['path']}")
    else:
        print(f"Failed to register directory {directory_info['path']}")

if __name__ == "__main__":
    main()
