# python program to merge multiple pdf files into one

from pypdf import PdfWriter  # pip install pypdf

def merge_pdfs(pdf_list, output_path):
    merger = PdfWriter()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output_path)
    merger.close()

'''
# Example usage
# Replace with your actual file names. Assuming they are in the same directory as this script. Else provide the full path.
pdf_files = ['file1.pdf', 'file2.pdf', 'file3.pdf']  
output_file = 'merged.pdf'
merge_pdfs(pdf_files, output_file)
print(f"Merged PDF saved as: {output_file}")
'''
