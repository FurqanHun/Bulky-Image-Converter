# Bulky Image Converter

The name's a joke but the real purpose of this script is to convert images in bulk.

## Installation

It doesn't require any installation. Just clone the repository and run the script. It relies on the `Pillow` library which is a fork of the `PIL` library and is installed by default on many linux distros.

If you don't have it installed, you can install it using pip:
```bash
pip install pillow
```
You do need python 3.x to run the script.

## Usage
Follow the prompts after running the script.
```bash
python bulky_launcher.py
```
You can also run the scripts directly. The launcher is there to make it easier to choose between the single and multi process scripts.
```bash
python bulky_image_converter.py
```
or
```bash
python multi_process_bulky_image_converter.py
```
## Liscense
This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Note
I do want to add more things, like using multiprocess, pool, a compression at the cost of quality option, etc. But I'm too lazy to do it right now. Maybe in the future.
Also, I'm not sure if the script works on Windows, Like by the way its written it should work on any OS but I haven't tested it on anything else than Linux (Fedora 40).
I was gonna make it so it replaces the images in the same directory but then realised some idiot (me) might accidentally run it in the wrong directory.
BTW, this script is supposed to me trying not to convert images in bulk manually. I'm not sure if it's faster than doing it manually but it's definitely less brain numbing.

*PS. alright so i've added multiporcess script and a launcher to allow users to choose between single and multi process. I've also added a compression option. If you've any suggestions or want to contribute, feel free to do so. I like programming but i hate coding. I'm not sure if that makes sense but it does to me.*

## Author
- [0xQan](https://github.com/furqanhun)
