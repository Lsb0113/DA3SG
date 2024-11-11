import os

# download dataset
count = 0
train_path='./data/3DSSG_subset/train_scans.txt'
val_path='./data/3DSSG_subset/validation_scans.txt'
with open(train_path, 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line)
        python_script = "download.py"
        argument = f"-o {'./data/3RScan/'} --id {str(line)}"

        os.system(f"python {python_script} {argument}")
        print(f'--------------{count}-----------------')
        count += 1
