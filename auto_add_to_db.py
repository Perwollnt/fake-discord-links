import markdown
import firebase_admin
from firebase_admin import firestore
import os
import json 
firebase_admin.initialize_app(json.loads(os.getenv('GOOGLE_APPLICATION_CREDENTIALS')))
f = open("./README.md")
gkjaséféa = markdown.markdown(f.read())
checkForLinks = False
links = []
text = gkjaséféa.split("<li>")
text.pop(0)
for t in text:
    t2 = t.split("</li>")[0]
    print(t2)
    if "http" in t2:
        links.append(t2)
print(links)
db = firestore.client()
db.collection("discord").document("fake-links").set({
    u'links' : links
})
