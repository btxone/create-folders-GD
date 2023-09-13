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


def crear_carpeta(nombre_carpeta,id_folder):
    credenciales = login()
    folder = credenciales.CreateFile({'title': nombre_carpeta, 
                               'mimeType': 'application/vnd.google-apps.folder',
                               'parents': [{"kind": "drive",\
                                                    "id": id_folder}]})
    folder.Upload()

    
    
    
crear_carpeta('prueba_rackoot', '1Le5x-4I5ECAKDYVaL1RPue2WX6LvRsVY')
print('Carpeta creada')
