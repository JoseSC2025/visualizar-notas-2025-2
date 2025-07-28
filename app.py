import streamlit as st
import pandas as pd
import datetime
from io import BytesIO
import requests

# Configuración de la página
st.set_page_config(page_title="Visualizar Notas de Física General 2025-2", page_icon="📚")

# URL del archivo Excel (reemplazar con tu enlace real)
#EXCEL_URL = "https://docs.google.com/spreadsheets/d/1TU_ID_DE_ARCHIVO/export?format=xlsx"
EXCEL_URL = "https://docs.google.com/spreadsheets/d/17bSX9rOMlrOMLlXVrUshexavZxt9BcdN/edit?usp=drive_link&ouid=104569301030055065312&rtpof=true&sd=true"

# Función para cargar datos
#@st.cache_resource(ttl=600)
#def load_data():
#    response = requests.get(EXCEL_URL)
#    return pd.ExcelFile(BytesIO(response.content))

# Reemplaza la función load_data con:
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def load_data():
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    
    # Crea un archivo credentials.json con las credenciales de Google API
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    client = gspread.authorize(creds)
    
    # Abre por URL
    spreadsheet = client.open_by_url("https://docs.google.com/spreadsheets/d/187LELG4kMazPk7cE5VR8IVmWsAC525Pr9ai4Ouixx6Y/edit?usp=sharing")
    return spreadsheet

# Función de autenticación
def authenticate(excel_file, grupo, codigo, password):
    try:
        df = pd.read_excel(excel_file, sheet_name=grupo)
        mask = (df['Código de matrícula'] == codigo) & (df['DNI'] == password)
        if mask.any():
            return df[mask].iloc[0]
        return None
    except:
        return None

# Función para formatear tabla
def format_table(student_data):
    actividades = [
        "Examen Parcial",
        "Examen Final",
        "Exposición Grupal",
        "Cuestionarios",
        "Participación (2%) + Asistencia (3%)",
        "Laboratorio",
        "Promedio"
    ]
    
    ponderacion = [
        "30%", "30%", "10%", "5%", "5%", "20%", "100%"
    ]
    
    notas = [
        student_data['ExParcial'],
        student_data['ExFinal'],
        student_data['Exposición'],
        student_data['Cuestionario'],
        student_data['ParticipaAsiste'],
        student_data['Laboratorio'],
        student_data['Promedio']
    ]
    
    df = pd.DataFrame({
        'Actividades': actividades,
        'Ponderación': ponderacion,
        'Notas': notas
    })
    
    # Calcular promedio (por si acaso)
    recalculated = (
        0.30 * student_data['ExParcial'] +
        0.30 * student_data['ExFinal'] +
        0.10 * student_data['Exposición'] +
        0.05 * student_data['Cuestionario'] +
        0.05 * student_data['ParticipaAsiste'] +
        0.20 * student_data['Laboratorio']
    )
    df.loc[6, 'Notas'] = recalculated
    
    return df

# Interfaz principal
st.title("Visualizar Notas de Física General 2025-2")

# Inicializar estado de sesión
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.student_data = None

# Formulario de login si no está autenticado
if not st.session_state.logged_in:
    grupos = [f"Grupo_{i:02d}" for i in range(1, 16)]
    grupo = st.selectbox("Selecciona tu grupo:", grupos, index=None)
    codigo = st.text_input("Código de matrícula:", max_chars=10)
    password = st.text_input("Contraseña (DNI):", type="password", max_chars=8)
    
    if st.button("Ingresar"):
        if grupo and codigo and password:
            try:
                excel_file = load_data()
                student_data = authenticate(excel_file, grupo, codigo, password)
                
                if student_data is not None:
                    # Actualizar contador de ingresos (simulado)
                    st.session_state.logged_in = True
                    st.session_state.student_data = student_data
                    st.session_state.grupo = grupo
                    st.rerun()
                else:
                    st.error("⚠️ Credenciales incorrectas. Verifica tus datos.")
            except Exception as e:
                st.error(f"Error al acceder a los datos: {str(e)}")
        else:
            st.warning("Por favor completa todos los campos")

# Mostrar datos si está autenticado
else:
    student_data = st.session_state.student_data
    st.success(f"✅ Bienvenido(a): {student_data['Apellidos y Nombre']}")
    
    # Mostrar datos del estudiante
    st.subheader("Tus resultados académicos")
    st.markdown(f"**Grupo:** {st.session_state.grupo}")
    
    # Crear tabla de notas
    df = format_table(student_data)
    
    # Formatear tabla con estilo
    st.dataframe(
        df.style
        .set_properties(**{
            'text-align': 'center',
            'background-color': '#f0f2f6',
            'color': '#333333',
            'border': '1px solid #cccccc'
        })
        .set_table_styles([{
            'selector': 'th',
            'props': [
                ('background-color', '#4a86e8'),
                ('color', 'white'),
                ('font-weight', 'bold'),
                ('text-align', 'center')
            ]
        }])
        .format({"Notas": "{:.2f}"}),
        hide_index=True
    )
    
    # Mensaje motivador
    st.markdown("---")
    st.subheader("📚 Sigamos estudiando...")
    st.markdown("> *El esfuerzo constante es la clave del éxito académico. ¡Sigue así!*")
    
    # Fecha y hora
    now = datetime.datetime.now()
    st.caption(f"Última visualización: {now.strftime('%d/%m/%Y %H:%M:%S')}")
    
    # Botón para salir
    if st.button("Cerrar sesión"):
        st.session_state.logged_in = False
        st.session_state.student_data = None
        st.rerun()

# Notas importantes en el sidebar
st.sidebar.header("Información importante")
st.sidebar.markdown("""
1. Usa tu DNI como contraseña inicial
2. Selecciona tu grupo correctamente
3. Las notas se actualizan periódicamente
4. Contacta al docente si encuentras errores
""")

st.sidebar.markdown("---")
st.sidebar.caption("Sistema Académico - Física General 2025-2")
