
html_template = '''
<html>
<body>
    <h2>USN: {{usn}} </h2>
    <h2>Name: {{name}}</h2>
</body>
</html>
'''
def replace_html_variables(output_file, variables):
    html_content = html_template
    try:
        for key, value in variables.items():
            placeholder = f"{{{{{key}}}}}" 
            html_content = html_content.replace(placeholder, value)

        with open(output_file, 'w') as file:
            file.write(html_content)
        
        print(f"HTML file with replaced values has been saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

output_file = input('Enter html file name(with extension .html): ')

usn = input('Enter USN of the student: ')
name = input('Enter Name of the student: ')

variables = {
    'usn': usn, 
    'name': name
}

replace_html_variables(output_file, variables)
