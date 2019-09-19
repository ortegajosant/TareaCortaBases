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
    ciudades = ["Melbourne", "París", "Estocolmo", "Boston", "Los Angeles", "Londres",
                "Nueva York", "Houston", "Buenos Aires", "Alajuela",
                "Amsterdam", "Berlín", "Madrid", "Barcelona", "Toronto", "Bruselas",
                "Atenas", "Roma", "Mónaco", "Lisboa", "Moscú", "Zagreb",
                "Caracas", "Quito", "Bogotá", "Santiago", "Brasilia", "Berna",
                "Kingston", "La Habana", "Seúl", "Tokio", "Pekín", "Doha"]
    for aeropuerto in aeropuertos:
        telefono = str(random.randint(10000000, 99999999))
        try:
            vdb.execute("INSERT INTO Aeropuerto ('Nombre', 'Telefono', 'Localizacion', 'Codigo') VALUES (?,?,?,?)",
                        ("Aeropuerto " + aeropuerto, telefono, ciudades[0],
                         hashlib.md5(aeropuerto.encode("utf-8")).hexdigest()))
            ciudades.remove(ciudades[0])
        except:
            print(Exception)
            return
    viajes_db.commit()


def insertar_horario_servicio():
    vdb.execute("SELECT AEP.IdAeropuerto FROM Aeropuerto AEP;")
    aeropuertos = vdb.fetchall()
    for aeropuerto in aeropuertos:
        cantidad = random.randint(3, 5)
        while cantidad > 0:
            fecha = datetime.datetime.today() - datetime.timedelta(days=random.randrange(5000, 15000))
            vdb.execute("INSERT INTO HorarioServicio ('IdAeropuerto', 'IdHorario', 'Fecha') VALUES (?, ?, ?)",
                        (aeropuerto[0], random.choice([8, 9]), fecha.strftime("%Y-%m-%d")))
            cantidad -= 1
    viajes_db.commit()


def insertar_fabricantes():
    fabricantes = ["Boeing", "Airbus", "Embraer", "Bombardier", "Tupoloev",
                   "Ahrens", "Agusta", "Avro", "British Aircraft Corporation",
                   "Beechcraft", "Convair", "Dassault", "Ilyushin"]
    for i in range(len(fabricantes)):
        # try:
        vdb.execute("INSERT INTO Fabricante ('Nombre') VALUES (?);",
                    (fabricantes[i],))
    # except:
    #     print(Exception)
    #     return
    viajes_db.commit()


def insertar_aviones(cantidad):
    vdb.execute("SELECT * FROM Aerolinea;")
    aerolineas = vdb.fetchall()
    vdb.execute("SELECT * FROM Fabricante;")
    fabricantes = vdb.fetchall()
    vdb.execute("SELECT AEP.Localizacion FROM Aeropuerto AEP GROUP BY AEP.Localizacion;")
    localizaciones = vdb.fetchall()

    modelos = ["A320 neo", "A340", "A350", "A380", "717", "747-8", " 787 Dreamliner",
               "CRJ 700", "CRJ 900", "CRJ 1000", "Cseries", "Il-103", "Il-114", "Il-86",
               "Mercure", "Falcon 7X", "Falcon 5X", "CV-990/990A ", "Challenger 605", "Challenger 850 ",
               "Global Express", "720", "777", "757", "737", "RJ Series", "A330", "A310",
               "A319", "A380", "A300", "AR 404", "Corvette", "Aerospace Concorde", "Mohawk 298 "]

    estados = ["Activo", "Inactivo", "En reparacion", "En vuelo"]

    while cantidad > 0:

        estado = random.choice(estados)
        localizacion = random.choice(localizaciones)[0]
        if (estado == "En vuelo"):
            localizacion = calcular_coordenada()
        vdb.execute("INSERT INTO Avion ('IdAerolinea', 'IdFabricante','Codigo'," +
                    "'Modelo','CapacidadTripulacion','CapacidadItinerario','Estado','Posicion') " +
                    "VALUES (?,?,?,?,?,?,?,?)",
                    (random.choice(aerolineas)[0], random.choice(fabricantes)[0],
                     hashlib.md5(
                         (str(cantidad) + random.choice(modelos) + random.choice(fabricantes)[1]).encode(
                             "utf-8")).hexdigest(),
                     random.choice(modelos), random.randint(30, 100), random.randint(1, 3), estado,
                     localizacion))

        cantidad -= 1
    viajes_db.commit()


def insertar_aeropuerto_aerolinea():
    vdb.execute("SELECT AEP.IdAeropuerto FROM Aeropuerto AEP;")
    aeropuertos = vdb.fetchall()
    vdb.execute("SELECT AE.IdAerolinea FROM Aerolinea AE;")
    aerolineas = vdb.fetchall()
    for aeropuerto in aeropuertos:
        cantidad = random.randint(1, len(aerolineas))
        aero_temp = aerolineas.copy()
        while cantidad > 0:
            random.shuffle(aero_temp)
            vdb.execute("INSERT INTO AeropuertoAerolinea ('IdAeropuerto', 'IdAerolinea') VALUES (?, ?)",
                        (aeropuerto[0], aero_temp[0][0]))
            aero_temp.remove(aero_temp[0])
            cantidad -= 1
    viajes_db.commit()


def insertar_vuelo(cantidad_vuelos):
    viajes_db = sqlite3.connect("viajesDB.sqlite3")
    vdb = viajes_db.cursor()
    vdb.execute("SELECT A.IdAvion FROM Avion A;")
    aviones = vdb.fetchall()
    vdb.execute("SELECT AEP.Localizacion FROM Aeropuerto AEP GROUP BY AEP.Localizacion;")
    ciudades = vdb.fetchall()
    estados = ["Activo", "En proceso", "Finalizado"]
    cont = 1
    while cont <= cantidad_vuelos:
        estado = random.choice(estados)
        fecha_salida = 0
        fecha_llegada = 0
        if estado == "Activo":
            fecha_salida = datetime.datetime.today() + datetime.timedelta(days=random.randrange(0, 365))
            fecha_llegada = fecha_salida + datetime.timedelta(days=random.randrange(0, 4),
                                                              hours=random.randrange(0, 24),
                                                              minutes=random.randrange(0, 60),
                                                              seconds=random.randrange(0, 60))
        elif estado == "En proceso":
            dia_variable = random.randrange(0, 2)
            fecha_salida = datetime.datetime.today() - datetime.timedelta(days=dia_variable,
                                                                          hours=random.randrange(0, 24),
                                                                          minutes=random.randrange(0, 60),
                                                                          seconds=random.randrange(0, 60))
            fecha_llegada = fecha_salida + datetime.timedelta(days=dia_variable + random.randrange(0, 2),
                                                              hours=random.randrange(0, 24),
                                                              minutes=random.randrange(0, 60),
                                                              seconds=random.randrange(0, 60))
        else:
            fecha_salida = datetime.datetime.today() - datetime.timedelta(days=random.randrange(4, 13000))
            fecha_llegada = fecha_salida + datetime.timedelta(days=random.randrange(0, 4),
                                                              hours=random.randrange(0, 24),
                                                              minutes=random.randrange(0, 60),
                                                              seconds=random.randrange(0, 60))
        precio = random.randint(100000, 1200000)
        random.shuffle(ciudades)
        vdb.execute("INSERT INTO Vuelo ('IdAvion', 'NumeroVuelo', 'Origen', 'Destino',"
                    " 'FechaHoraSalida', 'FechaHoraLlegada', 'Estado', 'Precio', 'PesoMaximo') "
                    "VALUES (?, ?, ? , ?, ?, ?, ?, ?, ?)",
                    (random.choice(aviones)[0], cont, ciudades[0][0], ciudades[1][0],
                     fecha_salida, fecha_llegada, estado, precio, random.randint(1, 15)))
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
    vdb.execute("SELECT C.IdClase, C.IdAvion FROM Clase C WHERE C.Tipo = 'Común';")
    comunes = vdb.fetchall()
    vdb.execute("SELECT C.IdClase, C.IdAvion FROM Clase C WHERE C.Tipo = 'Preferencial';")
    preferenciales = vdb.fetchall()

    for asiento in comunes:
        vdb.execute("SELECT A.CapacidadTripulacion FROM Avion A WHERE A.IdAvion = " + str(asiento[1]) + ";")
        avion = vdb.fetchall()
        cont = int(avion[0][0] * 0.7)
        while cont > 0:
            vdb.execute("INSERT INTO Asiento ('IdClase', 'NumeroAsiento') VALUES (?, ?);",
                        (asiento[0], cont))
            cont -= 1
    for asiento in preferenciales:
        vdb.execute("SELECT A.CapacidadTripulacion FROM Avion A WHERE A.IdAvion = " + str(asiento[1]) + ";")
        avion = vdb.fetchall()
        cont = int(avion[0][0] * 0.3)
        while cont > 0:
            vdb.execute("INSERT INTO Asiento ('IdClase', 'NumeroAsiento') VALUES (?, ?);",
                        (asiento[0], cont))
            cont -= 1
    viajes_db.commit()


def insertar_bodega():
    vdb.execute("SELECT AEP.IdAeropuerto, AEP.Nombre FROM Aeropuerto AEP;")
    aeropuertos = vdb.fetchall()
    for aeropuerto in aeropuertos:
        vdb.execute("INSERT INTO Bodega ('IdAeropuerto', 'Nombre') VALUES (?, ?);",
                    (aeropuerto[0], "Bodega " + aeropuerto[1]))

    viajes_db.commit()


def insertar_bodega_avion():
    vdb.execute("SELECT B.IdBodega, B.IdAeropuerto FROM Bodega B;")
    bodegas = vdb.fetchall()

    for bodega in bodegas:
        vdb.execute(
            "SELECT A.IdAvion, A.Estado, A.Posicion FROM Avion A WHERE A.IdAerolinea IN (SELECT AAE.IdAerolinea "
            "FROM AeropuertoAerolinea AAE WHERE AAE.IdAeropuerto =" + str(bodega[1]) + ");")
        aviones = vdb.fetchall()
        vdb.execute("SELECT AEP.Localizacion FROM Aeropuerto AEP WHERE  AEP.IdAeropuerto = " + str(bodega[1]) + ";")
        localizacion = vdb.fetchall()
        for avion in aviones:
            if avion[1] == "Inactivo" and avion[2] == localizacion[0][0]:
                fecha_entrada = datetime.datetime.today() - datetime.timedelta(days=random.randrange(0, 30))
                vdb.execute(
                    "INSERT INTO BodegaAvion ('IdBodega', 'IdAvion', 'FechaHoraSalida', 'FechaHoraLlegada') VALUES (?, ?, ?, ?);",
                    (bodega[0], avion[0], 'NULL', fecha_entrada))
            else:
                fecha_entrada = datetime.datetime.today() - datetime.timedelta(days=random.randrange(35, 10000))
                fecha_salida = fecha_entrada + datetime.timedelta(days=random.randrange(5, 30))
                vdb.execute(
                    "INSERT INTO BodegaAvion ('IdBodega', 'IdAvion', 'FechaHoraSalida', 'FechaHoraLlegada') VALUES (?, ?, ?, ?);",
                    (bodega[0], avion[0], fecha_salida, fecha_entrada))
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
    vdb.execute("SELECT AEP.IdAeropuerto, AEP.Nombre FROM Aeropuerto AEP;")
    aeropuertos = vdb.fetchall()

    for aeropuerto in aeropuertos:
        vdb.execute("INSERT INTO Taller ('IdAeropuerto', 'Nombre') VALUES (?, ?)",
                    (aeropuerto[0], "Taller " + aeropuerto[1]))
    viajes_db.commit()


def insertar_taller_avion():
    vdb.execute("SELECT * FROM Taller;")
    talleres = vdb.fetchall()

    for taller in talleres:
        vdb.execute(
            "SELECT A.IdAvion, A.Estado, A.Posicion FROM Avion A WHERE A.IdAerolinea IN (SELECT AAE.IdAerolinea "
            "FROM AeropuertoAerolinea AAE WHERE AAE.IdAeropuerto =" + str(taller[1]) + ");")
        aviones = vdb.fetchall()
        vdb.execute("SELECT AEP.Localizacion FROM Aeropuerto AEP WHERE  AEP.IdAeropuerto = " + str(taller[1]) + ";")
        localizacion = vdb.fetchall()
        for avion in aviones:
            if avion[1] == "En reparacion" and localizacion[0][0] == avion[2]:
                fecha_entrada = datetime.datetime.today() - datetime.timedelta(days=random.randrange(0, 30))
                vdb.execute(
                    "INSERT INTO TallerAvion ('IdTaller', 'IdAvion', 'FechaHoraSalida', 'FechaHoraLlegada') VALUES (?, ?, ?, ?);",
                    (taller[0], avion[0], 'NULL', fecha_entrada))
            else:
                fecha_entrada = datetime.datetime.today() - datetime.timedelta(days=random.randrange(35, 10000))
                fecha_salida = fecha_entrada + datetime.timedelta(days=random.randrange(5, 30))
                vdb.execute(
                    "INSERT INTO TallerAvion ('IdTaller', 'IdAvion', 'FechaHoraSalida', 'FechaHoraLlegada') VALUES (?, ?, ?, ?);",
                    (taller[0], avion[0], fecha_salida, fecha_entrada))
    viajes_db.commit()


def insertar_factura():
    vdb.execute("SELECT TA.IdTallerAvion FROM TallerAvion TA WHERE FechaHoraSalida IS NOT NULL;")
    reparaciones = vdb.fetchall()

    for reparacion in reparaciones:
        vdb.execute("INSERT INTO Factura ('IdTallerAvion', 'Costo') VALUES (?, ?);",
                    (reparacion[0], random.randint(3000000, 10000000)))
    viajes_db.commit()


def insertar_danho():
    vdb.execute("SELECT F.IdFactura FROM Factura F;")
    facturas = vdb.fetchall()

    danhos = ["Impacto por rayo", "Impacto de pájaro", "Granizadas",
              "Fuga de líquido", "Frenos inestables", "Ruidos en el motor",
              "Generación de energía", "Problemas con ruedas"]
    for factura in facturas:
        vdb.execute("INSERT INTO Daño ('IdFactura', 'Descripcion') VALUES (?, ?);",
                    (factura[0], random.choice(danhos)))
    viajes_db.commit()


def insertar_repuesto():
    vdb.execute("SELECT F.IdFactura FROM Factura F;")
    facturas = vdb.fetchall()

    repuestos = ["Motor", "Batería", "Llanta", "Parabrisas", "Giroscopo", "Frenos",
                 "Asientos", "Ventanas", "Puerta", "Aceites", "Alternadores", "Luces de navegación",
                 "Hélice", "Tanque", "Retenedores", "Radio Comunicador", "Empaques"]
    for factura in facturas:
        vdb.execute("INSERT INTO Repuesto ('IdFactura', 'Descripcion') VALUES (?, ?);",
                    (factura[0], random.choice(repuestos)))
    viajes_db.commit()
