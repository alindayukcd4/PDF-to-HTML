import fitz  # PyMuPDF
from bs4 import BeautifulSoup

def pdf_to_html(pdf_path, html_path):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)

    # Create BeautifulSoup object to store HTML content
    html_content = BeautifulSoup()

    # Iterate through each page in the PDF
    for page_number in range(pdf_document.page_count):
        # Get the page
        page = pdf_document[page_number]

        # Extract text from the page
        text = page.get_text("text")

        # Create a new HTML tag for the page
        page_tag = html_content.new_tag("div", attrs={"class": "page"})
        page_tag.string = text
        html_content.append(page_tag)

    # Save the HTML content to a file
    with open(html_path, "w", encoding="utf-8") as html_file:
        html_file.write(str(html_content))

    # Close the PDF document
    pdf_document.close()

if __name__ == "__main__":
    pdf_file_path = "C:\\cengage\\content_sets\\Cali\\capture\\temp\\ca.2023a0001.pdf"
    html_file_path = "C:\\Users\\e756212\\Documents\\output.html"

    pdf_to_html(pdf_file_path, html_file_path)
