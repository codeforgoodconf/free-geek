import os.path

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# print(BASE_DIR)
# os.path.join(dir_name, base_filename + "." + filename_suffix)


def replace_links(file):
    """
    """
    file = os.path.join(BASE_DIR, "docs", file) 

    doc_file = open(file, "r")

    doc_data = doc_file.read()
    doc_data = doc_data.replace(
        "</", "<https://github.com/neex-io/free-geek/tree/master")
    doc_file.close()

    doc_file = open(file, "w")
    doc_file.write(doc_data)
    doc_file.close()


def fix_all():
    """
    """
    list_of_files = ["README.rst"]
    
    for file in list_of_files:
        replace_links(file)


if __name__ == "__main__":
    fix_all()
