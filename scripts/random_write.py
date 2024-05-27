import os
import random

source_dir = '.\\NBTData'
target_dir = 'C:\\Users\\batch_kl6edmc\\AppData\\Roaming\\Citra\\load\\mods\\00040000001B8700\\romfs\\structures\\mansion'

source_files = [os.path.join(source_dir, f'n{i}.nbt') for i in range(1, 12)]
target_files = [os.path.join(target_dir, f) for f in os.listdir(target_dir) if os.path.isfile(os.path.join(target_dir, f))]

def read_file(file_path):
    with open(file_path, 'rb') as file:
        return file.read()

def write_file(file_path, data):
    with open(file_path, 'wb') as file:
        file.write(data)

for target_file in target_files:
    source_file = random.choice(source_files)
    data = read_file(source_file)
    write_file(target_file, data)
    print(f"Overwritten {target_file} with data from {source_file}")
