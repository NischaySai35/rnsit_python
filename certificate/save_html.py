
html_code = '''
<html>
	<body>
		<h2> Hello World </h2>
	</body>
</html>
'''

file_name = input('Enter name of the file: ') # anand.html

with open(file_name, 'w') as fp:
	fp.write(html_code)




