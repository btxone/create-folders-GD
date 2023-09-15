from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive


directorio_credenciales = 'credentials_module.json'

# INICIAR SESION
def login():
    GoogleAuth.DEFAULT_SETTINGS['client_config_file'] = directorio_credenciales
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile(directorio_credenciales)
    
    if gauth.credentials is None:
        gauth.LocalWebserverAuth(port_numbers=[8092])
    elif gauth.access_token_expired:
        gauth.Refresh()
    else:
        gauth.Authorize()
        
    gauth.SaveCredentialsFile(directorio_credenciales)
    credenciales = GoogleDrive(gauth)
    return credenciales


drive = login()

nombre_carpeta = "emblue"

# Busca la carpeta por su nombre
carpetas = drive.ListFile({'q': "title='" + nombre_carpeta + "' and mimeType='application/vnd.google-apps.folder' and trashed=false"}).GetList()

# Verifica si se encontró la carpeta
if len(carpetas) == 1:
    carpeta = carpetas[0]
    carpeta_id = carpeta['id']
    print(f"ID de la carpeta '{nombre_carpeta}': {carpeta_id}")
else:
    print(f"No se encontró una carpeta con el nombre '{nombre_carpeta}' o se encontraron múltiples carpetas con el mismo nombre.")


    