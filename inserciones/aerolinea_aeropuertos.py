import sqlite3, random, hashlib, datetime

viajes_db = sqlite3.connect("viajesDB.sqlite3")
vdb = viajes_db.cursor()


def insertar_aerolineas():
    lista_aerlineas = ["Avianca", "Azul Airlines", "LATAM", "Sky Airline",
                       "Easyfly", "Singapur Airlines", "Qatar Airways",
                       "Emirates", "ANA AII Nippon Airways", "The Airways"
                                                             "Lufthansa", "Cathay Pasific Airway", "AirAsia X",
                       "Eurowings", "Jetstar Airways"]
    insercion = "INSERT INTO Aerolinea ('Codigo', 'Nombre')\n VALUES"
    values = ""
    for aerolinea in lista_aerlineas:
        values = values + "('" + hashlib.new("md5", aerolinea.encode("utf-8")).hexdigest()[0:9] \
                 + "', " + "'" + aerolinea
        if aerolinea == lista_aerlineas[-1]:
            values = values + "');"
            break
        values = values + "'),\n"
    insercion = insercion + values
    vdb.execute(insercion)
    viajes_db.commit()


def insertar_aeropuerto():
    aeropuertos = ["de Changi", "Internacional Hamad", "de Munich", "Internacional Chubu Centrair",
                   "de Heathrow", "de Zurich", "de Frankfurt", "Internacional de Hong Kong", "Internacional de Haneda",
                   "Internacional de Incheon", "Juan Santamaría", "Internacional El Dorado",
                   "Internacional Jorge Chávez",
                   "Internacional Mariscal Sucre", "Internacional José Joaquín de Olmedo", "Internacional Tocumen",
                   "Hartsfield-Jackson Atlanta", "Pékin Capital", "Dubái International", "Los Angeles",
                   "París Charles de Gaulle", "Estambul Atatürk", "de Barcelona", "de Gran Canaria", "de Washington",
                   "Tenerife Sur", "de Valencia", "de Ibiza", "Fiumicino", "Internacional Daniel Oduber",
                   "Internacional Tobias Bolaños", "Internacional de Kansai"]
    for aeropuerto in aeropuertos:
        telefono = str(random.randint(10000000, 99999999))
        localizacion = calcular_coordenada()
        try:
            vdb.execute("INSERT INTO Aeropuerto ('Nombre', 'Telefono', 'Localizacion', 'Codigo') VALUES (?,?,?,?)",
                        ("Aeropuerto " + aeropuerto, telefono, localizacion,
                         hashlib.md5(aeropuerto.encode("utf-8")).hexdigest()))
        except:
            print(Exception)
            return
    viajes_db.commit()


def insertar_horario_servicio():
    vdb.execute("SELECT AEP.IdAeropuerto FROM Aeropuerto;")
    aeropuertos = vdb.fetchall()
    for aeropuerto in aeropuertos:
        cantidad = random.randint(3, 5)
        while cantidad > 0:
            fecha = datetime.datetime.today() - datetime.timedelta(days=random.randrange(5000, 15000))
            vdb.execute("INSERT INTO HorarioServicio ('IdAeropuerto', 'IdHorario', 'Fecha') VALUES (?, ?, ?)",
                        (aeropuerto[0], random.choice([8, 9]), fecha.strftime("%Y-%m-%d")))
            cantidad -= 1
    viajes_db.commit()


def calcular_coordenada():
    latitud = random.randint(-90, 90)
    longitud = random.randint(-180, 180)
    if latitud > 0:
        latitud = str(latitud) + "° " + "N"
    else:
        latitud = str(latitud) + "° " + "S"
    if longitud > 0:
        longitud = str(longitud) + "° " + "E"
    else:
        longitud = str(longitud) + "° " + "O"

    return latitud + " " + longitud


def insertar_fabricantes():
    fabricantes = ["Boeing", "Airbus", "Embraer", "Bombardier", "Tupoloev",
                   "Ahrens", "Agusta", "Avro", "British Aircraft Corporation",
                   "Beechcraft", "Convair", "Dassault", "Ilyushin"]
    for fabricante in fabricantes:
        try:
            vdb.execute("INSERT INTO Fabricante ('Nombre') VALUES (?)",
                        (fabricante))
        except:
            print(Exception)
            return
    viajes_db.commit()


def insertar_aviones(cantidad):
    vdb.execute("SELECT * FROM Aerolinea;")
    aerolineas = vdb.fetchall()
    vdb.execute("SELECT * FROM Fabricante;")
    fabricantes = vdb.fetchall()

    modelos = ["A320 neo", "A340", "A350", "A380", "717", "747-8", " 787 Dreamliner",
               "CRJ 700", "CRJ 900", "CRJ 1000", "Cseries", "Il-103", "Il-114", "Il-86",
               "Mercure", "Falcon 7X", "Falcon 5X", "CV-990/990A ", "Challenger 605", "Challenger 850 ",
               "Global Express", "720", "777", "757", "737", "RJ Series", "A330", "A310",
               "A319", "A380", "A300", "AR 404", "Corvette", "Aerospace Concorde", "Mohawk 298 "]

    estados = ["Activo", "Inactivo", "En reparacion"]

    while cantidad > 0:
        try:
            vdb.execute("INSERT INTO Avion ('IdAerolinea', 'IdFabricante','Codigo'," +
                        "'Modelo','CapacidadTripulacion','CapacidadItinerario','Estado','Posicion') " +
                        "VALUES (?,?,?,?,?,?,?,?)",
                        (random.choice(aerolineas)[0], random.choice(fabricantes)[0],
                         hashlib.md5(
                             (str(cantidad) + random.choice(modelos) + random.choice(fabricantes)[1]).encode(
                                 "utf-8")).hexdigest(),
                         random.choice(modelos), random.randint(30, 100), random.randint(1, 3), random.choice(estados),
                         calcular_coordenada()))
        except:
            print(Exception)
            return
        cantidad -= 1
    viajes_db.commit()


def insertar_aeropuerto_aerolinea(cantidad):
    vdb.execute("SELECT AEP.IdAeropuerto FROM Aeropuerto AEP;")
    aeropuertos = vdb.fetchall()
    vdb.execute("SELECT AE.IdAerolinea FROM Aerolinea AE;")
    aerolineas = vdb.fetchall()

    while cantidad > 0:
        vdb.execute("INSERT INTO AeropuertoAerolinea ('IdAeropuerto', 'IdAerolinea') VALUES (?, ?)",
                    (random.choice(aeropuertos)[0], random.choice(aerolineas)[0]))
        random.shuffle(aeropuertos)
        random.shuffle(aerolineas)
        cantidad -= 1
    viajes_db.commit()


def insertar_vuelo(cantidad_vuelos):
    viajes_db = sqlite3.connect("viajesDB.sqlite3")
    vdb = viajes_db.cursor()
    vdb.execute("SELECT A.IdAvion FROM Avion A;")
    aviones = vdb.fetchall()

    ciudades = ["Melbourne", "París", "Estocolmo", "Boston", "Los Angeles", "Londres",
                "Nueva York", "Houston", "Buenos Aires", "Alajuela",
                "Amsterdam", "Berlín", "Madrid", "Barcelona", "Toronto", "Bruselas",
                "Atenas", "Roma", "Mónaco", "Lisboa", "Moscú", "Zagreb",
                "Caracas", "Quito", "Bogotá", "Santiago", "Brasilia", "Berna",
                "Kingston", "La Habana", "Seúl", "Tokio", "Pekín", "Doha"]
    estados = ["Activo", "En proceso", "Finalizado"]
    cont = 1
    while cont <= cantidad_vuelos:
        fecha_salida = datetime.datetime.today() - datetime.timedelta(days=random.randrange(0, 13000))
        fecha_llegada = fecha_salida + datetime.timedelta(days=random.randrange(1, 4))
        precio = random.randint(100000, 1200000)
        vdb.execute("INSERT INTO Vuelos ('IdAvion', 'NumeroVuelo', 'Origen', 'Destino',"
                    " 'FechaHoraSalida', 'FechaHoraLlegada', 'Estado', 'Precio') "
                    "VALUES (?, ?, ? , ?, ?, ?, ?, ?)",
                    (random.choice(aviones)[0], cont, random.choice(ciudades), random.choice(ciudades),
                     fecha_salida, fecha_llegada, random.choice(estados), precio))
        cont += 1
    viajes_db.commit()


def insertar_clase():
    vdb.execute("SELECT A.IdAvion FROM Avion A;")
    aviones = vdb.fetchall()

    for avion in aviones:
        precio_normales = random.randint(30000, 45000)
        precio_vip = random.randint(75000, 150000)
        vdb.execute("INSERT INTO Clase ('IdAvion', 'Tipo', 'Precio') VALUES (?, ?, ?)",
                    (avion[0], "Común", precio_normales))
        vdb.execute("INSERT INTO Clase ('IdAvion', 'Tipo', 'Precio') VALUES (?, ?, ?)",
                    (avion[0], "Preferencial", precio_vip))
    viajes_db.commit()


def insertar_asiento():
    vdb.execute("SELECT C.IdClase FROM Clase C WHERE C.Tipo = 'Común';")
    comunes = vdb.fetchall()
    vdb.execute("SELECT C.IdClase FROM Clase C WHERE C.Tipo = 'Preferencial';")
    preferenciales = vdb.fetchall()

    for asiento in comunes:
        cont = random.randint(50, 80)
        while cont > 0:
            vdb.execute("INSERT INTO Asiento ('IdClase', 'NumeroAsiento') VALUES (?, ?)",
                        (asiento, cont))
            cont -= 1
    for asiento in preferenciales:
        cont = random.randint(25, 35)
        while cont > 0:
            vdb.execute("INSERT INTO Asiento ('IdClase', 'NumeroAsiento') VALUES (?, ?)",
                        (asiento, cont))
            cont -= 1
    viajes_db.commit()


def insertar_tiquete():
    vdb.execute("SELECT V.IdVuelo, V.IdAvion FROM Vuelo V;")
    vuelos = vdb.fetchall()
    vdb.execute("SELECT EQ.IdEquipaje, EQ.IdUsuario FROM Equipaje EQ;")
    equipajes = vdb.fetchall()
    vdb.execute("SELECT PS.IdPasaporte, PS.IdUsuario FROM Pasaporte PS;")
    pasaportes = vdb.fetchall()
    for vuelo in vuelos:
        vdb.execute("SELECT AN.IdAsiento FROM Asiento INNER JOIN "
                    "Clase C ON C.IdAvion = " + vuelo[1] +
                    " WHERE C.IdClase = AN.IdClase;")
        asientos = vdb.fetchall()
        cantidad_tiquetes = random.randint(0, len(asientos))
        cont = 0
        while cont < cantidad_tiquetes:
            pasaporte = random.choice(pasaportes)
            equipaje = ()
            for eq in equipajes:
                if eq[1] == pasaporte[1]:
                    equipaje = eq
                    break
            vdb.execute("INSERT INTO Tiquete ('IdVuelo', 'IdAsiento', "
                        "'IdEquipaje', 'IdPasaporte') VALUES (?, ?, ?, ?)",
                        (vuelo[0], asientos[0][0], equipaje[0], pasaporte[0]))
            asientos.remove(0)
            random.shuffle(asientos)
            cont += 1
    viajes_db.commit()


def insertar_bodega():
    vdb.execute("SELECT AEP.IdAeropuerto, AEP.Nombre FROM Aeropuerto AEP;")
    aeropuertos = vdb.fetchall()
    for aeropuerto in aeropuertos:
        vdb.execute("INSERT INTO Bodega ('IdAeropuerto', 'Nombre')", (aeropuerto[0], "Bodega " + aeropuerto[1]))

    viajes_db.commit()


def insertar_bodega_avio():
    vdb.execute("SELECT B.IdBodega, B.IdAeropuerto FROM Bodega B;")
    bodegas = vdb.fetchall()

    for bodega in bodegas:
        vdb.execute("SELECT A.IdAvion FROM Avion A INNER JOIN AeropuertoAerolinea AAE ON AAE.IdAeropuerto = " + str(
            bodega[1]) + " WHERE A.Estado = 'Inactivo';")
        aviones = vdb.fetchall()

        for avion in aviones:
            fecha_entrada = datetime.datetime.today() - datetime.timedelta(days=random.randrange(0, 60))
            fecha_salida = fecha_entrada + datetime.timedelta(days=random.randrange(0, 30))

            if fecha_salida >= fecha_entrada:
                vdb.execute(
                    "INSERT INTO BodegaAvion ('IdAvion', 'FechaHoraLlegada', 'FechaHoraSalida') VALUES (?, ?, ?);",
                    (avion[0], fecha_entrada, 'NULL'))
            else:
                vdb.execute(
                    "INSERT INTO BodegaAvion ('IdAvion', 'FechaHoraLlegada', 'FechaHoraSalida') VALUES (?, ?, ?);",
                    (avion[0], fecha_entrada, fecha_salida))
    viajes_db.commit()


def insertar_controlador_vuelo():
    vdb.execute("SELECT V.IdVuelo FROM Vuelo V;")
    vuelos = vdb.fetchall()
    cont = 1
    for vuelo in vuelos:
        vdb.execute("INSERT INTO ControladorVuelo ('IdVuelo', 'CodigoComunicacion') VALUES (?,?);",
                    (vuelo[0], str(193) + "." + str(random.randint(100, 999)) + "." + str(cont)))
        cont += 1
    viajes_db.commit()


def insertar_taller():
    vdb.execute("SELECT AEP.IdAerpuerto, AEP.Nombre FROM Aeropuerto AEP;")
    aeropuertos = vdb.fetchall()

    for aeropuerto in aeropuertos:
        vdb.execute("INSERT INTO Taller ('IdAeropuerto', 'Nombre') VALUES (?, ?)",
                    (aeropuerto[0], "Taller " + aeropuerto[1]))
    viajes_db.commit()


def insertar_taller_avion():
    vdb.execute("SELECT * FROM Taller;")
    talleres = vdb.fetchall()

    for taller in talleres:
        vdb.execute("SELECT A.IdAvion FROM Avion A INNER JOIN AeropuertoAerolinea AAE ON AAE.IdAeropuerto = " + str(
            taller[1]) + " WHERE A.Estado = 'En reparación';")
        aviones = vdb.fetchall()
        for avion in aviones:
            vdb.execute("INSERT INTO TallerAvion ('IdTaller', 'IdAvion') VALUES (?, ?);", (taller[0], avion[0]))
    viajes_db.commit()


def insertar_factura():
    vdb.execute("SELECT TA.IdTallerAvion FROM TallerAvion TA;")
    reparaciones = vdb.fetchall()

    for reparacion in reparaciones:
        fecha_entrada = datetime.datetime.today() - datetime.timedelta(days=random.randrange(0, 60))
        fecha_salida = fecha_entrada + datetime.timedelta(days=random.randrange(0, 30))

        if fecha_salida >= datetime.datetime.today():
            vdb.execute(
                "INSERT INTO Factura ('IdTallerAvion', 'Costo', 'FechaHoraSalida', 'FechaHoraLlegada') VALUES (?, ?, ?, ?);",
                (reparacion[0], random.randint(1000000, 3000000), 'NULL', fecha_entrada))
        else:
            vdb.execute(
                "INSERT INTO Factura ('IdTallerAvion', 'Costo', 'FechaHoraSalida', 'FechaHoraLlegada') VALUES (?, ?, ?, ?);",
                (reparacion[0], random.randint(1000000, 3000000), fecha_salida, fecha_entrada))
    viajes_db.commit()


def insertar_daño():
    vdb.execute("SELECT F.IdFactura FROM Factura;")
    facturas = vdb.fetchall()

    daños = ["Impacto por rayo", "Impacto de pájaro", "Granizadas",
             "Fuga de líquido", "Frenos inestables", "Ruidos en el motor",
             "Generación de energía"]
    for factura in facturas:
        vdb.execute("INSERT INTO Daño ('IdFactura', 'Descripcion') VALUES (?, ?);",
                    (factura[0], random.choice(daños)))
    viajes_db.commit()


def insertar_repuesto():
    vdb.execute("SELECT F.IdFactura FROM Factura;")
    facturas = vdb.fetchall()

    repuestos = ["Motor", "Batería", "Llanta", "Parabrisas", "Giroscopo", "Frenos",
                 "Asientos", "Ventanas", "Puerta", "Aceites", "Alternadores", "Luces de navegación",
                 "Hélice", "Tanque", "Retenedores", "Radio Comunicador", "Empaques"]
    for factura in facturas:
        vdb.execute("INSERT INTO Repuesto ('IdFactura', 'Descripcion') VALUES (?, ?);",
                    (factura[0], random.choice(repuestos)))
    viajes_db.commit()
