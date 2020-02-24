import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate('./serviceAccountKey.json')
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()
def on_snapshot(doc_snapshot, changes, read_time):
  for doc in doc_snapshot:
      print(u'Received document snapshot: {}'.format(doc.id))

# Watch the document
# doc_ref = db.collection(u'led-status').document(u'status')
# doc_watch = doc_ref.on_snapshot(on_snapshot)
# print(doc_watch)

while True:
  users_ref = db.collection(u'led-status')
  docs = users_ref.stream()

  for doc in docs:
    print(u'{} => {}'.format(doc.id, doc.to_dict()))