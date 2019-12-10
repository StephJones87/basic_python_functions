# code for find available files within a directory using pathlib

from pathlib import Path
FILES_FOLDER = Path("../my_files/") 

available_files = [ item for item in FILES_FOLDER.iterdir() if item.is_file() ]
print('found', len(available_files), 'csv files containing stuff')
available_files

