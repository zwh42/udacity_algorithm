import os
class FindFiles:

    def __init__(self):
        #self.suffix = suffix
        #self.path = path
        self.found_file_list = []

    
    def traverse(self, suffix, path):
        file_list, dir_list = self.seprate_file_and_dir(path)
        filtered_files = [f for f in file_list if os.path.splitext(f)[1] == suffix]
        self.found_file_list += filtered_files

        for dir in dir_list:
            self.traverse(suffix, dir)
    
    def find_files(self, suffix, path):
        if not os.path.isdir(path):
            print("{} is not a valid directory!".format(path))
            return
        
        if suffix == "":
            print("input suffix is empty!")
            return 
        
        self.traverse(suffix, path)

        return self.found_file_list
        
        

    
    def seprate_file_and_dir(self, path):
        file_list, dir_list = [], []
        for item in os.listdir(path):
            item = os.path.join(path, item)
            if os.path.isfile(item):
                file_list.append(item)
            elif os.path.isdir(item):
                dir_list.append(item)
        
        return file_list, dir_list


    
        

    




if __name__ == "__main__":
    print("\ntest case 1:\n")
    test_path = r"./testdir/"
    test_suffix = r".c"
    Test = FindFiles()
    found_file_list = Test.find_files(test_suffix, test_path)

    truth_list = []
    for r, d ,f in os.walk(test_path):
        for file in f:
            if file.endswith(test_suffix): 
                truth_list.append(os.path.join(r, file))   
    
    print(found_file_list)
    print(truth_list)

    assert sorted(found_file_list) == sorted(truth_list)


    print("\ntest case 2")
    test_path = r"non/exist/path"
    test_suffix = r".h"
    Test = FindFiles()
    found_file_list = Test.find_files(test_suffix, test_path)


    print("\ntest case 3")
    test_path = r"./testdir/"
    test_suffix = ""
    Test = FindFiles()
    found_file_list = Test.find_files(test_suffix, test_path)
     