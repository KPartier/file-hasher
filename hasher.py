import os
import hashlib
import csv
 
 
# Gets all directories from directories.txt, then loops through every file in every directory and returns the absolute path of each file.

def get_file_list():
    
    full_directory_list = []
    
    with open('directories.txt', 'r') as directory_file:
        directories = directory_file.read()
        directories = directories.strip()
        directories = directories.replace('"', '')
        directories_list = directories.split("\n")
    
    full_directory_list = directories_list
    
    print(full_directory_list)
    
    paths = []
    
    for directory in full_directory_list:
        for dirpath,_,filenames in os.walk(directory):
            for f in filenames:
                paths.append(os.path.abspath(os.path.join(dirpath, f)))
         
    return paths


# Hash functions for individual files; reads in small chunks to avoid memory issues.

# SHA256

def sha256_checksum(filename, block_size=65536):
    sha256 = hashlib.sha256()
    with open(filename, 'rb') as file:
        for block in iter(lambda: file.read(block_size), b''):
            sha256.update(block)
    
    return sha256.hexdigest()

# MD5
def md5_checksum(filename, block_size=65536):
    md5 = hashlib.md5()
    with open(filename, 'rb') as file:
        for block in iter(lambda: file.read(block_size), b''):
            md5.update(block)
    
    return md5.hexdigest()

algorithm = input("Enter the desired algorithm [md5, sha256]: ")

filelist = get_file_list()

if algorithm == "sha256":

    # Create a CSV file to store all hashes
    with open('sha256.csv', 'w', newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        
        for file in filelist:
            # Calculate hash
            checksum = sha256_checksum(file)
            print(algorithm + " " + checksum + " " + file)
            writer.writerow([algorithm, checksum, file])
            
            
    csvfile.close()
    
    print("=====================")
    print("SHA256 hashing complete.")
    print("=====================")
    

elif algorithm == "md5":

    # Create a CSV file to store all hashes
    with open('md5.csv', 'w', newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        
        for file in filelist:
            # Calculate hash
            checksum = md5_checksum(file)
            print(algorithm + " " + checksum + " " + file)
            writer.writerow([algorithm, checksum, file])
            
            
    csvfile.close()
    
    print("=====================")
    print("MD5 hashing complete.")
    print("=====================")

else:
    print("Invalid algorithm.")
    
