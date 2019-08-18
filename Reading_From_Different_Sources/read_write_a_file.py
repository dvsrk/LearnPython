"""
    python read from a file,
    1) Open the file in one of the defined modes. This will return file object.
    2) call .read or .write functions on the file depneding on the need.
    Modes:
        ‘r’ – Read mode which is used when the file is only being read 
        ‘w’ – Write mode which is used to edit and write new information to the file (any existing files with the same name will be erased when this mode is activated) 
        ‘a’ – Appending mode, which is used to add new data to the end of the file; that is new information is automatically amended to the end 
        ‘r+’ – Special read and write mode, which is used to handle both actions when working with a file 

    file = open("<file_name>", "r")

    
"""
