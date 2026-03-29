import multiprocessing
import subprocess

# To run Raphael
def startalexa():
    print("Process 1 (Raphael) is running.")
    from main import start
    start()

# To run hotword detection
def listenHotword():
    print("Process 2 (Hotword) is running.")
    from engine.features import hotword
    hotword()

if __name__ == '__main__':
    multiprocessing.freeze_support()  # Required for Windows

    # Create processes
    p1 = multiprocessing.Process(target=startalexa)
    p2 = multiprocessing.Process(target=listenHotword)

    # Start both processes
    p1.start()
    # Run the batch file synchronously (optional)
    subprocess.call([r'device.bat'])

    p2.start()

    

    # Wait for Raphael process to complete
    p1.join()

    # Clean up hotword process if still running
    if p2.is_alive():
        p2.terminate()
        p2.join()

    print("System stopped.")
