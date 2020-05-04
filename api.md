# Messages API
##### Contributors: Jack Farley

---

### Get all users

`GET` `/api/users/`

Response

```yaml
{
  "success": true,
  "data": [
    {
      "id": 1,
      "username": "jf123",
      "name": "Jack",
      "friends": [ <SERIALIZED USER WITHOUT FRIENDS FIELD>, ... ],
      "messages sent": [ <SERIALIZED MESSAGE>, ... ],
      "messages received": [ <SERIALIZED MESSAGE>, ... ]
    },
    {
      "id": 2,
      "username": "mt456",
      "name": "Matt",
      "friends": [ <SERIALIZED USER WITHOUT FRIENDS FIELD>, ... ],
      "messages sent": [ <SERIALIZED MESSAGE>, ... ],
      "messages received": [ <SERIALIZED MESSAGE>, ... ]
    }
  ]
}
```
---

### Create a user

`POST` `/api/users/`

Request

```yaml
{
  "username": <USER INPUT>,
  "name": <USER INPUT>
}
```

Response

```yaml
{
  "success": true,
  "data": {
    "id": <ID>,
    "username": <USER INPUT FOR USERNAME>,
    "name": <USER INPUT FOR NAME>,
    "friends": [],
    "messages sent": [],
    "messages received": []
  }
}
```

---

### Delete a specific user

`DELETE` `/api/users/{id}/`

Response

```yaml
{
  "success": true,
  "data": {
    "id": <ID>,
    "username": <USER INPUT FOR USERNAME>,
    "name": <USER INPUT FOR NAME>,
    "friends": [ <SERIALIZED USER WITHOUT FRIENDS FIELD>, ... ],
    "messages sent": [ <SERIALIZED MESSAGE>, ... ],
    "messages received": [ <SERIALIZED MESSAGE>, ... ]
  }
}
```

---

### Get a specific user

`GET` `/api/users/{id}/`

Response

```yaml
{
  "success": true,
  "data": {
    "id": <ID>,
    "username": <USER INPUT FOR USERNAME>,
    "name": <USER INPUT FOR NAME>,
    "friends": [ <SERIALIZED USER WITHOUT FRIENDS FIELD>, ... ],
    "messages sent": [ <SERIALIZED MESSAGE>, ... ],
    "messages received": [ <SERIALIZED MESSAGE>, ... ]
  }
}
```

---

### Send a friend request

`POST` `/api/request/`

Request

```yaml
{
  "sender_id": <USER INPUT>,
  "receiver_id": <USER INPUT>, 
  "message": <USER INPUT>
}
```

Response

```yaml
{
  "success": true,
  "data": {
    "sender_id": <USER INPUT>,
    "receiver_id": <USER INPUT>, 
    "message": <USER INPUT>
  }
}
```

---

### View pending friend requests

---

### Approve a friend request

---

### Send a message

---

### Get all sent messages

---

### Get all incoming messages

---

### Get unread messages

---

### Get a specific message

---

### Mark a specific message as read

