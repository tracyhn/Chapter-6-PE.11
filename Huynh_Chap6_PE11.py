#=======================================================================================
#Author:        Tracy Huynh
#Program ID:    Huynh_Chap6_PE11.py
#Due Date:      05/06/2019
#Description:   This program prompts the user to enter their name and
#               personal description. Using the user's inputs, the program
#               then opens a file to write html codes in order to display
#               the user's information on a web page.
#=======================================================================================

# Define main function
def main():

    # Get name and description from user
    name = input("Enter your name: ")
    description = input("Describe yourself: ")

    # Create an html file by opening it in mode 'w'
    outfile = open("my_page.html", "w")

    # Call write_html_file function
    # and passing three arguments
    write_html_file(name,description,outfile)

    # Close the file
    outfile.close()

# Define write_html_file function
def write_html_file(n, d, file):

    # Write <html> tag
    file.write("<html>\n")

    # Call write_html_head function and pass an argument
    write_html_head(file)

    # Call write_html_body and pass three arguments
    write_html_body(n,d,file)

    # Write </html> tag
    file.write("</html>\n")

def write_html_head(f):

    # Write the head and title tags
    f.write("<head>\n")
    f.write("<title>My Personal Web Page</title>\n")
    f.write("</head>\n")

def write_html_body(head, body, f):

    # Write the body, center, h1,
    # name and description
    f.write("<body>\n")
    f.write("\t<center>\n")
    f.write("\t\t<h1>" + head + "</h1>\n")
    f.write("\t</center>\n")
    f.write("\t<hr />\n")
    f.write("\t" + body + "\n")
    f.write("\t<hr />\n")
    f.write("</body>\n")

# Call the main function
main()
    
    
    
    


    

    
    

    
