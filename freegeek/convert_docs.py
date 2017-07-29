import os.path
import pypandoc

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = ["README.md", "CHANGES.md", "AUTHORS.md", "LICENSE"]

def convert_file(file):
    """Converts .md to .rst and moves to docs folder.
    """
    output_file_with_ext = file[:-3] + ".rst"
    input_file = os.path.join(BASE_DIR, file)
    output_file = os.path.join(BASE_DIR, "docs", output_file_with_ext)
    pypandoc.convert_file(input_file, "rst", outputfile=output_file)

def copy_license(file):
    """Adds .txt extension to LICENSE and moves it to docs folder.
    """
    input_file = os.path.join(BASE_DIR, file)
    output_file = os.path.join(BASE_DIR, "docs", file + ".txt")

    file_in = open(input_file, "r")
    file_data = file_in.read()
    
    file_out = open(output_file, "w+")
    file_out.write(file_data)
    file_out.close()

def main():
    """Converts and moves specified files (FILES) to docs folder.
    Markdown files are converted to reStructuredText. 
    LICENSE (that has no extension) is turned into a text file (.txt)
    """
    for file in FILES:
        if file != "LICENSE":
            convert_file(file)
        else:
            copy_license(file)

if __name__ == "__main__":
    main()
