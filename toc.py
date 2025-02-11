from pypdf import PdfWriter, PdfReader

"""
Function to add table of contents data (provided as a tuple) to the bookmark data of an input pdf by 
copying pages to output_pdf and including bookmark data

input_pdf: Path to original pdf
output_pdf: Path to new pdf that will be created
tupl_toc: List of tuples of table of contents information in format [("Chapter Name", page_number), ("Next Chapter", page_nuber)]
"""
def add_toc(input_pdf, output_pdf, tupl_toc, newFileBool):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    n = len(reader.pages)

    valid_toc = [(title, page) for title, page in tupl_toc if page and page <= n]

    for (title, page) in valid_toc:
        writer.add_outline_item(title, page - 1)

    
    if newFileBool:
        with open(output_pdf, "wb") as f:
            writer.write(f)
        print("Updated as", output_pdf)
    else: 
        with open(input_pdf, "wb") as f:
            writer.write(f)
        print("Updated as", input_pdf)


if __name__ == "__main__":
    # pdfIn = "/Users/shaurya/Development/temp/CC205c.pdf"
    # pdfOut = "/Users/shaurya/Development/temp/toc.pdf"
    pdfIN = "./CC205c.pdf"
    pdfOUT = "./CC205 with TOC.pdf"

    toc_tuple = [
        ("Chapter 1: A Brief History of Organized Crime in Canada", 3),
        ("Chapter 2: Defining and Conceptualizing Organized Crime", 28),
        ("Chapter 3: Describing Organized Crime: Identifying and Classifying Dominant Characteristics", 69),
        ("Chapter 4: Theories of Organized Crime", 98),
        ("Chapter 5: Italian Organized Crime", 144),
        ("Chapter 6: Chinese Organized Crime", 186),
        ("Chapter 7: English and French Canadian Outlaw Motorcycle Gangs", 232),
        ("Chapter 8: Other Organized Criminal Associations in Canada", 278),
        ("Chapter 9: Predatory Crimes", 330),
        ("Chapter 10: Consensual Crimes", 363),
        ("Chapter 11: Drug Trafficking", 389),
        ("Chapter 12: Organized Crime Control in Theory: Theoretical Overview, Concepts, Objectives, and Strategies", 438),
        ("Chapter 13: Organized Crime Control in Practice: Criminal Law and Enforcement Agencies in Canada", 481),
        ("Conclusion: Is There a Distinctively Canadian Version of Organized Crime?", 522),
        
    ]

    newFileBool = True if input("Would you like to create a new file or modify the original? (enter Y/N): ").strip().lower() == "y" else False

    add_toc(pdfIN, pdfOUT, toc_tuple, newFileBool)