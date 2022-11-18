# SkillFactory QAP-92 задание 19.3.3

# Имя пользователя для логина
username = 'kate'

# Пароль пользователя для логина
password = 'qwerty'

# Данные для создания нового юзера
created_user = {
  "id": 0,
  "username": "katee",
  "firstName": "Katte",
  "lastName": "Ivannova",
  "email": "kate@ivannova.org",
  "password": "qwerty123456",
  "phone": "+12345678901",
  "userStatus": 0
}

# Данные для обновления юзера
updated_user = {
  "id": 0,
  "username": "katee2",
  "firstName": "Katte2",
  "lastName": "Ivannova2",
  "email": "kate2@ivannova2.org",
  "password": "asdfgh234567",
  "phone": "+12345678902",
  "userStatus": 0
}

# Данные для создания пользователей списком
list_of_users = [
  {
    "id": 0,
    "username": "semen",
    "firstName": "Semen",
    "lastName": "Semenov",
    "email": "semen@semenov.org",
    "password": "qwe123",
    "phone": "+12345678903",
    "userStatus": 0
  },
  {
    "id": 0,
    "username": "semen2",
    "firstName": "Semen2",
    "lastName": "Semenov2",
    "email": "semen2@semenov2.org",
    "password": "rty456",
    "phone": "+12345678904",
    "userStatus": 0
  }
]

# Данные для создания ордера
order = {
  "id": 0,
  "petId": 0,
  "quantity": 0,
  "shipDate": "0",
  "status": "placed",
  "complete": True
}

# Данные для добавления нового питомца
new_pet = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "Category"
  },
  "name": "Name",
  "photoUrls": [
    "None"
  ],
  "tags": [
    {
      "id": 0,
      "name": "Tags"
    }
  ],
  "status": "available"
}