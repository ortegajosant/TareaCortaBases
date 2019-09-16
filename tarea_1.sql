-- SQLite
CREATE TABLE IF NOT EXISTS Aerolinea(
    IdAerolinea INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Codigo TEXT NOT NULL,
    Nombre TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Puesto(
    IdPuesto INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    NombrePuesto TEXT NOT NULL,
    Sueldo TEXT NOT NULL,
    FechaInicio DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS Usuario(
    IdUsuario INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Codigo TEXT NOT NULL UNIQUE,
    Nombre TEXT NOT NULL,
    ApellidoPat TEXT NOT NULL,
    ApellidoMat TEXT NOT NULL,
    Cedula TEXT NOT NULL,
    CuentaBancaria TEXT NOT NULL,
    Direccion TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Telefono(
    IdUsuario INTEGER NOT NULL,
    NumeroTelefonico TEXT NOT NULL,
    FOREIGN KEY (IdUsuario) REFERENCES Usuario(IdUsuario)
);

CREATE TABLE IF NOT EXISTS Empleado(
    IdEmpleado INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    IdUsuario INTEGER NOT NULL,
    Codigo TEXT NOT NULL,
    FOREIGN KEY (IdUsuario) REFERENCES Usuario(IdUsuario)
);

CREATE TABLE IF NOT EXISTS Horario(
    IdHorario INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Lunes TEXT,
    Martes TEXT,
    Miercoles TEXT,
    Jueves TEXT,
    Viernes TEXT,
    Sabado TEXT,
    Domingo TEXT
);

CREATE TABLE IF NOT EXISTS Aeropuerto(
    IdAeropuerto INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Nombre TEXT NOT NULL,
    Telefono TEXT NOT NULL,
    Localizacion TEXT NOT NULL,
    Codigo TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS AeropuertoAerolinea(
    IdAeropuerto INTEGER NOT NULL,
    IdAerolinea INTEGER NOT NULL,
    FOREIGN KEY (IdAeropuerto) REFERENCES Aeropuerto(IdAeropuerto),
    FOREIGN KEY (IdAerolinea) REFERENCES Aerolinea(IdUsuario)
);

CREATE TABLE IF NOT EXISTS HorarioTrabajo(
    IdEmpleado INTEGER NOT NULL,
    IdHorario INTEGER NOT NULL,
    Fecha TEXT NOT NULL,
    FOREIGN KEY (IdEmpleado) REFERENCES Empleado(IdEmpleado),
    FOREIGN KEY (IdHorario) REFERENCES Horario(IdHorario)
);

CREATE TABLE IF NOT EXISTS HorarioServicio(
    IdAeropuerto INTEGER NOT NULL,
    IdHorario INTEGER NOT NULL,
    Fecha TEXT NOT NULL,
    FOREIGN KEY (IdAeropuerto) REFERENCES Aeropuerto(IdAeropuerto),
    FOREIGN KEY (IdHorario) REFERENCES Horario(IdHorario)
);

CREATE TABLE IF NOT EXISTS Fabricante(
    IdFabricante INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Nombre TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Avion(
    IdAvion INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    IdAerolinea INTEGER NOT NULL,
    IdFabricante INTEGER NOT NULL,
    Codigo TEXT NOT NULL,
    Modelo TEXT NOT NULL,
    CapacidadTripulacion INTEGER NOT NULL,
    CapacidadItinerario INTEGER NOT NULL,
    Estado TEXT NOT NULL,
    Posicion TEXT NOT NULL,
    FOREIGN KEY (IdAerolinea) REFERENCES Aerolinea(IdAerolinea),
    FOREIGN KEY (IdFabricante) REFERENCES Fabricante(IdFabricante)
);

CREATE TABLE IF NOT EXISTS Vuelo(
    IdVuelo INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    IdAvion INTEGER NOT NULL,
    NumeroVuelo INTEGER NOT NULL UNIQUE,
    Origen TEXT NOT NULL,
    Destino TEXT NOT NULL,
    FechaHoraSalida DATETIME NOT NULL,
    FechaHoraLlegada DATETIME NOT NULL,
    Estado TEXT NOT NULL,
    Precio INTEGER NOT NULL,
    FOREIGN KEY (IdAvion) REFERENCES Avion(IdAvion)
);

CREATE TABLE IF NOT EXISTS Clase(
    IdClase INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    IdAvion INTEGER NOT NULL,
    Tipo TEXT NOT NULL,
    Precio INTEGER NOT NULL,
    FOREIGN KEY (IdAvion) REFERENCES Avion(IdAvion)
);

CREATE TABLE IF NOT EXISTS Equipaje(
    IdEquipaje INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    IdUsuario INTEGER NOT NULL,
    Peso INTEGER NOT NULL,
    FOREIGN KEY (IdUsuario) REFERENCES Usuario(IdUsuario)
);

CREATE TABLE IF NOT EXISTS Pasaporte(
    IdPasaporte INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    IdUsuario INTEGER NOT NULL,
    Nacionalidad TEXT NOT NULL,
    LugarNacimiento TEXT NOT NULL,
    FechaNacimiento DATE NOT NULL,
    FechaEmision DATE NOT NULL,
    FechaExpiracion DATE NOT NULL,
    LugarEmision TEXT NOT NULL,
    Sexo TEXT NOT NULL,
    CodigoEstado TEXT NOT NULL,
    NumeroSecuencial TEXT NOT NULL,
    NumeroPasaporte TEXT NOT NULL,
    Tipo TEXT NOT NULL,
    FOREIGN KEY (IdUsuario) REFERENCES Usuario(IdUsuario)
);

CREATE TABLE IF NOT EXISTS EmpleadoAerolinea(
    IdEmpleado INTEGER NOT NULL,
    IdAerolinea INTEGER NOT NULL,
    IdPuesto INTEGER NOT NULL,
    FOREIGN KEY (IdEmpleado) REFERENCES Empleado(IdEmpleado),
    FOREIGN KEY (IdAerolinea) REFERENCES Aerolinea(IdAerolinea),
    FOREIGN KEY (IdPuesto) REFERENCES Puesto(IdPuesto)
);

CREATE TABLE IF NOT EXISTS EmpleadoAeropuerto(
    IdEmpleado INTEGER NOT NULL,
    IdAeropuerto INTEGER NOT NULL,
    IdPuesto INTEGER NOT NULL,
    FOREIGN KEY (IdEmpleado) REFERENCES Empleado(IdEmpleado),
    FOREIGN KEY (IdAeropuerto) REFERENCES Aeropuerto(IdAeropuerto),
    FOREIGN KEY (IdPuesto) REFERENCES Puesto(IdPuesto)
);

CREATE TABLE IF NOT EXISTS Bodega(
    IdBodega INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    IdAeropuerto INTEGER NOT NULL,
    Nombre TEXT NOT NULL,
    FOREIGN KEY (IdAeropuerto) REFERENCES Aeropuerto(IdAeropuerto)
);

CREATE TABLE IF NOT EXISTS BodegaAvion(
    IdBodega INTEGER NOT NULL,
    IdAvion INTEGER NOT NULL,
    FechaHoraLlegada DATETIME NOT NULL,
    FechaHoraSalida DATETIME,
    FOREIGN KEY (IdBodega) REFERENCES Bodega(IdBodega),
    FOREIGN KEY (IdAvion) REFERENCES Avion(IdAvion)
);

CREATE TABLE IF NOT EXISTS ControladorVuelo(
    IdControladorVuelo INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    IdVuelo INTEGER NOT NULL,
    CodigoComunicacion TEXT NOT NULL,
    FOREIGN KEY (IdVuelo) REFERENCES Vuelo(IdVuelo)
);

CREATE TABLE IF NOT EXISTS Tiquete(
    IdTiquete INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    IdVuelo INTEGER NOT NULL,
    IdEquipaje INTEGER NOT NULL,
    IdPasaporte INTEGER NOT NULL,
    FOREIGN KEY (IdVuelo) REFERENCES Vuelo(IdVuelo),
    FOREIGN KEY (IdEquipaje) REFERENCES Equipaje(IdEquipaje),
    FOREIGN KEY (IdPasaporte) REFERENCES Pasaporte(IdPasaporte)
);

CREATE TABLE IF NOT EXISTS Taller(
    IdTaller INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    IdAeropuerto INTEGER NOT NULL,
    Nombre TEXT NOT NULL,
    FOREIGN KEY (IdAeropuerto) REFERENCES Aeropuerto(IdAeropuerto)
);

CREATE TABLE IF NOT EXISTS TallerAvion(
    IdTaller INTEGER NOT NULL,
    IdAvion INTEGER NOT NULL,
    FOREIGN KEY (IdTaller) REFERENCES Taller(IdTaller),
    FOREIGN KEY (IdAvion) REFERENCES Avion(IdAvion)
);

CREATE TABLE IF NOT EXISTS Factura(
    IdFactura INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    IdTaller INTEGER NOT NULL,
    Costo INTEGER NOT NULL,
    FechaHoraSalida DATETIME NOT NULL,
    FechaHoraLlegada DATETIME NOT NULL,
    FOREIGN KEY (IdTaller) REFERENCES Taller(IdTaller)
);

CREATE TABLE IF NOT EXISTS Daño(
    IdTaller INTEGER NOT NULL,
    Descripcion TEXT NOT NULL,
    FOREIGN KEY (IdTaller) REFERENCES Taller(IdTaller)
);

CREATE TABLE IF NOT EXISTS Repuesto(
    IdTaller INTEGER NOT NULL,
    Descripcion TEXT NOT NULL,
    FOREIGN KEY (IdTaller) REFERENCES Taller(IdTaller)
);