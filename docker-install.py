import subprocess
import time

def install_docker():
    try:
        # Install Docker
        install_command = "sudo apt-get update && sudo apt-get install -y docker.io"
        subprocess.run(install_command, shell=True, check=True)
        
        # Start Docker
        start_command = "sudo systemctl start docker"
        subprocess.run(start_command, shell=True, check=True)

        print("Docker installation and startup initiated. Waiting for Docker to start...")

        # Check Docker status every 2 seconds, waiting up to 60 seconds
        max_wait_time = 60
        interval = 2
        start_time = time.time()
        while time.time() - start_time < max_wait_time:
            status_command = "sudo systemctl is-active docker"
            status_process = subprocess.Popen(status_command, shell=True, stdout=subprocess.PIPE)
            status_output = status_process.communicate()[0].decode("utf-8").strip()
            
            if status_output == "active":
                print("Docker has started successfully.")
                return
            time.sleep(interval)

        print("Timed out while waiting for Docker to start. Check Docker status manually.")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        print("Docker installation and startup failed.")

if __name__ == "__main__":
    install_docker()

