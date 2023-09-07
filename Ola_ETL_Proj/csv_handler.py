from os import listdir

def get_csv_files_as_list():
    filenames = listdir('csv_files')
    return filenames

# inspired by:
# https://stackoverflow.com/questions/9234560/find-all-csv-files-in-a-directory-using-python#:~:text=from%20os%20import%20listdir%0A%0Adef%20find_csv_filenames(%20path_to_dir%2C%20suffix%3D%22.csv%22%20)%3A%0A%20%20%20%20filenames%20%3D%20listdir(path_to_dir)%0A%20%20%20%20return%20%5B%20filename%20for%20filename%20in%20filenames%20if%20filename.endswith(%20suffix%20)%20%5D

