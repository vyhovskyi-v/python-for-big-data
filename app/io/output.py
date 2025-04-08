
def output_in_console(text):
    '''
    Prints text to the console.

    Args:
        text(str): Text to be printed.
    '''
    print(text)

def write_in_file(file_path, text):
    '''
    Writes text to a file.

    args:
        file_path (str): Path to the file.
        text (str): Text to be written.
    '''
    with open(file_path, 'w', encoding="utf-8") as f:
        f.write(text)