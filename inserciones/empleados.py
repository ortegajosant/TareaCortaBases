import sqlite3, random, hashlib, datetime

viajes_db = sqlite3.connect("viajesDB.sqlite3")
vdb = viajes_db.cursor()


def insertar_usuario(cantidad):
    nombres_varon = ["Mario", "Manuel", "Miguel", "Oscar", "Nicolás", "Orlando", "Pablo",
                     "Alonso", "Armando", "Álvaro", "Alfredo", "Antonio", "Augusto",
                     "Aníbal", "Alejandro", "Boris", "Braulio", "Baltasar", "Basilio",
                     "Cristóbal", "Carlos", "Cristopher", "Christian", "César", "Carlo",
                     "David", "Diego", "Domingo", "Danilo", "Dimitri", "Darío", "Daniel",
                     "Edgar", "Enrique", "Esteban", "Emmanuel", "Eloy", "Eduardo", "Ernesto",
                     "Fabián", "Félix", "Federico", "Gabriel", "Gonzalo", "Gilberto", "George",
                     "Gustavo", "Jose", "Harold", "Haníbal", "Hugo", "Isaac", "Iván", "Ignacio",
                     "Juan", "Joaquín", "Julio", "Jonathan", "Jaime", "Kevin", "Lucas", "Luis",
                     "Paco", "Damián", "Pedro", "Renzo", "Ricardo", "Rafael", "Sebastián", "Tobías"]
    nombres_dama = ["Sophia", "Isabel", "Emily", "Abigail", "Sofia", "Sara", "Elizabeth", "María",
                    "Elena", "Alicia", "Flora", "Amelia", "Chloe", "Paula", "Andrea", "Ada", "Michelle",
                    "Daniela", "Sarem", "Hellen", "Liliana", "Cristina", "Rachel", "Kristel", "Stefany",
                    "Stephanie", "Paulina", "Amanda", "Liseth", "Patricia", "Alba", "Marta", "Mónica",
                    "Marcela", "Karla", "Verónica", "Alejandra", "Luisa", "Ana", "Estér", "Fabiola",
                    "Monserrath", "Natalia", "Vanessa", "Evelyn", "Melissa", "Jennifer", "Melany",
                    "Josselyn", "Mia", "Kathia", "Katherine", "Kimberly", "Raquel", "Alisson", "Cindy",
                    "Teresa", "Tatiana", "Angélica", "Brenda", "Dayanna", "Gabriela", "Rebeca", "Milena"]
    apellidos = ["González", "Ortega", "Chacón", "Chaves", "Monge", "Araya", "Marín", "Cordero", "Espinoza",
                 "Castillo", "Alvarado", "Leiva", "Sibaja", "Jiménez", "Alpizar", "Herrera", "Villalobos",
                 "Largaespada", "Montdragon", "Torres", "Venegas", "Ugalde", "López", "Leal", "Bolaños",
                 "Blanco", "Toruño", "Briceño", "Gómez", "Cruz", "Corona", "Díaz", "Meneses", "Salvatiera",
                 "Chirino", "Solis", "Villalta", "Castro", "Estrada", "Madriz", "Aguilar", "Ruíz", "Montenegro",
                 "Arce", "Smith", "Campbell", "Brown", "Miller", "Artavia", "Barrantes", "Tencio",
                 "Calderón", "Moore", "Murillo", "Mora", "Mata", "Salazar", "Jones", "Chavarría", "Ramos", "Molina",
                 "Solano", "Piedra", "Martínez"]

    provincia = ["San José", "Alajuela", "Cartago", "Heredia", "Guanacaste", "Puntarenas", "Limón"]
    generos = ['F', 'M']
    cuentas = ["2001", "001", "932", "302"]
    while cantidad > 0:
        sexo = random.choice(generos)
        if sexo == 'F':
            if random.randint(1, 101) > 50:
                nombre = random.choice(nombres_dama) + " " + random.choice(nombres_dama)
            else:
                nombre = random.choice(nombres_dama)
        else:
            if random.randint(1, 101) > 50:
                nombre = random.choice(nombres_varon) + " " + random.choice(nombres_varon)
            else:
                nombre = random.choice(nombres_varon)
        apellido_pat = random.choice(apellidos)
        apellido_mat = random.choice(apellidos)
        fecha_nacimiento = datetime.datetime.today() - datetime.timedelta(days=random.randrange(3000, 20000))
        indice = random.randint(1, 7)
        direccion = provincia[indice - 1] + " Calle " + str(random.randint(1, 21)) \
                    + ", Avenida " + str(random.randint(1, 30))
        cedula = str(indice) + str(random.randint(10000000, 99999999))
        cuenta_bancaria = random.choice(cuentas) + str(random.randint(10000000, 99999999))
        codigo = hashlib.md5((cedula + nombre + apellido_pat + apellido_mat).encode("utf-8")).hexdigest()[0:9]
        vdb.execute("INSERT INTO Usuario ('Codigo', 'Nombre', 'ApellidoPat', 'ApellidoMat', 'Sexo',\
                'FechaNacimiento', 'Cedula','CuentaBancaria', 'Direccion')\n VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);",
                    (codigo, nombre, apellido_pat, apellido_mat, sexo, fecha_nacimiento.strftime('%Y-%m-%d'),
                     cedula, cuenta_bancaria, direccion))
        cantidad -= 1
    viajes_db.commit()


# insertar_usuario(4000)

def insertar_empleado():
    vdb.execute("SELECT * FROM Usuario U WHERE U.FechaNacimiento < '2001-01-01';")
    usuarios = vdb.fetchall()
    numero_empleados = random.randint(int(len(usuarios) * 0.2), int(len(usuarios) * 0.25))

    while numero_empleados > 0:
        random.shuffle(usuarios)
        vdb.execute("INSERT INTO Empleado ('IdUsuario', 'Codigo') VALUES (?, ?);",
                    (usuarios[0][0], hashlib.md5((usuarios[0][1] + usuarios[0][7]).encode('utf-8')).hexdigest()))
        usuarios.remove(usuarios[0])
        numero_empleados -= 1

    viajes_db.commit()


# insertar_empleado()

def insertar_pasaporte():
    vdb.execute("SELECT * FROM Usuario;")
    usuarios = vdb.fetchall()

    cantidad = int(len(usuarios) * 0.7)

    lugares_nacimiento = ["Golfito", "Pérez Zeledón", "San José", "Buenos Aires", "Turrialba",
                          "San Ramón", "Escazú", "San Carlos", "San Vito", "Coto Brus", "Sarapiquí",
                          "Nicoya", "San Pedro", "Cartago", "Roma", "Madrid", "Washington", "Sidney",
                          "Liberia", "Paraíso", "Juan Viñas", "Río Claro", "Pocosí", "Palmares",
                          "Naranjo", "Tres Ríos", "Río Cuarto", "Peñas Blancas", "Puerto Viejo",
                          "Santa Cruz", "Acosta", "Upala", "Ciudad Cortez", "Guácimo", "Toronto",
                          "Bajos del Toro", "Poás", "Fortuna", "Ciudad Quesada", "Florencia", "San Joaquín",
                          "Barva", "San Rafael", "Uruca", "Curridabat", "Tokyo", "Moscú", "Berlín", "Paris",
                          "Palermo", "Paris", "Nairobi", "Venecia", "Grecia", "Beijgin", "Estocolmo", "Londres",
                          "Amsterdam", "Munich", "Seúl", "Dortmund", "New York", "San Salvador", "Lima", "La Paz",
                          "Medellín", "Bogotá", "Atlanta", "Santiago"]
    nacionalidades = ["AD", "AE", "AR", "AT", "AU", "CA", "CL", "CR", "CZ", "DE", "US", "EC", "HR", "HN", "IT",
                      "JP", "FR", "RU", "BR", "SV", "ZA", "VE", "SE", "PL", "PE", "NZ", "MX", "NL", "KR"]
    tipos = ['T', 'P', 'N', 'E']
    while cantidad > 0:
        fecha_emision = datetime.datetime.today() - datetime.timedelta(days=random.randrange(200, 4000))
        lugare_nac = random.choice(lugares_nacimiento)
        usuario = usuarios[0]
        vdb.execute("INSERT INTO Pasaporte ('IdUsuario', 'Nacionalidad', 'LugarNacimiento',"
                    " 'FechaEmision', 'FechaExpiracion', 'LugarEmision', 'CodigoEstado',"
                    "'NumeroSecuencial', 'NumeroPasaporte', 'Tipo') VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
                    (usuario[0], random.choice(nacionalidades),
                     lugare_nac, fecha_emision.strftime('%Y-%m-%d'),
                     (fecha_emision + datetime.timedelta(2300)).strftime('%Y-%m-%d'),
                     random.choice(lugares_nacimiento), lugare_nac.upper()[0:2],
                     str(random.randint(10000000, 99999999)), str(cantidad),
                     random.choice(tipos)))
        cantidad -= 1
        usuarios.remove(usuario)
        random.shuffle(usuarios)
    viajes_db.commit()


# insertar_pasaporte()

def insertar_puesto():
    puestos_aerolinea = [("Piloto", 2000000), ("Azafata", 600000), ("Copiloto", 1200000)]
    puestos_aeropuerto = [("Despachador de vuelos", 400000), ("Técnicos Administrativos", 450000),
                          ("Agente de servicios aeroportuarios", 550000), ("Auxiliar de tierra", 650000)]
    cont = 0
    while cont < 7:
        if cont < 3:
            lugar = "Aerolínea"
            puesto = puestos_aerolinea[cont]
        else:
            lugar = "Aeropuerto"
            puesto = puestos_aeropuerto[0]
            puestos_aeropuerto.remove(puesto)

        vdb.execute("INSERT INTO Puesto ('NombrePuesto', 'Lugar', 'Sueldo') VALUES (?,?,?);",
                    (puesto[0], lugar, puesto[1]))
        cont += 1
    viajes_db.commit()


# insertar_puesto()

def insertar_empleado_aerolinea():
    vdb.execute("SELECT E.IdEmpleado FROM Empleado E;")
    empleados = vdb.fetchall()
    vdb.execute("SELECT P.IdPuesto, P.Sueldo FROM Puesto P WHERE P.Lugar = 'Aerolínea';")
    puestos = vdb.fetchall()
    vdb.execute("SELECT AE.IdAerolinea FROM Aerolinea AE;")
    aerolineas = vdb.fetchall()

    cantidad_empleados = int(len(empleados) * 0.35)

    while cantidad_empleados > 0:
        puesto = random.choice(puestos)
        fecha_inicio = datetime.datetime.today() - datetime.timedelta(days=random.randrange(100, 12000))
        vdb.execute("INSERT INTO EmpleadoAerolinea ('IdEmpleado', 'IdAerolinea', 'IdPuesto', 'FechaInicio', 'Salario') "
                    "VALUES (?, ?, ?, ?, ?);", (empleados[0][0], random.choice(aerolineas)[0], puesto[0],
                                                fecha_inicio.strftime("%Y-%m-%d"),
                                                puesto[1] + random.randint(0, int(puesto[1] / 2))))
        empleados.remove(empleados[0])
        random.shuffle(empleados)
        cantidad_empleados -= 1
    viajes_db.commit()


# insertar_empleado_aerolinea()

def insertar_empleados_aeropuerto():
    vdb.execute("SELECT E.IdEmpleado FROM Empleado E LEFT JOIN EmpleadoAerolinea EA "
                "ON E.IdEmpleado = EA.IdEmpleado WHERE EA.IdEmpleado IS NULL;")
    empleados = vdb.fetchall()
    vdb.execute("SELECT P.IdPuesto, P.Sueldo FROM Puesto P WHERE P.Lugar = 'Aeropuerto';")
    puestos = vdb.fetchall()
    vdb.execute("SELECT AEP.IdAeropuerto FROM Aeropuerto AEP;")
    aeropuertos = vdb.fetchall()
    cont = 0
    cantidad = len(empleados)
    while cont < cantidad:
        puesto = random.choice(puestos)
        fecha_inicio = datetime.datetime.today() - datetime.timedelta(days=random.randrange(100, 12000))
        vdb.execute(
            "INSERT INTO EmpleadoAeropuerto ('IdEmpleado', 'IdAeropuerto', 'IdPuesto', 'FechaInicio', 'Salario') "
            "VALUES (?, ?, ?, ?, ?);", (empleados[0][0], random.choice(aeropuertos)[0], puesto[0],
                                        fecha_inicio.strftime("%Y-%m-%d"),
                                        puesto[1] + random.randint(0, int(puesto[1] / 2))))
        empleados.remove(empleados[0])
        random.shuffle(empleados)
        cont += 1
    viajes_db.commit()


# insertar_empleados_aeropuerto()


def insertar_equipaje():
    vdb.execute("SELECT V.PesoMaximo, A.CantidadTripulacion, A.IdAvion, V.IdVuelo FROM Vuelo V INNER JOIN Avion ON A.IdAvion = V.IdAvion;")
    vuelos = vdb.fetchall()
    vdb.execute("SELECT U.IdUsuario, PS.IdPasaporte FROM Usuario U INNER JOIN Pasaporte PS ON PS.IdUsuario = U.IdUsuario;")
    usuarios = vdb.fetchall()
    id_equipaje = 1
    for vuelo in vuelos:
        cont = random.randint(10, vuelo[1])
        usuarios_temp = usuarios.copy()
        vdb.execute("SELECT A.IdAsiento FROM Asiento A WHERE A.IdClase IN "
                    "(SELECT C.IdClase FROM Clase C WHERE C.IdAvion =" + str(vuelo[2]) + ");")
        asientos = vdb.fetchall()
        while cont > 0:
            random.shuffle(usuarios_temp)
            random.shuffle(asientos)
            vdb.execute("INSERT INTO Equipaje ('IdUsuario', 'Peso') VALUES (?,?);",
                        (usuarios_temp[0][0], random.randint(1, vuelo[0])))
            vdb.execute("INSERT INTO Tiquete ('IdVuelo', 'IdAsiento', "
                        "'IdEquipaje', 'IdPasaporte') VALUES (?, ?, ?, ?)",
                        (vuelo[3], asientos[0][0], id_equipaje, usuarios_temp[0][1]))
            usuarios_temp.remove(usuarios_temp[0])
            asientos.remove(asientos[0])
            cont -= 1
            id_equipaje += 1
    viajes_db.commit()


def insertar_horarios():
    horarios = [("6am-2pm", "6am-2pm", "6am-2pm", "6am-2pm", "6am-2pm", "6am-2pm", "Libre"),
                ("2pm-10pm", "2pm-10pm", "2pm-10pm", "2pm-10pm", "2pm-10pm", "2pm-10pm", "Libre"),
                ("10pm-6am", "10pm-6am", "10pm-6am", "10pm-6am", "10pm-6am", "10pm-6am", "Libre"),
                ("Libre", "6am-2pm", "6am-2pm", "6am-2pm", "6am-2pm", "6am-2pm", "6am-2pm"),
                ("Libre", "2pm-10pm", "2pm-10pm", "2pm-10pm", "2pm-10pm", "2pm-10pm", "2pm-10pm"),
                ("Libre", "10pm-6am", "10pm-6am", "10pm-6am", "10pm-6am", "10pm-6am", "10pm-6am"),
                ("7am-5pm", "7am-5pm", "7am-5pm", "7am-5pm", "7am-3pm", "Libre", "Libre"),
                ("7am-10pm", "7am-10pm", "7am-10pm", "7am-10pm", "7am-10pm", "7am-10pm", "7am-10pm"),
                ("0:00am-11:59pm", "0:00am-11:59pm", "0:00am-11:59pm", "0:00am-11:59pm", "0:00am-11:59pm",
                 "0:00am-11:59pm", "0:00am-11:59pm")]
    for horario in horarios:
        vdb.execute(
            "INSERT INTO Horario ('Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo') VALUES "
            "(?, ?, ?, ?, ?, ?, ?)", horario)
    viajes_db.commit()


# insertar_horarios()

def insertar_horario_trabajo():
    vdb.execute("SELECT H.IdHorario FROM Horario H WHERE H.IdHorario < 8;")
    horarios = vdb.fetchall()
    vdb.execute("SELECT EA.IdEmpleado, EA.FechaInicio FROM EmpleadoAerolinea EA;")
    empleados_aerolineas = vdb.fetchall()
    vdb.execute("SELECT EAP.IdEmpleado, EAP.FechaInicio FROM EmpleadoAeropuerto EAP;")
    empleados_aeropuertos = vdb.fetchall()
    empleados = empleados_aerolineas + empleados_aeropuertos
    for e_a in empleados:
        cantidad = random.randint(5, 15)
        while cantidad > 0:
            fecha = datetime.datetime.today() - datetime.timedelta(days=random.randrange(100, 12000))
            if fecha.strftime("%Y-%m-%d") >= e_a[1]:
                vdb.execute("INSERT INTO HorarioTrabajo ('IdEmpleado', 'IdHorario', 'Fecha') VALUES "
                            "(?, ?, ?);", (e_a[0], random.choice(horarios)[0], fecha.strftime("%Y-%m-%d")))
                cantidad -= 1
    viajes_db.commit()


def insertar_telefonos():
    vdb.execute("SELECT U.IdUsuario FROM Usuario U;")
    usuarios = vdb.fetchall()

    for usuario in usuarios:
        cant = random.randint(1, 3)
        while cant > 0:
            vdb.execute("INSERT INTO Telefono ('IdUsuario', 'NumeroTelefonico') VALUES (?, ?);",
                        (usuario[0], random.randint(10000000, 999999999)))
            cant -= 1
    viajes_db.commit()

# insertar_telefonos()

# def insertar_intarlos():
#     vdb.execute("INSERT INTO Intervalos ('IntervaloInicio', 'IntervaloFinal')"
#                     " VALUES ('00:00:00', '06:00:00'), ('03:00:01', '06:00:00'), "
#                 "('06:00:01', '09:00:00'), ('09:00:01', '12:00:00'), ('12:00:01', '15:00:00'), "
#                 "('15:00:01', '18:00:00'), ('18:00:01', '21:00:00'), ('21:00:01' , '23:59:59');")
#     viajes_db.commit()

# insertar_intarlos()
