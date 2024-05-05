import os
import xml.etree.ElementTree as ET

def process_xml_file(file_path):

    tree = ET.parse(file_path)
    root = tree.getroot()

    for elem in root.iter():
       if elem.text and 'Cattle' in elem.text:
            elem.text = elem.text.replace('Cattle', 'cattle')
    tree.write(file_path)

def process_xml_files_in_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".xml"):
            file_path = os.path.join(directory, filename)
            process_xml_file(file_path)

dir = os.path.dirname(__file__)
process_xml_files_in_directory(dir)