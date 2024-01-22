import os
import requests
import json

def scan_directory(directory):
    """Scan the directory and return a list of file paths."""
    file_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_paths.append(os.path.join(root, file))
    return file_paths

def extract_metadata(file_path):
    """Extract and return metadata from the file."""
    # Example metadata: file name and size
    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)
    return {"name": file_name, "size": file_size}

def post_to_registry(metadata, registry_url):
    """Post the metadata to the data registry."""
    headers = {"Content-Type": "application/json"}
    response = requests.post(registry_url, headers=headers, data=json.dumps(metadata))
    return response

def main():
    # Update this path to the path of your cloned sample data repository
    directory_to_scan = "/path/to/cloned/WEHI-demo-dataset"

    # Update this URL to the local URL of your teammate's sample web app
    registry_url = "http://localhost:8000/api/datasets"

    for file_path in scan_directory(directory_to_scan):
        metadata = extract_metadata(file_path)
        response = post_to_registry(metadata, registry_url)
        if response.status_code == 200:
            print(f"Successfully registered {metadata['name']}")
        else:
            print(f"Failed to register {metadata['name']}")

if __name__ == "__main__":
    main()
