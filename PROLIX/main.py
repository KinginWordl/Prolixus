import json

class Usuario:
    def __init__(self, id, nombre, email, ubicacion=None, contrasena=None):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.ubicacion = ubicacion
        self.contrasena = contrasena
        self.tipo = self._determinar_tipo()

    def _determinar_tipo(self):
        return "Usuario Base"

    def verificar_contrasena(self, intento):
        return self.contrasena == intento

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Email: {self.email}, Tipo: {self.tipo}"

class Trabajador(Usuario):
    def __init__(self, id, nombre, email, habilidades=None, experiencia_laboral=None, certificaciones=None, aspiraciones=None, ubicacion=None, contrasena=None):
        super().__init__(id, nombre, email, ubicacion, contrasena)
        self.habilidades = habilidades if habilidades is not None else []
        self.experiencia_laboral = experiencia_laboral if experiencia_laboral is not None else []
        self.certificaciones = certificaciones if certificaciones is not None else []
        self.aspiraciones = aspiraciones
        self.tipo = "Trabajador"

    def _determinar_tipo(self):
        return "Trabajador"

    def __str__(self):
        return f"{super().__str__()}, Habilidades: {self.habilidades}"

class Coordinador(Usuario):
    def __init__(self, id, nombre, email, experiencia_gestion=None, certificaciones_liderazgo=None, historial_proyectos=None, evaluaciones_desempeno=None, ubicacion=None, contrasena=None):
        super().__init__(id, nombre, email, ubicacion, contrasena)
        self.experiencia_gestion = experiencia_gestion if experiencia_gestion is not None else []
        self.certificaciones_liderazgo = certificaciones_liderazgo if certificaciones_liderazgo is not None else []
        self.historial_proyectos = historial_proyectos if historial_proyectos is not None else []
        self.evaluaciones_desempeno = evaluaciones_desempeno if evaluaciones_desempeno is not None else []
        self.tipo = "Coordinador"

    def _determinar_tipo(self):
        return "Coordinador"

    def __str__(self):
        return f"{super().__str__()}, Experiencia en Gestión: {self.experiencia_gestion}, Certificaciones de Liderazgo: {self.certificaciones_liderazgo}"

class Empresa(Usuario):
    def __init__(self, id, nombre, email, catalogo_productos=None, mision=None, valores=None, impacto_social=None, calificaciones=None, proyectos_innovadores=None, ubicacion=None, contrasena=None):
        super().__init__(id, nombre, email, ubicacion, contrasena)
        self.catalogo_productos = catalogo_productos if catalogo_productos is not None else []
        self.mision = mision
        self.valores = valores
        self.impacto_social = impacto_social
        self.calificaciones = calificaciones if calificaciones is not None else {}
        self.proyectos_innovadores = proyectos_innovadores if proyectos_innovadores is not None else []
        self.tipo = "Empresa"

    def _determinar_tipo(self):
        return "Empresa"

    def __str__(self):
        return f"{super().__str__()}, Catálogo: {self.catalogo_productos}, Calificaciones: {self.calificaciones}"

class ProveedorColaborador(Empresa):
    def __init__(self, id, nombre, email, industria=None, servicios_ofrecidos=None, materiales_ofrecidos=None, valoraciones_proveedor=None, catalogo_productos=None, mision=None, valores=None, impacto_social=None, calificaciones=None, proyectos_innovadores=None, ubicacion=None, contrasena=None):
        super().__init__(id, nombre, email, catalogo_productos, mision, valores, impacto_social, calificaciones, proyectos_innovadores, ubicacion, contrasena)
        self.industria = industria
        self.servicios_ofrecidos = servicios_ofrecidos if servicios_ofrecidos is not None else []
        self.materiales_ofrecidos = materiales_ofrecidos if materiales_ofrecidos is not None else []
        self.valoraciones_proveedor = valoraciones_proveedor if valoraciones_proveedor is not None else {}
        self.tipo = "Proveedor/Colaborador"

    def _determinar_tipo(self):
        return "Proveedor/Colaborador"

    def __str__(self):
        base_str = super().__str__()
        proveedor_str = f", Industria: {self.industria}, Servicios: {self.servicios_ofrecidos}, Materiales: {self.materiales_ofrecidos}, Valoraciones Proveedor: {self.valoraciones_proveedor}"
        return base_str + proveedor_str

class Comprador(Usuario):
    def __init__(self, id, nombre, email, ubicacion=None, contrasena=None):
        super().__init__(id, nombre, email, ubicacion, contrasena)
        self.tipo = "Comprador"

    def _determinar_tipo(self):
        return "Comprador"

class DuenoInversionista(Usuario):
    def __init__(self, id, nombre, email, ubicacion=None, contrasena=None):
        super().__init__(id, nombre, email, ubicacion, contrasena)
        self.tipo = "Dueño/Inversionista"

    def _determinar_tipo(self):
        return "Dueño/Inversionista"

# --- Rutas de los archivos JSON ---
RUTA_TRABAJADORES = 'data/trabajadores.json'
RUTA_COORDINADORES = 'data/coordinadores.json'
RUTA_EMPRESAS = 'data/empresas.json'
RUTA_COMPRADORES = 'data/compradores.json'
RUTA_DUENOINVERSIONISTAS = 'data/duenoinversionistas.json'
RUTA_PROVEEDORES = 'data/proveedores.json'

# --- Funciones para guardar datos (modificada para incluir contraseña) ---
def guardar_datos(ruta_archivo, objeto):
    try:
        with open(ruta_archivo, 'r+') as archivo:
            datos = json.load(archivo)
            datos.append(objeto.__dict__)
            archivo.seek(0)
            json.dump(datos, archivo, indent=4)
            archivo.truncate()
    except FileNotFoundError:
        with open(ruta_archivo, 'w') as archivo:
            json.dump([objeto.__dict__], archivo, indent=4)
    except json.JSONDecodeError:
        with open(ruta_archivo, 'w') as archivo:
            json.dump([objeto.__dict__], archivo, indent=4)

# --- Función para cargar datos ---
def cargar_datos(ruta_archivo, clase):
    usuarios = []
    try:
        with open(ruta_archivo, 'r') as archivo:
            datos = json.load(archivo)
            for dato in datos:
                usuario = clase(**dato)
                usuarios.append(usuario)
    except FileNotFoundError:
        pass
    except json.JSONDecodeError:
        pass
    return usuarios

# --- Función para crear usuario (modificada para pedir contraseña y usar email) ---
def crear_usuario():
    print("\n--- Crear Nuevo Usuario ---")
    print("¿Qué tipo de usuario desea crear?")
    print("1. Trabajador")
    print("2. Coordinador/Manager")
    print("3. Empresa")
    print("4. Comprador")
    print("5. Dueño/Inversionista")
    print("6. Proveedor/Colaborador")

    opcion = input("Seleccione una opción (1-6): ")

    id_usuario = input("Ingrese el ID del usuario: ")
    nombre = input("Ingrese el nombre del usuario: ")
    email = input("Ingrese el correo electrónico del usuario: ")
    ubicacion = input("Ingrese la ubicación del usuario (opcional): ")
    contrasena = input("Ingrese una contraseña de 4 cifras: ")
    while len(contrasena) != 4 or not contrasena.isdigit():
        print("La contraseña debe tener exactamente 4 cifras numéricas.")
        contrasena = input("Ingrese una contraseña de 4 cifras: ")

    if opcion == '1':
        habilidades = input("Ingrese sus habilidades (separadas por coma): ").split(',')
        trabajador = Trabajador(id=id_usuario, nombre=nombre, email=email, habilidades=habilidades, ubicacion=ubicacion, contrasena=contrasena)
        guardar_datos(RUTA_TRABAJADORES, trabajador)
        print("\nPerfil de Trabajador creado y guardado.")
        print(trabajador)
    elif opcion == '2':
        experiencia_gestion = input("Ingrese su experiencia en gestión (separadas por coma): ").split(',')
        coordinador = Coordinador(id=id_usuario, nombre=nombre, email=email, experiencia_gestion=experiencia_gestion, ubicacion=ubicacion, contrasena=contrasena)
        guardar_datos(RUTA_COORDINADORES, coordinador)
        print("\nPerfil de Coordinador creado y guardado.")
        print(coordinador)
    elif opcion == '3':
        nombre_empresa = input("Ingrese el nombre de la empresa: ")
        empresa = Empresa(id=id_usuario, nombre=nombre_empresa, email=email, ubicacion=ubicacion, contrasena=contrasena)
        guardar_datos(RUTA_EMPRESAS, empresa)
        print("\nPerfil de Empresa creado y guardado.")
        print(empresa)
    elif opcion == '4':
        comprador = Comprador(id=id_usuario, nombre=nombre, email=email, ubicacion=ubicacion, contrasena=contrasena)
        guardar_datos(RUTA_COMPRADORES, comprador)
        print("\nPerfil de Comprador creado y guardado.")
        print(comprador)
    elif opcion == '5':
        dueno_inversor = DuenoInversionista(id=id_usuario, nombre=nombre, email=email, ubicacion=ubicacion, contrasena=contrasena)
        guardar_datos(RUTA_DUENOINVERSIONISTAS, dueno_inversor)
        print("\nPerfil de Dueño/Inversionista creado y guardado.")
        print(dueno_inversor)
    elif opcion == '6':
        industria = input("Ingrese la industria de su empresa: ")
        proveedor = ProveedorColaborador(id=id_usuario, nombre=nombre, email=email, industria=industria, ubicacion=ubicacion, contrasena=contrasena)
        guardar_datos(RUTA_PROVEEDORES, proveedor)
        print("\nPerfil de Proveedor/Colaborador creado y guardado.")
        print(proveedor)
    else:
        print("Opción inválida.")

# --- Función para iniciar sesión (usando email y contraseña) ---
def iniciar_sesion():
    print("\n--- Inicio de Sesión ---")
    email_usuario = input("Ingrese su correo electrónico: ")
    contrasena = input("Ingrese su contraseña de 4 cifras: ")

    # Cargar todos los tipos de usuarios y buscar el email y la contraseña
    trabajadores = cargar_datos(RUTA_TRABAJADORES, Trabajador)
    coordinadores = cargar_datos(RUTA_COORDINADORES, Coordinador)
    empresas = cargar_datos(RUTA_EMPRESAS, Empresa)
    compradores = cargar_datos(RUTA_COMPRADORES, Comprador)
    duenos_inversores = cargar_datos(RUTA_DUENOINVERSIONISTAS, DuenoInversionista)
    proveedores = cargar_datos(RUTA_PROVEEDORES, ProveedorColaborador)

    todos_los_usuarios = trabajadores + coordinadores + empresas + compradores + duenos_inversores + proveedores

    for usuario in todos_los_usuarios:
        if usuario.email == email_usuario and usuario.verificar_contrasena(contrasena):
            print(f"\n¡Inicio de sesión exitoso para {usuario.nombre} ({usuario.tipo})!")
            # Aquí podrías implementar la lógica para la sesión del usuario
            return usuario
    print("\nCredenciales incorrectas. Intente nuevamente.")
    return None

if __name__ == "__main__":
    while True:
        print("\n--- Menú Principal ---")
        print("1. Crear Nuevo Usuario")
        print("2. Iniciar Sesión")
        print("3. Salir")

        opcion_menu = input("Seleccione una opción (1-3): ")

        if opcion_menu == '1':
            crear_usuario()
        elif opcion_menu == '2':
            usuario_actual = iniciar_sesion()
            if usuario_actual:
                print(f"\nBienvenido, {usuario_actual.nombre} ({usuario_actual.tipo})!")
                # Aquí podrías iniciar la interfaz principal del usuario
        elif opcion_menu == '3':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
