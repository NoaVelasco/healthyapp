import re
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate(r"cred\desappgcp-firebase-adminsdk-pxid8-73aa5b9b41.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
formato = '(formato numérico "dd mm aaaa")'

# ----------------- Funciones CRUD -------------------------
# Create a new document in Firestore
def create_document(collection, document_data):
    custom_id = document_data["dia"]
    custom_id = re.sub("[-/ ]", "_", custom_id)
    doc_ref = db.collection(collection).document(f"{custom_id}_id")
    doc_ref.set(document_data)
    print("Has registrado este día con el código:", doc_ref.id)


# Read a document from Firestore
def read_document(collection, document_id):
    document_id = re.sub("[-/ ]", "_", document_id)
    document_id = f"{document_id}_id"
    doc_ref = db.collection(collection).document(document_id)
    document = doc_ref.get()
    if document.exists:
        print("Tus datos solicitados:", document.to_dict())
    else:
        print("¡No existe el día solicitado!")

# Update a document in Firestore
def update_document(collection, document_id, update_data):
    document_id = re.sub("[-/ ]", "_", document_id)
    document_id = f"{document_id}_id"
    doc_ref = db.collection(collection).document(document_id)
    doc_ref.update(update_data)
    print('¡Día modificado con éxito!')

# Delete a document from Firestore
def delete_document(collection, document_id):
    document_id = re.sub("[-/ ]", "_", document_id)
    document_id = f"{document_id}_id"
    doc_ref = db.collection(collection).document(document_id)
    doc_ref.delete()
    print("¡Día eliminado con éxito!")

# OTRAS FUNCIONES -----------------------------------
def comprueba(input):
    pat = r"[0-9]{2}[-/ ][0-9]{2}[-/ ][0-9]{4}"
    search = re.search(pat, input)
    if search:
        return True
    else:
        print("No es una fecha válida")
        return False

options = {
    1: 'Añadir día',
    2: 'Consultar día',
    3: 'Actualizar día',
    4: 'Eliminar día',
    5: 'Salir'
}

def menu(options):
    print("\nMENÚ PRINCIPAL: 😴 SUEÑO\n\
🌜✨✨✨✨✨✨✨✨✨✨✨✨✨🌛")
    for i, option in options.items():
        print(f"✨ {i}: {option}")

# -----------------ejemplos -------------------------

# Usage example
# create_document("users", {"name": "John Doe", "email": "johndoe@example.com"})

# Usage example
# read_document("sueno", "8NuoOdJMJTThM2679NeC")

# Usage example
# update_document('users', 'document_id123', {'name': 'Jane Smith'})

# Usage example
# delete_document("users", "document_id123")
# -----------------menu -------------------------
    


if __name__ == "__main__":
    loop = True
    print("\nTe damos la bienvenida a la mejor aplicación de salud: HealthyApp. 😉")

    while loop:
        menu(options)

        selection = input("🌜✨✨✨✨✨✨✨✨✨✨✨✨✨🌛\n\nElige tu opción: ")

        # Print the message corresponding to the user's selection.
        if selection == "1":
            fecha_correcta = False
            while fecha_correcta is False:
                what_day = input(f"\nIntroduce el día que quieres añadir {formato}: ")
                fecha_correcta = comprueba(what_day)

            what_hour = int(input("Introduce las horas de sueño que quieres registrar: "))
            create_document("sueno", {"dia":what_day, "hora":what_hour})
        elif selection == "2":
            what_day = input(f"\n¿Qué día quieres consultar? {formato} ")
            read_document("sueno", what_day)
        elif selection == "3":
            id_input = input(f"\n¿Qué día quieres modificar? {formato} ")
            what_hour = int(input("Introduce las horas de sueño actualizadas: "))
            update_document("sueno", id_input, {"hora":what_hour})
        elif selection == "4":
            id_input = input(f"\n¿Qué día quieres eliminar? {formato} ")
            delete_document("sueno", id_input)

        elif selection == "5":
            print("Has decidido salir. Ten un buen descanso. 🌚\n")
            loop = False
