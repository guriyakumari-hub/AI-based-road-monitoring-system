import os
import subprocess
import urllib.request
import sys

def main():
    print("Installing requirements...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    
    weights_path = os.path.join("models", "yolov3.weights")
    if not os.path.exists(weights_path) or os.path.getsize(weights_path) < 1000000:
        print("Downloading YOLOv3 weights (this may take a while)...")
        url = "https://pjreddie.com/media/files/yolov3.weights"
        urllib.request.urlretrieve(url, weights_path)
        print("Downloaded YOLOv3 weights.")
    else:
        print("YOLOv3 weights already present.")
        
    print("Running main.py...")
    subprocess.check_call([sys.executable, "src/main.py"])

if __name__ == "__main__":
    main()
