import os
import zipfile

def walkFile(file):
    for root, dirs, files in os.walk(file):
        for d in dirs:
            if os.path.exists(os.path.join(root, d, 'sequence')): 
                continue
            else:  
                os.makedirs(os.path.join(root, d, 'sequence'))
                zip_path = os.path.join(root, d, 'sequence.zip')
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    zip_ref.extractall(os.path.join(root, d, 'sequence'))
                    os.remove(os.path.join(root, d, 'sequence.zip'))

walkFile("./data/3RScan")
