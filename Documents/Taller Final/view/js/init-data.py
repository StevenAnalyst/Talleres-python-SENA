from datetime import date, timedelta
import json

class personalizaError():
    pass

def initializeData(): 
    try: 
        with open('clientes.json', 'w') as c, open('glampings.json', 'w') as g, open('reservas.json', 'w') as r:
            print("cargando archivos")
    except FileNotFoundError:
        CLIENTES = [
            {
               id: 1,
               "nombre": 'Juan Pérez',
               "email": 'juan@ejemplo.com',
               "telefono": '3001234567',
               "documento": '12345678'
            },
            {
               id: 2,
               "nombre": 'María López',
               "email": 'maria@ejemplo.com',
               "telefono": '3109876543',
               "documento": '87654321'
            },
            {
               id: 3,
               "nombre": 'Carlos Rodríguez',
               "email": 'carlos@ejemplo.com',
               "telefono": '3201112233',
               "documento": '11223344'
            }
        ]
        clientes_json = json.dumps([c.toJSON() for c in CLIENTES])
        GLAMPINGS = [
            {
               id: 1,
               "nombre": 'Cabaña del Bosque',
               "capacidad": 4,
               "precioPorNoche": 200000,
               "caracteristicas": ['WiFi', 'Chimenea', 'Vista al bosque', 'Cocina equipada'],
               "disponible": True
            },
            {
               id: 2,
               "nombre": 'Domo Estrella',
               "capacidad": 2,
               "precioPorNoche": 150000,
               "caracteristicas": ['Techo transparente', 'Jacuzzi', 'Desayuno incluido'],
               "disponible": True
            },
            {
                id: 3,
               "nombre": 'Tienda Safari',
               "capacidad": 6,
               "precioPorNoche": 300000,
               "caracteristicas": ['Terraza', 'Baño privado', 'Cerca del lago', 'Hamacas'],
               "disponible": True
            }
        ]
        glampings_json = json.dumps([g.toJSON() for g in GLAMPINGS])

        HOY = date.today()
        FECHAINICIO = HOY.isoformat()
        MAÑANA = HOY + timedelta(days=1)
        FECHAFIN = MAÑANA.isoformat()

        RESERVAS = [
            {
                "id": 1,
                "clienteId": 1, 
                "glampingId": 2,
                "fechaInicio": FECHAINICIO,
                "fechaFin": FECHAFIN,
                "totalPagado": 150000,
                "estado": 'confirmada'
            }
        ]
        reservas_json = json.dumps([r.toJSON() for r in RESERVAS])
        c.write(clientes_json)
        g.write(glampings_json)
        r.write(reservas_json)
    else:
        print("ya existen archivos, no se inicializara la prueba") 
        
# document.addEventListener('DOMContentLoaded', initializeData); 