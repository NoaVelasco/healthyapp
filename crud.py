import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate(r"cred\desappgcp-firebase-adminsdk-pxid8-73aa5b9b41.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# -----------------CRUD -------------------------
# Create a new document in Firestore
def create_document(collection, document_data):
    # db = firestore.client()
    doc_ref = db.collection(collection).document()
    doc_ref.set(document_data)
    print("Document created with ID:", doc_ref.id)


# Read a document from Firestore
def read_document(collection, document_id):
    # db = firestore.client()
    doc_ref = db.collection(collection).document(document_id)
    document = doc_ref.get()
    if document.exists:
        print("Document data:", document.to_dict())
    else:
        print("No such document!")

# Update a document in Firestore
def update_document(collection, document_id, update_data):
    db = firestore.client()
    doc_ref = db.collection(collection).document(document_id)
    doc_ref.update(update_data)
    print('Document updated successfully!')

# Delete a document from Firestore
def delete_document(collection, document_id):
    db = firestore.client()
    doc_ref = db.collection(collection).document(document_id)
    doc_ref.delete()
    print("Document deleted successfully!")


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
    
options = {
    1: 'crear registro',
    2: 'consultar registro',
    3: 'actualizar registro',
    4: 'eliminar registro',
    5: 'salir'
}

def menu(options):
    print("Elige una opción")
    for i, option in options.items():
        print(f"{i}: {option}")


loop = True

while loop:
    menu(options)

    selection = input("Enter your selection: ")

    # Print the message corresponding to the user's selection.
    if selection == "1":
        print("Has seleccionado la opción 1.")
        what_day = int(input("Introduce el día que quieres registrar: "))
        what_hour = int(input("Introduce las horas de sueño que quieres registrar: "))
        create_document("sueno", {"dia":what_day, "hora":what_hour})
    elif selection == "2":
        print("Has seleccionado la opción 2.")
        what_day = input("¿Qué ID quieres consultar? ")
        read_document("sueno", what_day)
    elif selection == "3":
        print("Has seleccionado la opción 3.")
        id_input = input("¿Qué registro quieres modificar? ")
        what_hour = int(input("Introduce las horas de sueño actualizadas: "))
        update_document("sueno", id_input, {"hora":what_hour})
    elif selection == "4":
        print("Has seleccionado la opción 4.")
        id_input = input("¿Qué registro quieres eliminar? ")
        delete_document("sueno", id_input)

    elif selection == "5":
        print("Has decidido irte. Adiós.")
        loop = False
