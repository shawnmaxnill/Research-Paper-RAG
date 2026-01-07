import os
import shutil

class FileManager:

    def __init__(self, base_dir="data/papers"):
        self.base_dir = base_dir
        os.makedirs(self.base_dir, exist_ok=True)

    def addFiles(self, src_path):
        if not os.path.isfile(src_path):
            print("File/Path does not exist!!!")
            return
        
        filename = os.path.basename(src_path)
        destination = os.path.join(self.base_dir, filename)
        shutil.copy2(src_path, destination)
        print(f"{filename} successfully added!")

    def removeFiles(self, filename):
        path = os.path.join(self.base_dir, filename)
        if not os.path.isfile(path):
            print("File does not exist!!!")
            return
        
        os.remove(path)
        print(f"{filename} successfully removed!")

    def listFiles(self):
        files = os.listdir(self.base_dir)
        if not files:
            print("No files exists!")
            return
        
        print("----- Files -----")
        for f in files:
            print(" -", f)

    def menu(self):
        print("\n--- File Manager ---")
        print("Please type in a number")
        print("1. List files")
        print("2. Add file")
        print("3. Remove file")
        print("4. Exit")

    def run(self):
        while True:
            self.menu()
            usr_inp = input("Choose an option: ").strip()

            match usr_inp:
                case "1":
                    self.listFiles()

                case "2":
                    path = input("Please input path to file: ").strip()
                    self.addFiles(path)

                case "3":
                    filename = input("Please input name of file: ").strip()
                    self.removeFiles(filename)

                case "4":
                    print("Exiting")
                    break

                case _:
                    print("Invalid Selection")

if __name__ == "__main__":
    fm = FileManager()
    fm.run()