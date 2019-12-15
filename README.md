# generate_game

### Пользователь
```
GET /api/v1/user - получение списка пользователей
GET /api/v1/user/<int:id_user> - получение профиля пользователя

POST /api/v1/user/login - авторизация пользователя
{
  'login': text,
  'password': text
}

POST /api/v1/user/register - регистрация пользователя
{
  'login': text
  'password': text
  'email': text
  'name': text
}
```

### Игра

```
GET /api/v1/game - Список игр
POST /api/v1/game - создание игры
GET /api/v1/game/<int:id_game> - Информация о игре
PUT /api/v1/game/<int:id_game> - Изменение данных о игре
PUT /api/v1/game/<int:id_game>/register/ - Регистрация на игру
GET /api/v1/game/<int:id_game>/rating/ - Рейтинг игры
GET /api/v1/game/<int:id_game>/question/ - Получить вопрос
POST /api/v1/game/<int:id_game>/question/ - Ответить на вопрос
```