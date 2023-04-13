import yaml
nom= input("Ingrese su nombre: ")
ape=input("Ingrese su apellido: ")


data ={
    "nombre":nom,
    "apellido":ape
}

data_yaml = yaml.dump(data)

print(data_yaml)
