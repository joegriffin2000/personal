import os

filename = os.path.basename(__file__)[:-3]

#grabs the files ending in py from the directory
python_files = [i for i in os.listdir() if i.endswith(".py")]

#edit the names to exclude the .py (also exclude the filename of this file)
import_names = [i[:-3] for i in python_files if i[:-3] != filename]

#import all of the files using the __import__ builtin function
[__import__(i) for i in import_names]

# Below you can now start creating functions that import any of the imports by name
class ImportedFile():
    def __init__(self,filename:str):
        if filename in python_files or filename in import_names:
            self.__filename__ = filename
        else:
            return FileNotFoundError(f"{filename} does not exist in the directory")
        
    def run(self,func):
        return filename.func()
    
if __name__ == "__main__":
    print(import_names)
    file = ImportedFile(import_names[0])