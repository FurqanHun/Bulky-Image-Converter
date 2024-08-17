from PIL import Image
import os

def convert_images(input_folder, output_folder, output_format, quality):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.webp', '.ico')):
            img_path = os.path.join(input_folder, filename)
            try:
                with Image.open(img_path) as img:
                    output_filename = os.path.splitext(filename)[0] + f'.{output_format}'
                    output_path = os.path.join(output_folder, output_filename)
                    if quality is None:
                        img.save(output_path, output_format.upper())
                    else:
                        img.save(output_path, output_format.upper(), quality=quality)

                    print(f'Converted {filename} to {output_filename} with quality {quality if quality is not None else "original"}')
            except (IOError, OSError) as e:
                print(f'Error converting {filename}: {e}')
        else:
            print(f'{filename} is not in supported static image format!!!')

def get_quality_setting():
    print("Select the desired quality setting:")
    print("1. Same quality as original (Original here means, quality closest to given format)")
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
    print("---------------Bulk Image Converter - 0xQan - v0.4---------------")
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

    print("Supported (static image) formats to convert to:")
    for i, format in enumerate(supported_formats, start=1):
        print(f"{i}. {format.upper()}")

    choice = input("Enter the number corresponding to the desired output format: ")

    while not choice.isdigit() or int(choice) < 1 or int(choice) > len(supported_formats):
        print("Ayo don't try to outsmort me. Select a valid number from the list.")
        choice = input("Enter the number corresponding to the desired output format: ")

    output_format = supported_formats[int(choice) - 1]
    quality = get_quality_setting()

    print(f"Input folder: '{input_folder}'")
    print(f"Output folder: '{output_folder}'")
    print(f"Output format: '{output_format}'")
    print(f"Quality setting: {quality if quality is not None else 'original'}")

    convert_images(input_folder, output_folder, output_format, quality)
