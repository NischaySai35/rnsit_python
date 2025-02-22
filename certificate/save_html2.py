
html_template = '''
<html>
<body>
    <h1>USN: {{usn}} </h1>
    <h2>Name: {{name}} </h2>
</body>
</html>
'''
def replace_html_variables(template_file, output_file, variables):
    try:
        with open(template_file, 'r') as file:
            html_content = file.read()

        for key, value in variables.items():
            placeholder = f"{{{{{key}}}}}"
            html_content = html_content.replace(placeholder, value)

        with open(output_file, 'w') as file:
            file.write(html_content)
        
        print(f"HTML file with replaced values has been saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

template_file = input('Enter template html fileName(with extension): ')
output_file = input('Enter output html file name(with extension): ')

with open(template_file, 'w') as fp:
	fp.write(html_template)

usn = input('Enter USN of the student: ')
name = input('Enter Name of the student: ')

variables = {
    'usn': usn, 
    'name': name
}

replace_html_variables(template_file, output_file, variables)
