
# slashes may need to change for MacOS or Linux
# import shutil with shutil we can take entire directory and zip it
# shutil.make_archive(output_filename,'zip',directory_to_zip)
import zipfile

# This module is used to zip and unzip files
# and to work with the files
f = open("new_file.txt", 'w+')
f.write("Here is some text")
f.close()

# slashes may need to change for MacOS or Linux
f = open("new_file2.txt", 'w+')
f.write("Here is some text")
f.close()


# Create Zip file first, then write to it(the write step compresses the files.)

comp_file = zipfile.ZipFile('comp_file.zip', 'w')
comp_file.write("new_file.txt", compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('new_file2.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

zip_obj = zipfile.ZipFile('comp_file.zip', 'r')
zip_obj.extractall("extracted_content")
