import time
import subprocess

def start_capture(capture_file):    
    print(f"Starting network capture, saving to {capture_file}...")

    tshark_process = subprocess.Popen(
        ["tshark", "-w", capture_file],  # Capture packets to the specified file
        stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )

    return tshark_process

def stop_capture(tshark_process):
    print("Stopping network capture...")

    tshark_process.terminate()
    tshark_process.wait()

if __name__ == "__main__":
    print("Inside the wireshark capture scritp of the database server!!!")

    capture_file = "/home/sarahwilliams/networkCapture/email_and_db/email_and_db.pcap"

    print("Call the function to start the capture")
    tshark_process = start_capture(capture_file)

    time.sleep(7)

    input("\nPress the ENTER key to stop the capture on the database server...\n")

    print("Call the function to stop the capture")
    stop_capture(tshark_process)
