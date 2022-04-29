<!-- Login API -->

http://127.0.0.1:8000/auth/login/

        Method: POST
        {
            "username":
            "password":
        }

<!-- Forget password reset API -->

http://127.0.0.1:8000/auth/password-reset-complete

Pacth request for change password

{
"password": "",
"token": "",
"uidb64": ""
}

<!-- Update profile -->

http://127.0.0.1:8000/auth/update

Authentication are required

{
"username": "",
"usertype": "",
"password": ""
}

<!-- logout API -->
 
http://127.0.0.1:8000/auth/logout

{
"detail": "Authentication credentials must provided."
}

# property

<!-- get all state -->

http://127.0.0.1:8000/property/state

GET Request for all state

{
"id": 1,
"name": "Karnataka"
},


<!-- get all city -->

http://127.0.0.1:8000/property/city

GET Request for all city

{
"id": 1,
"name": "Chikballapur"
},

<!-- path("data/<str:name>", GetDataView.as_view(), name="property"), -->

<!-- get data using the category(school,collage,land,hospital) -->

http://127.0.0.1:8000/property/data/school

Get request for get all category data

    {
        "id": 3,
        "name": "BGS Nursery School",
        "image": "/media/images/hqdefault_Gc7xwbQ.jpg",
        "address": "Chikkaballapur, Karnataka 562101",
        "category": 6,
        "state": 1,
        "city": 1
    },

<!-- contact us  -->

http://127.0.0.1:8000/property/contactus/

GET & POST

    {
        "id": 1,
        "username": "harsha gowda",
        "email": "harshag1996@gmail.com",
        "phone": "8880973864",
        "message": "Hi,Can you tell me what courses are available."
    }
