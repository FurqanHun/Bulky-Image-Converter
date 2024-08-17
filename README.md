# Bulky Image Generator

The name's a joke but the real purpose of this script is to convert images in bulk.

## Installation

It doesn't require any installation. Just clone the repository and run the script. It relies on the `Pillow` library which is a fork of the `PIL` library and is installed by default on many linux distros.

If you don't have it installed, you can install it using pip:
```bash
pip install pillow
```
## Usage
Follow the prompts after running the script.
```bash
python bulk_image_generator.py
```
## Liscense
This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Note
I do want to add more things, like using multiprocess, pool, a compression at teh cost of quality option, etc. But I'm too lazy to do it right now. Maybe in the future.
Also, I'm not sure if the script works on Windows, Like by the way its written it should work on any OS but I haven't tested it on anything else than Linux (Fedora 40).
I was gonna make it so it replaces the images in the same directory but then realised some idiot (me) might accidentally run it in the wrong directory.

## Author
- [0xQan](https://github.com/furqanhun)
