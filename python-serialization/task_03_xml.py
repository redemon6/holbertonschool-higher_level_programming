#!/usr/bin/python3
import xml.etree.ElementTree as ET 
def serialize_to_xml(dictionary, filename):
    root = ET.Element('data')

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, xml_declaration = True)
def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    deserialized_dict = {}
    for child in root:
        deserialized_dict[child.tag] = child.text
    return deserialized_dict
