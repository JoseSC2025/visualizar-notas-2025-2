Visualización de Notas de Física General 2025-2
Aplicación web para que los estudiantes visualicen sus notas académicas con autenticación segura mediante código de matrícula y DNI.

Características principales
Autenticación segura: Validación por grupo, código de matrícula y DNI

Visualización de notas: Tabla organizada con ponderaciones y cálculos automáticos

Diseño profesional: Interfaz intuitiva con colores y formato claro

Registro de acceso: Contador de ingresos no visible para estudiantes

Elementos motivadores: Mensaje de ánimo para continuar estudiando

Información contextual: Fecha y hora exacta de visualización

Requisitos previos
Python 3.8+

Cuenta de Google Drive para alojar el archivo Excel

Acceso a internet para ejecutar la aplicación

Instalación
Clonar el repositorio:

bash
git clone https://github.com/tuusuario/visualizador-notas-fisica.git
cd visualizador-notas-fisica
Crear entorno virtual (opcional pero recomendado):

bash
python -m venv venv
Activar entorno virtual:

bash
# Linux/Mac:
source venv/bin/activate

# Windows:
.\venv\Scripts\activate
Instalar dependencias:

bash
pip install -r requirements.txt
Configuración
Preparar el archivo Excel:

Crear un libro con hojas: Grupo_01, Grupo_02, ..., Grupo_15

Cada hoja debe tener estas columnas exactas:

text
Código de matrícula, DNI, Apellidos y Nombre, ExParcial, ExFinal, 
Exposición, Cuestionario, ParticipaAsiste, Laboratorio, Promedio, Ingresos
Subir a Google Drive

Obtener enlace público:

En Google Drive: Compartir → "Cualquier persona con el enlace"

Copiar el ID del archivo de la URL:

text
https://docs.google.com/spreadsheets/d/[TU_ID_DE_ARCHIVO]/edit?usp=sharing
Configurar aplicación:

Editar app.py

Reemplazar TU_ID_DE_ARCHIVO con tu ID real:

python
EXCEL_URL = "https://docs.google.com/spreadsheets/d/TU_ID_DE_ARCHIVO/export?format=xlsx"
Ejecución
bash
streamlit run app.py
La aplicación estará disponible en:

text
http://localhost:8501
Uso para estudiantes
Seleccionar grupo del menú desplegable

Ingresar código de matrícula

Ingresar DNI como contraseña

Hacer clic en "Ingresar"

Visualizar notas académicas

Usar "Cerrar sesión" para salir

Estructura del proyecto
text
visualizador-notas-fisica/
├── app.py                # Código principal
├── requirements.txt      # Dependencias
├── README.md             # Documentación
└── .gitignore            # Archivos excluidos de Git
Personalización
Mensaje motivador: Modificar texto en:

python
st.subheader("📚 Sigamos estudiando...")
Colores de tabla: Ajustar códigos hexadecimales en:

python
.set_properties(**{'background-color': '#f0f2f6'})
Fórmula de notas: Editar ponderaciones en:

python
recalculated = (0.30*... + 0.20*...)
Solución de problemas
Error	Solución
Credenciales incorrectas	Verificar grupo, código y DNI en Excel
Archivo no encontrado	Confirmar ID correcto en EXCEL_URL
Datos desactualizados	Esperar 10 min (caché se actualiza automáticamente)
Error de columnas	Verificar nombres exactos de columnas en Excel
Contribución
Hacer fork del proyecto

Crear rama con nueva característica:

bash
git checkout -b nueva-caracteristica
Confirmar cambios:

bash
git commit -m 'Añadir característica X'
Hacer push a la rama:

bash
git push origin nueva-caracteristica
Abrir pull request

Licencia
Distribuido bajo licencia MIT. Ver LICENSE para más información.

Departamento de Física
Facultad de Ciencias
Universidad Nacional de Ingeniería
Ciclo 2025-2

New chat
