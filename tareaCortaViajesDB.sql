-- -- SQLite
-- CREATE TABLE IF NOT EXISTS Aerolinea(
--     IdAerolinea INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
--     Codigo TEXT NOT NULL,
--     Nombre TEXT NOT NULL
-- );

-- CREATE TABLE IF NOT EXISTS Puesto(
--     IdPuesto INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
--     NombrePuesto TEXT NOT NULL,
--     Lugar TEXT NOT NULL,
--     Sueldo INTEGER NOT NULL
-- );

-- CREATE TABLE IF NOT EXISTS Usuario(
--     IdUsuario INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
--     Codigo TEXT NOT NULL UNIQUE,
--     Nombre TEXT NOT NULL,
--     ApellidoPat TEXT NOT NULL,
--     ApellidoMat TEXT NOT NULL,
--     Sexo CHAR NOT NULL,
--     FechaNacimiento DATE NOT NULL,
--     Cedula TEXT NOT NULL,
--     CuentaBancaria TEXT NOT NULL,
--     Direccion TEXT NOT NULL
-- );

-- CREATE TABLE IF NOT EXISTS Telefono(
--     IdUsuario INTEGER NOT NULL,
--     NumeroTelefonico TEXT NOT NULL,
--     FOREIGN KEY (IdUsuario) REFERENCES Usuario(IdUsuario)
-- );

-- CREATE TABLE IF NOT EXISTS Empleado(
--     IdEmpleado INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
--     IdUsuario INTEGER NOT NULL,
--     Codigo TEXT NOT NULL,
--     FOREIGN KEY (IdUsuario) REFERENCES Usuario(IdUsuario)
-- );

-- CREATE TABLE IF NOT EXISTS Horario(
--     IdHorario INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
--     Lunes TEXT,
--     Martes TEXT,
--     Miercoles TEXT,
--     Jueves TEXT,
--     Viernes TEXT,
--     Sabado TEXT,
--     Domingo TEXT
-- );

-- CREATE TABLE IF NOT EXISTS Aeropuerto(
--     IdAeropuerto INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
--     Nombre TEXT NOT NULL,
--     Telefono TEXT NOT NULL,
--     Localizacion TEXT NOT NULL,
--     Codigo TEXT NOT NULL
-- );

-- CREATE TABLE IF NOT EXISTS AeropuertoAerolinea(
--     IdAeropuerto INTEGER NOT NULL,
--     IdAerolinea INTEGER NOT NULL,
--     FOREIGN KEY (IdAeropuerto) REFERENCES Aeropuerto(IdAeropuerto),
--     FOREIGN KEY (IdAerolinea) REFERENCES Aerolinea(IdUsuario)
-- );

-- CREATE TABLE IF NOT EXISTS HorarioTrabajo(
--     IdEmpleado INTEGER NOT NULL,
--     IdHorario INTEGER NOT NULL,
--     Fecha TEXT NOT NULL,
--     FOREIGN KEY (IdEmpleado) REFERENCES Empleado(IdEmpleado),
--     FOREIGN KEY (IdHorario) REFERENCES Horario(IdHorario)
-- );

-- CREATE TABLE IF NOT EXISTS HorarioServicio(
--     IdAeropuerto INTEGER NOT NULL,
--     IdHorario INTEGER NOT NULL,
--     Fecha TEXT NOT NULL,
--     FOREIGN KEY (IdAeropuerto) REFERENCES Aeropuerto(IdAeropuerto),
--     FOREIGN KEY (IdHorario) REFERENCES Horario(IdHorario)
-- );

-- CREATE TABLE IF NOT EXISTS Fabricante(
--     IdFabricante INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
--     Nombre TEXT NOT NULL
-- );

-- CREATE TABLE IF NOT EXISTS Avion(
--     IdAvion INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
--     IdAerolinea INTEGER NOT NULL,
--     IdFabricante INTEGER NOT NULL,
--     Codigo TEXT NOT NULL,
--     Modelo TEXT NOT NULL,
--     CapacidadTripulacion INTEGER NOT NULL,
--     CapacidadItinerario INTEGER NOT NULL,
--     Estado TEXT NOT NULL,
--     Posicion TEXT NOT NULL,
--     FOREIGN KEY (IdAerolinea) REFERENCES Aerolinea(IdAerolinea),
--     FOREIGN KEY (IdFabricante) REFERENCES Fabricante(IdFabricante)
-- );

-- CREATE TABLE IF NOT EXISTS Vuelo(
--     IdVuelo INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
--     IdAvion INTEGER NOT NULL,
--     NumeroVuelo INTEGER NOT NULL UNIQUE,
--     Origen TEXT NOT NULL,
--     Destino TEXT NOT NULL,
--     FechaHoraSalida DATETIME NOT NULL,
--     FechaHoraLlegada DATETIME NOT NULL,
--     Estado TEXT NOT NULL,
--     Precio INTEGER NOT NULL,
--     PesoMaximo INTEGER NOT NULL,
--     FOREIGN KEY (IdAvion) REFERENCES Avion(IdAvion)
-- );

-- CREATE TABLE IF NOT EXISTS Clase(
--     IdClase INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
--     IdAvion INTEGER NOT NULL,
--     Tipo TEXT NOT NULL,
--     Precio INTEGER NOT NULL,
--     FOREIGN KEY (IdAvion) REFERENCES Avion(IdAvion)
-- );

-- CREATE TABLE IF NOT EXISTS Asiento (
--     IdAsiento INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
--     IdClase INTEGER NOT NULL,
--     NumeroAsiento INTEGER NOT NULL,
--     FOREIGN KEY (IdClase) REFERENCES Clase(IdClase) 
-- );

-- CREATE TABLE IF NOT EXISTS Equipaje(
--     IdEquipaje INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
--     IdUsuario INTEGER NOT NULL,
--     Peso INTEGER NOT NULL,
--     FOREIGN KEY (IdUsuario) REFERENCES Usuario(IdUsuario)
-- );

-- CREATE TABLE IF NOT EXISTS Pasaporte(
--     IdPasaporte INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
--     IdUsuario INTEGER NOT NULL,
--     Nacionalidad TEXT NOT NULL,
--     LugarNacimiento TEXT NOT NULL,
--     FechaEmision DATE NOT NULL,
--     FechaExpiracion DATE NOT NULL,
--     LugarEmision TEXT NOT NULL,
--     CodigoEstado TEXT NOT NULL,
--     NumeroSecuencial TEXT NOT NULL,
--     NumeroPasaporte TEXT NOT NULL,
--     Tipo TEXT NOT NULL,
--     FOREIGN KEY (IdUsuario) REFERENCES Usuario(IdUsuario)
-- );

-- CREATE TABLE IF NOT EXISTS EmpleadoAerolinea(
--     IdEmpleado INTEGER NOT NULL,
--     IdAerolinea INTEGER NOT NULL,
--     IdPuesto INTEGER NOT NULL,
--     FechaInicio DATE NOT NULL,
--     Salario INTEGER NOT NULL,
--     FOREIGN KEY (IdEmpleado) REFERENCES Empleado(IdEmpleado),
--     FOREIGN KEY (IdAerolinea) REFERENCES Aerolinea(IdAerolinea),
--     FOREIGN KEY (IdPuesto) REFERENCES Puesto(IdPuesto)
-- );

-- CREATE TABLE IF NOT EXISTS EmpleadoAeropuerto(
--     IdEmpleado INTEGER NOT NULL,
--     IdAeropuerto INTEGER NOT NULL,
--     IdPuesto INTEGER NOT NULL,
--     FechaInicio DATE NOT NULL,
--     Salario INTEGER NOT NULL,
--     FOREIGN KEY (IdEmpleado) REFERENCES Empleado(IdEmpleado),
--     FOREIGN KEY (IdAeropuerto) REFERENCES Aeropuerto(IdAeropuerto),
--     FOREIGN KEY (IdPuesto) REFERENCES Puesto(IdPuesto)
-- );


-- CREATE TABLE IF NOT EXISTS Bodega(
--     IdBodega INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
--     IdAeropuerto INTEGER NOT NULL,
--     Nombre TEXT NOT NULL,
--     FOREIGN KEY (IdAeropuerto) REFERENCES Aeropuerto(IdAeropuerto)
-- );

-- CREATE TABLE IF NOT EXISTS BodegaAvion(
--     IdBodega INTEGER NOT NULL,
--     IdAvion INTEGER NOT NULL,
--     FechaHoraLlegada DATETIME NOT NULL,
--     FechaHoraSalida DATETIME,
--     FOREIGN KEY (IdBodega) REFERENCES Bodega(IdBodega),
--     FOREIGN KEY (IdAvion) REFERENCES Avion(IdAvion)
-- );

-- CREATE TABLE IF NOT EXISTS ControladorVuelo(
--     IdControladorVuelo INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
--     IdVuelo INTEGER NOT NULL,
--     CodigoComunicacion TEXT NOT NULL,
--     FOREIGN KEY (IdVuelo) REFERENCES Vuelo(IdVuelo)
-- );

-- CREATE TABLE IF NOT EXISTS Tiquete(
--     IdTiquete INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
--     IdVuelo INTEGER NOT NULL,
--     IdAsiento INTEGER NOT NULL,
--     IdEquipaje INTEGER NOT NULL,
--     IdPasaporte INTEGER NOT NULL,
--     FOREIGN KEY (IdVuelo) REFERENCES Vuelo(IdVuelo),
--     FOREIGN KEY (IdEquipaje) REFERENCES Equipaje(IdEquipaje),
--     FOREIGN KEY (IdPasaporte) REFERENCES Pasaporte(IdPasaporte),
--     FOREIGN KEY (IdAsiento) REFERENCES Asiento(IdAsiento)
-- );


-- CREATE TABLE IF NOT EXISTS Taller(
--     IdTaller INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
--     IdAeropuerto INTEGER NOT NULL,
--     Nombre TEXT NOT NULL,
--     FOREIGN KEY (IdAeropuerto) REFERENCES Aeropuerto(IdAeropuerto)
-- );

-- CREATE TABLE IF NOT EXISTS TallerAvion(
--     IdTallerAvion INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
--     IdTaller INTEGER NOT NULL,
--     IdAvion INTEGER NOT NULL,
--     FechaHoraSalida DATETIME,
--     FechaHoraLlegada DATETIME NOT NULL,
--     FOREIGN KEY (IdTaller) REFERENCES Taller(IdTaller),
--     FOREIGN KEY (IdAvion) REFERENCES Avion(IdAvion)
-- );

-- CREATE TABLE IF NOT EXISTS Factura(
--     IdFactura INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
--     IdTallerAvion INTEGER NOT NULL,
--     Costo INTEGER NOT NULL,
--     FOREIGN KEY (IdTallerAvion) REFERENCES TallerAvion(IdTallerAvion)
-- );

-- CREATE TABLE IF NOT EXISTS Daño(
--     IdFactura INTEGER NOT NULL,
--     Descripcion TEXT NOT NULL,
--     FOREIGN KEY (IdFactura) REFERENCES Factura(IdFactura)
-- );

-- CREATE TABLE IF NOT EXISTS Repuesto(
--     IdFactura INTEGER NOT NULL,
--     Descripcion TEXT NOT NULL,
--     FOREIGN KEY (IdFactura) REFERENCES Factura(IdFactura)
-- );

-- Consultas
-- 1) TOP 10 Aerolíneas 
SELECT AE.Nombre
FROM Aerolinea AE
WHERE AE.IdAerolinea IN 
	(SELECT EA.IdAerolinea 
	FROM EmpleadoAerolinea EA 
	GROUP BY EA.IdAerolinea 
	ORDER BY COUNT(EA.IdAerolinea) DESC 
	LIMIT 10);

-- 2) TOP 10 Aeropuertos
SELECT AEP.Nombre
FROM Aeropuerto AEP
WHERE AEP.IdAeropuerto IN 
	(SELECT AA.IdAeropuerto
	FROM AeropuertoAerolinea AA 
	GROUP BY AA.IdAeropuerto 
	ORDER BY COUNT(AA.IdAeropuerto) DESC 
	LIMIT 10);

-- 3) Informacion de empleados con mas salarios
SELECT U.*
FROM Usuario U 
INNER JOIN Empleado E ON E.IdUsuario = U.IdUsuario
WHERE E.IdEmpleado IN
	(
	SELECT EA.IdEmpleado FROM EmpleadoAerolinea EA
	GROUP BY EA.IdEmpleado ORDER BY EA.Salario DESC
	LIMIT 1
	)
	OR E.IdEmpleado IN
	(
	SELECT EAP.IdEmpleado FROM EmpleadoAeropuerto EAP
	GROUP BY EAP.IdEmpleado ORDER BY EAP.Salario DESC
	LIMIT 1
	);

-- 4) Promedio de salarios de aeropuertos
SELECT AVG(EA.Salario) AS Promedio, A.Nombre
FROM Aeropuerto A
INNER JOIN EmpleadoAeropuerto EA
ON EA.IdAeropuerto = A.IdAeropuerto
GROUP BY EA.IdAeropuerto
ORDER BY COUNT(EA.IdAeropuerto) DESC;

-- 5) Cantidad de aviones en reparacion para una aerolinea
SELECT COUNT(A.IdAerolinea) AS 'Cantidad de aviones', AE.Nombre AS 'Aerolínea' 
FROM Avion A
INNER JOIN Aerolinea AE ON A.IdAerolinea = AE.IdAerolinea
WHERE AE.Nombre = "Emirates" AND A.Estado = "En reparacion";

-- 6) Informacion del avion
SELECT FA.Costo AS 'Costo de reparación', A.Modelo, F.Nombre AS 'Fabricante', A.Codigo
FROM Avion A 
INNER JOIN Fabricante F ON A.IdFabricante = F.IdFabricante
INNER JOIN TallerAvion TA ON TA.IdAvion = A.IdAvion
INNER JOIN Factura FA ON FA.IdTallerAvion = TA.IdTallerAvion
INNER JOIN Taller T ON T.IdTaller = TA.IdTaller
INNER JOIN Aeropuerto AEP ON AEP.IdAeropuerto = T.IdAeropuerto
INNER JOIN Aerolinea AE ON AE.IdAerolinea = A.IdAerolinea
WHERE AE.Nombre = "Avianca" AND AEP.Nombre = "Aeropuerto de Changi";

-- 7) Cantidad aviones en aeropuerto
SELECT COUNT(AEP.Localizacion) AS 'Aviones activos'
FROM Avion A
INNER JOIN  Aeropuerto AEP ON AEP.Localizacion = A.Posicion
WHERE AEP.Nombre = "Aeropuerto de Changi" AND A.Estado = "Activo";

-- 8) Promedio costo de reparacion para un aeropuerto
SELECT AVG(FA.Costo) AS 'Promedio costo de reparación', AEP.Nombre
FROM Factura FA
INNER JOIN TallerAvion TA ON TA.IdTallerAvion = FA.IdTallerAvion
INNER JOIN Taller T ON T.IdTaller = TA.IdTaller
INNER JOIN Aeropuerto AEP ON T.IdAeropuerto = AEP.IdAeropuerto
WHERE AEP.Nombre = "Aeropuerto de Changi";

-- 9) Cantidad de aviones inactivos en una bodega
SELECT COUNT(B.IdBodega) as 'Cantidad de aviones inactivos'
FROM Avion A
INNER JOIN BodegaAvion BA ON BA.IdAvion = A.IdAvion
INNER JOIN Bodega B ON B.IdBodega = BA.IdBodega
INNER JOIN Aeropuerto AEP ON AEP.IdAeropuerto = B.IdAeropuerto
WHERE B.Nombre = "Bodega Aeropuerto de Changi" AND A.Estado = "Inactivo" AND A.Posicion = AEP.Localizacion;

-- 10) Fabricantes con mayor cantidad de modelos
SELECT F.Nombre, COUNT(F.Nombre) AS 'Cantidad de modelos'
FROM Fabricante F
INNER JOIN Avion A ON A.IdFabricante = F.IdFabricante
GROUP BY F.Nombre
ORDER BY COUNT(F.Nombre) DESC;

-- 11) Cantidad de vuelos activos de aerolineas con la letra 'a'
SELECT AE.Nombre, COUNT(AE.Nombre) AS 'Cantidad de vuelos activos'
FROM Aerolinea AE
INNER JOIN Avion A ON A.IdAerolinea = AE.IdAerolinea
INNER JOIN Vuelo V ON V.IdAvion = A.IdAvion
WHERE INSTR(LOWER(AE.Nombre), 'a') > 0 AND V.Estado = "Activo"
GROUP BY AE.Nombre
ORDER BY COUNT(AE.Nombre) DESC;

-- 12) Intervalo de horas en el que llegan mas vuelos

CREATE TEMP TABLE IF NOT EXISTS Intervalos (
IntervaloInicio TIME NOT NULL,
IntervaloFinal TIME NOT NULL);
INSERT INTO Intervalos ('IntervaloInicio', 'IntervaloFinal')
VALUES ('00:00:00', '03:00:00'),
('03:00:01', '06:00:00'),
('06:00:01', '09:00:00'),
('09:00:01', '12:00:00'),
('12:00:01', '15:00:00'),
('15:00:01', '18:00:00'),
('18:00:01', '21:00:00'), 
('21:00:01' , '23:59:59');

SELECT I.IntervaloInicio, I.IntervaloFinal
FROM Intervalos I
INNER JOIN Vuelo V ON strftime('%H:%M:%f', V.FechaHoraLlegada) BETWEEN I.IntervaloInicio AND I.IntervaloFinal
INNER JOIN Aeropuerto AEP ON V.Destino = AEP.Localizacion
WHERE AEP.Nombre = "Aeropuerto de Munich"
GROUP BY V.FechaHoraLlegada
ORDER BY COUNT(V.FechaHoraLlegada) DESC
LIMIT 1;

DROP TABLE Intervalos;