import json 
nom= input("Ingrese su nombre: ")
ape=input("Ingrese su apellido: ")


data ={
    "nombre":nom,
    "apellido":ape

}
data_json = json.dumps(data)

print(data_json)