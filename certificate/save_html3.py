

def replace_html_variables(template_file, output_file, variables):
    try:
        # Read the HTML template
        with open(template_file, 'r') as file:
            html_content = file.read()

        # Replace the variables in the template
        for key, value in variables.items():
            placeholder = f"{{{{{key}}}}}"  # Create the placeholder in the format {{key}}
            html_content = html_content.replace(placeholder, value)

        # Write the updated HTML to the output file
        with open(output_file, 'w') as file:
            file.write(html_content)
        
        print(f"HTML file with replaced values has been saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")





# Example usage
template_file = 'template.html'  # Path to the template HTML file
output_file = 'output.html'      # Path to save the generated HTML file

# Variables to replace in the template
variables = {
    'name': 'John Doe',           # Replacing {{name}} with 'John Doe'
    'message': 'This is a dynamic message.'  # Replacing {{message}} with the custom message
}

# Call the function to replace variables and generate the new HTML
replace_html_variables(template_file, output_file, variables)
