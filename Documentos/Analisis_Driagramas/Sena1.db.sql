BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Actividades" (
	"ID_actividades"	INTEGER,
	"id_programa"	INTEGER,
	"Actividad"	TEXT,
	"HorasTotal"	INTEGER,
	"HorasAsig"	INTEGER,
	"Descripcion"	TEXT,
	PRIMARY KEY("ID_actividades" AUTOINCREMENT),
	FOREIGN KEY("id_programa") REFERENCES "Programas"("ID_programa")
);
CREATE TABLE IF NOT EXISTS "Admin" (
	"ID_admin"	INTEGER,
	"Nombre"	TEXT,
	"Apellido"	TEXT,
	"Identificacion"	TEXT,
	"Correo"	TEXT,
	"Password"	TEXT,
	PRIMARY KEY("ID_admin" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Ambientes" (
	"ID_ambiente"	INTEGER,
	"id_sede"	INTEGER,
	"Ambiente"	INTEGER,
	"HorasDia"	INTEGER,
	"HorasAsig"	INTEGER,
	"Descripcion"	TEXT,
	PRIMARY KEY("ID_ambiente" AUTOINCREMENT),
	FOREIGN KEY("id_sede") REFERENCES "Sedes"("ID_sedes")
);
CREATE TABLE IF NOT EXISTS "Bloques" (
	"ID_bloque"	INTEGER,
	"id_centro"	INTEGER,
	"id_sede"	INTEGER,
	"id_ambiente"	INTEGER,
	"id_instructor"	INTEGER,
	"id_programa"	INTEGER,
	"id_ficha"	INTEGER,
	"id_actividad"	INTEGER,
	"Horabloq"	TEXT,
	"Fecha"	TEXT,
	"id_div"	INTEGER,
	PRIMARY KEY("ID_bloque" AUTOINCREMENT),
	FOREIGN KEY("id_actividad") REFERENCES "Actividades"("ID_actividades"),
	FOREIGN KEY("id_ambiente") REFERENCES "Ambientes"("ID_ambiente"),
	FOREIGN KEY("id_centro") REFERENCES "Centros"("ID_centro"),
	FOREIGN KEY("id_ficha") REFERENCES "Fichas"("ID_ficha"),
	FOREIGN KEY("id_instructor") REFERENCES "Instructores"("ID_instructores"),
	FOREIGN KEY("id_programa") REFERENCES "Programas"("ID_programa"),
	FOREIGN KEY("id_sede") REFERENCES "Sedes"("ID_sedes")
);
CREATE TABLE IF NOT EXISTS "Centros" (
	"ID_centro"	INTEGER,
	"Centro"	TEXT,
	"Telefono"	TEXT,
	"Descripcion"	TEXT,
	PRIMARY KEY("ID_centro" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Fichas" (
	"ID_ficha"	INTEGER,
	"id_programa"	INTEGER,
	"Ficha"	TEXT,
	"Descripcion"	TEXT,
	PRIMARY KEY("ID_ficha" AUTOINCREMENT),
	FOREIGN KEY("id_programa") REFERENCES "Programas"("ID_programa")
);
CREATE TABLE IF NOT EXISTS "HorasActi" (
	"ID_Horasacti"	INTEGER,
	"id_actividad"	INTEGER,
	"id_ficha"	INTEGER,
	"Horas"	INTEGER,
	PRIMARY KEY("ID_Horasacti" AUTOINCREMENT),
	FOREIGN KEY("id_actividad") REFERENCES "Actividades"("ID_actividades"),
	FOREIGN KEY("id_ficha") REFERENCES "Fichas"("ID_ficha")
);
CREATE TABLE IF NOT EXISTS "HorasAmbi" (
	"ID_Horasambi"	INTEGER,
	"id_ambiente"	INTEGER,
	"Dia"	TEXT,
	"Horas"	INTEGER,
	PRIMARY KEY("ID_Horasambi" AUTOINCREMENT),
	FOREIGN KEY("id_ambiente") REFERENCES "Ambientes"("ID_ambiente")
);
CREATE TABLE IF NOT EXISTS "HorasInstru" (
	"ID_horasins"	INTEGER,
	"id_instructor"	INTEGER,
	"Semana"	INTEGER,
	"Horas"	INTEGER,
	PRIMARY KEY("ID_horasins" AUTOINCREMENT),
	FOREIGN KEY("id_instructor") REFERENCES "Instructores"("ID_instructores")
);
CREATE TABLE IF NOT EXISTS "Instructores" (
	"ID_instructores"	INTEGER,
	"id_centro"	INTEGER,
	"Nombre"	TEXT,
	"Apellido"	TEXT,
	"NumIdenti"	TEXT,
	"Correo"	TEXT,
	"Tipocontrato"	TEXT,
	"HorasTotal"	INTEGER,
	"HorasAsig"	INTEGER,
	"Password"	TEXT,
	PRIMARY KEY("ID_instructores" AUTOINCREMENT),
	FOREIGN KEY("id_centro") REFERENCES "Centros"("ID_centro")
);
CREATE TABLE IF NOT EXISTS "Programas" (
	"ID_programa"	INTEGER,
	"id_sede"	INTEGER,
	"Programa"	TEXT,
	"id_titulacion"	INTEGER,
	"Descripcion"	TEXT,
	PRIMARY KEY("ID_programa" AUTOINCREMENT),
	FOREIGN KEY("id_sede") REFERENCES "Sedes"("ID_sedes"),
	FOREIGN KEY("id_titulacion") REFERENCES "Titulaciones"("ID_titulo")
);
CREATE TABLE IF NOT EXISTS "Sedes" (
	"ID_sedes"	INTEGER,
	"id_centro"	INTEGER,
	"Sede"	TEXT,
	"Descripcion"	TEXT,
	PRIMARY KEY("ID_sedes" AUTOINCREMENT),
	FOREIGN KEY("id_centro") REFERENCES "Centros"("ID_centro")
);
CREATE TABLE IF NOT EXISTS "Titulaciones" (
	"ID_titulo"	INTEGER,
	"Titulacion"	TEXT,
	"Descripcion"	TEXT,
	PRIMARY KEY("ID_titulo" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "prueba" (
	"ID_Prueba"	INTEGER,
	"id_centro"	INTEGER,
	"Sedes"	TEXT,
	"descripcion"	TEXT,
	PRIMARY KEY("ID_Prueba" AUTOINCREMENT),
	FOREIGN KEY("id_centro") REFERENCES "Centros"("ID_centro")
);
COMMIT;
