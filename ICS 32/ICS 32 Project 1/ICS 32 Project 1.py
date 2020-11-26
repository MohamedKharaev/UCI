# Mohamed Kharaev 43121144 & Yiqing Yang 26503330
# Project 1
from pathlib import Path
import os
import shutil
import time

def input_directory_path() -> Path:
    '''Accesses a directory provided by the user'''
    given_path = Path(input())
    if given_path.exists() and given_path.is_dir():
        print(given_path)
        return given_path
    else:
        print("ERROR")
        return input_directory_path()


def find_files_by_name(name: str, directory: Path) -> 'List of Paths':
    '''Returns a list of files with a specified name from a directory'''
    return_files = list()
    for file in directory.iterdir():
        if file.is_dir():
            try:
                return_files.extend(find_files_by_name(name, file))
            except:
                continue
        if file.is_file():            
            if str(file)[-len(name):] == name:
                return_files.append(file)
    return return_files
    

def find_files_by_extension(extension: str, directory: Path) -> 'List of Paths':
    '''Returns a list of files with specified extensions from a directory'''
    return_files = list()
    for file in directory.iterdir():
        if file.is_dir():
            try:
                return_files.extend(find_files_by_extension(extension, file))
            except:
                continue
        if file.is_file():
            if extension[0] == '.':
                if file.suffix == extension:
                    return_files.append(file)
            elif extension[0] != '.':
                if file.suffix[1:] == extension[1:]:
                    return_files.append(file)
    return return_files


def find_files_by_size(size: int, directory: Path) -> 'List of Paths':
    '''Returns a lis of files bigger than specified size from a directory'''
    return_files = list()
    for file in directory.iterdir():
        if file.is_dir():
            try:
                return_files.extend(find_files_by_size(size, file))
            except:
                continue
        if file.is_file():
            if os.path.getsize(file) > size:
                return_files.append(file)
    return return_files


def search_file_with_characteristics(directory: Path) -> 'List of Files and Directories':
    '''Searches for files and directories with specified characteristics within a provided path'''
    files_list = list()
    command = input()
    while len(command) < 2:
        print("ERROR")
        command = input()
    characteristic = command[0]
    value = command[2:]
    if characteristic == 'N':
        files_list.extend(find_files_by_name(value, directory))
    elif characteristic == 'E':
        files_list.extend(find_files_by_extension(value, directory))
    elif characteristic == 'S':
        try:
            files_list.extend(find_files_by_size(int(value), directory))
        except ValueError:
            print("ERROR")
            files_list = search_file_with_characteristics(directory)
    else:
        print("ERROR")
        files_list = search_file_with_characteristics(directory)
    
    return files_list


def print_path(path: Path) -> None:
    '''Prints the given path in a string format'''
    print(str(path))


def print_first_line_of_file(path: Path) -> None:
    '''Print the first line of a given file'''
    try:
        openned_file = path.open()
        print(openned_file.readline(), end = '')
    except:
        pass
    finally:
        openned_file.close()

            
def copy_file(file: Path) -> None:
    '''Copies files with '.dup' at the end of the name. If file.dup exists already, makes file.dup.dup'''
    copy_file_path = Path(str(file) + '.dup')
    try:
        if copy_file_path.exists():
            copy_file(copy_file_path)
        else:
            shutil.copyfile(file, copy_file_path)
    except:
        pass

    
def touch_file(file: Path) -> None:
    '''Changes the last modified time of a file to the current time'''
    try:
        os.utime(file)
    except:
        pass


def perform_action(files: 'List of Paths') -> None:
    '''Performs an action provided by the user'''
    action = input()
    if action == 'P':
        for file in files:
            print_path(file)
    elif action == 'F':
        for file in files:
            print_path(file)
            print_first_line_of_file(file)
    elif action == 'D':
        for file in files:
            print_path(file)
            copy_file(file)
    elif action == 'T':
        for file in files:
            print_path(file)
            touch_file(file)
    else:
        print("ERROR")
        perform_action(files)

        
                
if __name__ == '__main__':
    path = input_directory_path()
    searched_files = search_file_with_characteristics(path)
    perform_action(searched_files)

    
