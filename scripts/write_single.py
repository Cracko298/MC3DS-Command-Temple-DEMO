import os

source_file = ".\\NBTData\\new_stuff.nbt"
target_directory = "C:\\Users\\batch_kl6edmc\\AppData\\Roaming\\Citra\\load\\mods\\00040000001B8700\\romfs\\Command_Block_Temple\\structures\\mansion"

with open(source_file, 'rb') as src_file:
    data = src_file.read()

for filename in os.listdir(target_directory):
    file_path = os.path.join(target_directory, filename)
    
    if os.path.isfile(file_path):
        with open(file_path, 'wb') as tgt_file:
            tgt_file.write(data)

print("Data from 'new_stuff.nbt' has been written to all files in the directory.")
