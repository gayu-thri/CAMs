import pyrebase

config = {
    "apiKey" : "AIzaSyAIsSHOuNkfoGuUrJ5xQM2t6jNVT5TlHx8",
    "authDomain" : "cams-da440.firebaseapp.com",
    "databaseURL" : "https://cams-da440.firebaseio.com",
    "projectId" : "cams-da440",
    "storageBucket" : "cams-da440.appspot.com",
    "messagingSenderId" : "592415369968"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()
global active,credentials
#Firebase
from firebase import firebase
firebase = firebase.FirebaseApplication('https://cams-da440.firebaseio.com/', None)
db = firebase.get('/', None)
print(db)
#db.child("credentials").child("CAMS0000").push({"EmailId":"admin@gmail.com" , "Password": "admin@123"})
# userId = "CAMS"
# for i in range(2,5):
#     if i <= 9:
#         k = "000" +str(i)
#     elif i >= 10 and i <= 99:
#         k = "00" +str(i)
#     elif i >=100 and  i <= 999:
#         k = "0" + str(i)
#     uname = input()
#     pwd = input()
#     db.child("credentials").child(userId + k).set({"EmailId":uname , "Password": pwd})
#db.child("seats").push(({"branch":"elec sci","no_of_seats":"45"}))

ch = 'N'
while ch == 'Y':
    branch = input()
    c1 = int(input())
    c2 = int(input())
    c3 = int(input())
    db.child("Cutoff").child(branch).set({"Current": c1, "Previous": c2, "TwoYearsPrev": c3})
    ch = input()

# db.child("Cutoff").child("branch").remove()
#db.child("Cutoff").child("branch").update({'b': 1})

