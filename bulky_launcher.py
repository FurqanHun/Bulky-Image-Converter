import os
import subprocess
import atexit
import psutil
import signal

def byebye():
    kill_process_by_name('multi_process_bulky_image_converter.py')
    kill_process_by_name('bulky_image_converter.py')
    print("All done! Exiting...")

atexit.register(byebye)

def kill_process_by_name(process_name):
    for proc in psutil.process_iter(['pid', 'name']):
        if process_name in proc.info['name']:
            os.kill(proc.info['pid'], signal.SIGTERM)

def main():
    print("---------------[Launcher]Bulky Image Converter - 0xQan - v0.5---------------")
    choice = input("Do you want to use multiprocessing for image conversion? (yes/y for yes, anything else for no): ").strip().lower()

    if choice in ['yes', 'y']:
        print("Starting the multi-process image converter...")
        subprocess.run(['python', 'multi_process_bulky_image_converter.py'])
    else:
        print("Starting the single-threaded image converter...")
        subprocess.run(['python', 'bulky_image_converter.py'])

if __name__ == '__main__':
    main()
