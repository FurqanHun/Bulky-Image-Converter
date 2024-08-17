from PIL import Image
import os

def convert_images(input_folder, output_folder, output_format):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.webp', '.ico')):
            img_path = os.path.join(input_folder, filename)
            try:
                with Image.open(img_path) as img:
                    output_filename = os.path.splitext(filename)[0] + f'.{output_format}'
                    output_path = os.path.join(output_folder, output_filename)
                    img.save(output_path, output_format.upper())

                    print(f'Converted {filename} to {output_filename}')
            except (IOError, OSError) as e:
                print(f'Error converting {filename}: {e}')
        else:
            print(f'{filename} is not in supported static image format!!!')

if __name__ == '__main__':
    print("---------------Bulk Image Converter - 0xQan - v0.3---------------")
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

    print(f"Input folder: '{input_folder}'")
    print(f"Output folder: '{output_folder}'")
    print(f"Output format: '{output_format}'")

    convert_images(input_folder, output_folder, output_format)
