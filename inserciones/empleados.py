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
    insercion = "INSERT INTO Aerolinea ('Codigo', 'Nombre', 'ApellidoPat', 'ApellidoMat', 'Sexo',\
    'FechaNacimiento', 'Cedula','CuentaBancaria', 'Direccion')\n VALUES"

    provincia = ["San José", "Alajuela", "Cartago", "Heredia", "Guanacaste", "Puntarenas", "Limón"]
    values = ""
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

        values = values + "\n('" + hashlib.md5(
            (cedula + nombre + apellido_pat + apellido_mat).encode("utf-8")).hexdigest()[0:9] \
                 + "', '" + nombre + "', '" + apellido_pat + "', '" + apellido_mat + "', '" + sexo + "', '" \
                 + fecha_nacimiento.strftime(
            '%Y-%m-%d') + "', '" + cedula + "', '" + cuenta_bancaria + "', '" + direccion
        if cantidad == 1:
            values = values + "');"
            break
        values = values + "'),"
        cantidad -= 1

    insercion = insercion + values
    try:
        vdb.execute(insercion)
    except:
        print("Error")
        return
    viajes_db.commit()


def insertar_empleado():
    vdb.execute("SELECT * FROM Usuario U WHERE U.FechaNacimiento < '2001-01-01';")
    usuarios = vdb.fetchall()
    numero_empleados = random.randint(int(len(usuarios) * 0.2), int(len(usuarios) * 0.3))

    while numero_empleados > 0:
        random.shuffle(usuarios)
        try:
            vdb.execute("INSERT INTO Empleado ('IdUsuario', 'Codigo') VALUES (?, ?);",
                        (usuarios[0][0], hashlib.md5((usuarios[0][1] + usuarios[0][7]).encode('utf-8').hexdgest())))
        except Exception:
            print(Exception)
            return
        usuarios.remove(0)
        numero_empleados -= 1

    viajes_db.commit()


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
        vdb.execute("INSERT INTO Pasaporte ('IdUsuario', 'Nacionalidad', 'LugarNacimiento',"
                    " 'FechaEmision', 'FechaExpiracion', 'LugarEmision', 'CodigoEstado',"
                    "'NumeroSecuencial', 'NumeroPasaporte', 'Tipo') VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (random.choice(usuarios)[0], random.choice(nacionalidades),
                     lugare_nac, fecha_emision.strftime('%Y-%m-%d'),
                     (fecha_emision + datetime.timedelta(2300)).strftime('%Y-%m-%d'),
                     random.choice(lugares_nacimiento), lugare_nac.upper()[0:2],
                     str(random.randint(10000000, 99999999)), str(cantidad),
                     random.choice(tipos)))
        cantidad -= 1
    viajes_db.commit()


def insertar_puesto():
    puestos_aerolinea = [("Piloto", 2000000), ("Azafata", 600000), ("Copiloto", 1200000)]
    puestos_aeropuerto = [("Despachador de vuelos", 400000), ("Técnicos Administrativos", 450000),
                          ("Agente de servicios aeroportuarios", 550000), ("Auxiliar de tierra", 450000)]
    cont = 0
    while cont < 7:
        if cont < 3:
            lugar = "Aeropuerto"
            puesto = random.choice(puestos_aeropuerto)
        else:
            lugar = "Aerolínea"
            puesto = random.choice(puestos_aerolinea)

        vdb.execute("INSERT INTO Puesto ('NombrePuesto', 'Lugar', 'Sueldo') VALUES (?,?,?);",
                    (puesto[0], lugar, puesto[1]))
        cont += 1
    viajes_db.commit()


def insertar_empleado_aerolinea():
    vdb.execute("SELECT E.IdEmpleado FROM Empleado E;")
    empleados = vdb.fetchall()
    vdb.execute("SELECT P.IdPuesto FROM Puesto P WHERE P.Lugar = 'Aerolínea';")
    puestos = vdb.fetchall()
    vdb.execute("SELECT AE.IdAerolinea FROM Aerolinea AE;")
    aerolineas = vdb.fetchall()

    cantidad_empleados = int(len(empleados) * 0.35)

    while cantidad_empleados > 0:
        fecha_inicio = datetime.datetime.today() - datetime.timedelta(days=random.randrange(100, 12000))
        vdb.execute("INSERT INTO EmpleadoAerolinea ('IdEmpleado', 'IdAerolinea', 'IdPuesto', 'FechaInicio') "
                    "VALUES (?, ?, ?, ?);", (empleados[0][0], random.choice(aerolineas)[0], random.choice(puestos)[0],
                                             fecha_inicio.strftime("%Y-%m-%d")))
        empleados.remove(0)
        random.shuffle(empleados)
        cantidad_empleados -= 1
    viajes_db.commit()


def insertar_empleados_aeropuerto():
    vdb.execute("SELECT E.IdEmpleado FROM Empleado E INNER JOIN EmpleadoAerolinea EA ON E.IdEmpleado != EA.IdEmpleado;")
    empleados = vdb.fetchall()
    vdb.execute("SELECT P.IdPuesto FROM Puesto P WHERE P.Lugar = 'Aeropuerto';")
    puestos = vdb.fetchall()
    vdb.execute("SELECT AEP.IdAeropuerto FROM Aeropuerto AEP;")
    aeropuertos = vdb.fetchall()
    cont = 0
    while cont < len(empleados):
        fecha_inicio = datetime.datetime.today() - datetime.timedelta(days=random.randrange(100, 12000))
        vdb.execute("INSERT INTO EmpleadoAeropuerto ('IdEmpleado', 'IdAeropuerto', 'IdPuesto', 'FechaInicio') "
                    "VALUES (?, ?, ?, ?);", (empleados[0][0], random.choice(aeropuertos)[0], random.choice(puestos)[0],
                                             fecha_inicio.strftime("%Y-%m-%d")))
        empleados.remove(0)
        random.shuffle(empleados)
        cont += 1
    viajes_db.commit()


def insertar_equipaje():
    vdb.execute("SELECT U.IdUsuario FROM Usuario U INNER JOIN Pasaporte PS ON PS.IdUsuario = U.IdUsuario;")
    usuarios = vdb.fetchall()
    cont = 0
    while cont < len(usuarios):
        vdb.execute("INSERT INTO Equipaje ('IdUsuario', 'Peso') VALUES (?,?);",
                    random.choice(usuarios)[0], random.randint(2, 5))
        cont += 1
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
                            "(?, ?, ?);", (e_a[0], random.choice(horarios), fecha.strftime("%Y-%m-%d")))
                cantidad -= 1
    viajes_db.commit()

print("SELECT A.IdAvion FROM Avion A INNER JOIN AeropuertoAerolinea AAE ON AAE.IdAeropuerto = " + str(8) + " WHERE A.Estado = 'Inactivo';")