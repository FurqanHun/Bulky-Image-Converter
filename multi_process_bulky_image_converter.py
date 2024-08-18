from PIL import Image
import os
from concurrent.futures import ProcessPoolExecutor, as_completed

def convert_images(input_folder, output_folder, output_format, quality, include_subdirs):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    tasks = []
    if include_subdirs:
        #directoreis their subdirectories n their subdirectories and so on
        for dirpath, _, filenames in os.walk(input_folder):
            tasks.extend(process_files(dirpath, filenames, input_folder, output_folder, output_format, quality))
    else:
        #files only
        for filename in os.listdir(input_folder):
            if os.path.isfile(os.path.join(input_folder, filename)):
                tasks.extend(process_files(input_folder, [filename], input_folder, output_folder, output_format, quality))

    return tasks

def process_files(dirpath, filenames, input_folder, output_folder, output_format, quality):
    tasks = []
    for filename in filenames:
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.webp', '.ico')):
            tasks.append((dirpath, filename, input_folder, output_folder, output_format, quality))
    return tasks

def convert_image(args):
    dirpath, filename, input_folder, output_folder, output_format, quality = args
    img_path = os.path.join(dirpath, filename)
    try:
        with Image.open(img_path) as img:
            #output directory structure
            relative_path = os.path.relpath(dirpath, input_folder)
            output_dir = os.path.join(output_folder, relative_path)
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)

            output_filename = os.path.splitext(filename)[0] + f'.{output_format}'
            output_path = os.path.join(output_dir, output_filename)
            if quality is None:
                img.save(output_path, output_format.upper())
            else:
                img.save(output_path, output_format.upper(), quality=quality)

            return f'Converted {filename} to {output_filename} with quality {quality if quality is not None else "original"}'
    except (IOError, OSError) as e:
        return f'Error converting {filename}: {e}'

def get_quality_setting():
    print("\nSelect the desired quality/compression setting:")
    print("1. Same quality as original")
    print("2. Default (Quality: 75)")
    print("3. Compress size but keep quality (Quality: 85)")
    print("4. Compress size more (Quality: 50)")

    while True:
        choice = input("Enter the number corresponding to the desired quality setting (if pressed enter, default is 75): ")
        if choice == '':
            return 75
        elif not choice.isdigit() or int(choice) < 1 or int(choice) > 4:
            print("Invalid choice. Please select a valid number from the list.")
        else:
            break

    if choice == '1':
        return None
    elif choice == '2':
        return 75
    elif choice == '3':
        return 85
    elif choice == '4':
        return 50

if __name__ == '__main__':
    print("---------------Bulky Image Converter - 0xQan - v0.5---------------")
    input_folder = input("Input Folder: ").strip().replace("'", "").replace('"', "")
    while not os.path.exists(input_folder):
        print("Invalid folder path. Please enter a valid folder path.")
        input_folder = input("Input Folder: ").strip().replace("'", "").replace('"', "")

    output_folder = input("Output Folder (optional): ").strip().replace("'", "").replace('"', "")
    if not output_folder:
        output_folder = input_folder + "_converted"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    supported_formats = ['png', 'jpg', 'jpeg', 'bmp', 'tiff', 'webp', 'ico']

    print("\nSupported (static image) formats to convert to:")
    for i, format in enumerate(supported_formats, start=1):
        print(f"{i}. {format.upper()}")

    choice = input("Enter the number corresponding to the desired output format: ")
    while not choice.isdigit() or int(choice) < 1 or int(choice) > len(supported_formats):
        print("\nAyo don't try to outsmort me. Select a valid number from the list.")
        choice = input("Enter the number corresponding to the desired output format: ")

    output_format = supported_formats[int(choice) - 1]
    quality = get_quality_setting()

    include_subdirs = input("\nIf the input folder contains subdirectories, you wanna convert images in em too? (yes/y for yes, anything else is taken as no): ").strip().lower()
    include_subdirs = include_subdirs in ['yes', 'y']

    print("\nConverting images...")
    print(f"Input folder: '{input_folder}'")
    print(f"Output folder: '{output_folder}'")
    print(f"Output format: '{output_format}'")
    print(f"Quality setting: {quality if quality is not None else 'original'}")
    print(f"Include subdirectories: {'Yes' if include_subdirs else 'No'}")
    print("Parallel processing: Enabled (High CPU usage, but faster conversion)...")
    print("\n")

    tasks = convert_images(input_folder, output_folder, output_format, quality, include_subdirs)

    #parallel conversion
    with ProcessPoolExecutor() as executor:
        futures = {executor.submit(convert_image, task): task for task in tasks}
        for future in as_completed(futures):
            print(future.result())

    print(f"\nConversion completed.!!! Check the {output_folder} folder for the converted images.!!!")
