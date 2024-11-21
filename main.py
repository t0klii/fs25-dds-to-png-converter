"""

Please give me some credit :(

https://www.youtube.com/@realt0kliiuwu
https://github.com/t0klii/fs25-dds-to-png-converter

speed of convertion depends on your cpu. if you have a strong cpu, it should take you around 5-10 minutes
i have a i7-8700 6 cores 3.2ghz, 12 threads and it took me almost 20 minutes
whole process reserved 4000mb of ram if u have less = gg

FS25 has like almost 21000 .dds files... be prepared...

"""

import os
from PIL import Image
import concurrent.futures

root_path = r"C:\Program Files (x86)\Steam\steamapps\common\Farming Simulator 25" #<-- replace this to your game path, example should be default

root_dir = rf"{root_path}\data"

def convert_file(file_path):
    img = Image.open(file_path)
    img.save(file_path.replace('.dds', '.png'))
    print(f'Converted {file_path} to .png')

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.dds'):
                file_path = os.path.join(root, file)
                executor.submit(convert_file, file_path)