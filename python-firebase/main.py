import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate('./serviceAccountKey.json')
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()
l = {2: "dsf", 3: "fdsf"}
print(len(l.keys()))
while True:
  users_ref = db.collection(u'led-status')
  docs = users_ref.stream()

  for doc in docs:
    print(u'{} => {}'.format(doc.id, doc.to_dict()))
  