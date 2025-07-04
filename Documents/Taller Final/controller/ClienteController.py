
import json
import re
from Cliente import Cliente
class ClienteError():
    pass

class ClienteController():

    def __init__(self):
        pass

    def obtenerTodos():
        return Cliente.obtenerClientes()
    
    def buscarPorId(id):
        return Cliente.obtenerClientePorId(id)

    def buscarPorDocumento(documento):
            CLIENTES = ClienteController.obtenerTodos()
            return next((cliente for cliente in CLIENTES if cliente.getDocumento() == documento), False)
                
    def crear(datosCliente) : 

        try:
            CLIENTEEXISTENTE = ClienteController.buscarPorDocumento(datosCliente.documento)
            if not CLIENTEEXISTENTE: 
                raise ClienteError("ya existe un cliente con con ese documento")
        except ClienteError as c:
            print(f"error detectado. ${c}")
        else: 
            CLIENTE = Cliente(datosCliente.nombre,datosCliente.email,datosCliente.telefono,datosCliente.documento)
            CLIENTE.guardar()
            return CLIENTE
        
    def actualizar(id,datosCliente):
        CLIENTE = ClienteController.buscarPorId(id)
        if not CLIENTE:
            return False
        if datosCliente.documento and datosCliente.documento != CLIENTE.getDocumento():
            try:
                CLIENTEEXISTENTE = ClienteController.buscarPorDocumento(datosCliente.documento)
                if CLIENTEEXISTENTE and CLIENTEEXISTENTE.getId() != CLIENTE.getId():
                    raise ClienteError("ya existe un cliente con con ese documento")
            except ClienteError as c:
                print(f"error detectado. ${c}")
            else: 
                if (datosCliente.nombre): CLIENTE.setNombre(datosCliente.nombre)
                if (datosCliente.email): CLIENTE.setEmail(datosCliente.email)
                if (datosCliente.telefono): CLIENTE.setTelefono(datosCliente.telefono)
                if (datosCliente.documento): CLIENTE.setDocumento(datosCliente.documento)
    
                CLIENTE.guardar()
                return CLIENTE
    def eliminar(id): 
        CLIENTE = ClienteController.buscarPorId(id)
        if not CLIENTE:
            return False

        RESERVACONTROLLER = ReservaCotroller()
        RESERVACLIENTE = RESERVACONTROLLER.obtenerReservasCliente(id)
        try: 
            if len(RESERVACLIENTE) > 0:
                raise ClienteError("no se puede eliminar el cliente ya que tiene una reserva")
        except ClienteError as c:
            print(c)
        else: 
            CLIENTES = ClienteController.obtenerTodos()
            CLIENTES.remove(ClienteController.buscarPorId(id))
            clientes_json = json.dumps([c.toJSON() for c in CLIENTES])
            try: 
                with open('clientes.json', 'w') as c:
                    print("cargando archivos")
            except FileNotFoundError:
                return  print("Error: El archivo no existe.")
            else:
                c.write(clientes_json)
                return True
            

    def validar(datosCliente):
        ERRORES = {}

        if (not datosCliente.nombre) or datosCliente.nombre.strip() == '':
            ERRORES["nombre"] = 'El nombre es obligatorio'
        
        if (not datosCliente.email) or datosCliente.email.strip() == '': 
            ERRORES['email'] = 'El email es obligatorio'
        elif not ClienteController.validarFormatoEmail(datosCliente.email) :
            ERRORES['email'] = 'El formato del email no es válido'

        if (not datosCliente.telefono) or datosCliente.telefono.strip() == '':
            ERRORES['telefono'] = 'El teléfono es obligatorio'


        if (not datosCliente.documento) or datosCliente.documento.strip() == '':
            ERRORES['documento'] = 'El documento es obligatorio'
        
        return ERRORES

    def validarFormatoEmail(email):
        REGEX = '/^[^\s@]+@[^\s@]+\.[^\s@]+$/'
        return re.match(REGEX,email) is not None
