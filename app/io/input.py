import pandas

def input_from_console():
    """
    Prompts the user for text via console input..

    Returns:
        str: Text entered by the user.
    """
    text = input("Enter a text: ")
    return text

def read_file(file_path):
    """
    Reads text from a file at the specified path using standard Python tools.

    Args:
        file_path (str): File path.

    Returns:
        str: File contents as a string.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
    return text

def read_file_pandas(file_path):
    '''
    Reads text from a file at the specified path using pandas.

    Args:
        file_path (str): File path.

    Returns:
        pandas.DataFrame: File contents as a dataframe.
    '''
    text = pandas.read_csv(file_path, encoding="utf-8")
    return text