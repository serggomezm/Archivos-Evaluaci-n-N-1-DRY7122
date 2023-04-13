import xml.etree.ElementTree as ET

nom = input("Ingrese su nombre: ")
ape = input("Ingrese su apellido: ")

data = ET.Element("datos")

nombre = ET.SubElement(data, "nombre")
nombre.text = nom

apellido = ET.SubElement(data, "apellido")
apellido.text = ape

xml_data = ET.tostring(data)

# Mostrar en pantalla
print(xml_data.decode())
