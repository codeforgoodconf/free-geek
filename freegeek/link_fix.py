import os.path
from settings import BASE_DIR as BASE_DIR

LIST_OF_FILES = ["README.rst"]

def replace_links(file):
    """Replaces relative links with links to files in Github's master branch.
    It changes "</", into "<https://github.com/neex-io/free-geek/tree/master/"
    """
    file = os.path.join(BASE_DIR, "docs", file) 

    doc_file = open(file, "r")

    doc_data = doc_file.read()
    doc_data = doc_data.replace(
        "</", "<https://github.com/neex-io/free-geek/tree/master/")
    doc_file.close()

    doc_file = open(file, "w")
    doc_file.write(doc_data)
    doc_file.close()


def main():
    """Fixes relative links in given .rst files.
    """
    for file in LIST_OF_FILES:
        replace_links(file)

if __name__ == "__main__":
    main()
