class Agenda:
    def __init__(self):
        self.contactos = []
    
    def get_contactos(self):
        return self.contactos
    
    def agregar_contacto(self):
        nombre = input("Ingrese el nombre")
        telefono = input("Ingrese el teléfono")
        email = input("Ingrese el email")
        nuevo_contacto = Contacto(nombre, telefono, email)
        self.get_contactos().append(nuevo_contacto)
        print("Contacto creado con éxito")
        
    def listar_contactos(self):
        for (idx, contacto) in enumerate(self.get_contactos()):
            print(f"{idx + 1}. {contacto.get_nombre()}")
            
    def buscar_contacto(self):
        contacto_buscado = input("Ingrese el nombre del contacto: ")
        contactos_encontrados = list(filter(lambda contacto: contacto.get_nombre() == contacto_buscado , self.get_contactos()))
        if (len(contactos_encontrados) >= 1):
            return contactos_encontrados
        else:
            return None
        
    def editar_contacto(self):
        contacto = self.buscar_contacto()
        if (contacto):
            nuevo_telefono = input("Ingrese el nuevo teléfono")
            nuevo_email = input("Ingrese el nuevo email")
            contacto[0].set_telefono(nuevo_telefono)
            contacto[0].set_email(nuevo_email)
            print("Contacto editado con éxito")
        

    def cerrar_agenda(self):
        print("Cerrando agenda...")
        exit()
        
    def mostrar_menu(self):
        
        while (True):
            print("1-Añadir contacto\n2-Listar contactos\n3-Buscar contacto\n4-Editar contacto\n5-Cerrar agenda")
            opc = int(input())
            match (opc):
                case 1:
                    self.agregar_contacto()
                case 2:
                    self.listar_contactos()
                case 3:
                    contactos = self.buscar_contacto()
                    if (contactos):
                        for contacto in contactos:
                            print(str(contacto))
                case 4:
                    self.editar_contacto()
                case 5:
                    self.cerrar_agenda()
                case _:
                    print("Ingrese una opción correcta")
        
        
class Contacto:
    def __init__(self, nombre, telefono, email):
        self.set_nombre(nombre)
        self.set_telefono(telefono)
        self.set_email(email)

    def get_nombre(self):
        return self.nombre
    def get_telefono(self):
        return self.telefono
    def get_email(self):
        return self.email
    def set_nombre(self, nombre):
        self.nombre = nombre
    def set_telefono(self, telefono):
        self.telefono = telefono
    def set_email(self, email):
        self.email = email
    def __str__(self):
        return f"Nombre: {self.get_nombre()}\nTeléfono: {self.get_telefono()}\nEmail: {self.get_email()}"
        
        
agenda = Agenda();
agenda.mostrar_menu()