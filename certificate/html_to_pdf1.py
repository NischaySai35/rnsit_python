from weasyprint import HTML

def html_to_pdf(input_html, output_pdf):
    try:
        # Convert HTML to PDF
        HTML(input_html).write_pdf(output_pdf)
        print(f"PDF saved as {output_pdf}")
    except Exception as e:
        print(f"An error occurred: {e}")

file_name = input('Enter name of the HTML file: ')
html_file = file_name + '.html'
output_pdf = file_name + '.pdf'
html_to_pdf(html_file, output_pdf)

