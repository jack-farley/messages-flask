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
      "friend requests": [ <SERIALIZED REQUESTS>, ... ],
      "messages sent": [ <SERIALIZED MESSAGE>, ... ],
      "messages received": [ <SERIALIZED MESSAGE>, ... ]
    },
    {
      "id": 2,
      "username": "mt456",
      "name": "Matt",
      "friends": [ <SERIALIZED USER WITHOUT FRIENDS FIELD>, ... ],
      "friend requests": [ <SERIALIZED REQUESTS>, ... ],
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
    "friend requests": [],
    "messages sent": [],
    "messages received": []
  }
}
```

---

### Delete a specific user

`DELETE` `/api/users/{user_id}/`

Response

```yaml
{
  "success": true,
  "data": {
    "id": <ID>,
    "username": <USER INPUT FOR USERNAME>,
    "name": <USER INPUT FOR NAME>,
    "friends": [ <SERIALIZED USER WITHOUT FRIENDS FIELD>, ... ],
    "friend requests": [ <SERIALIZED REQUESTS>, ... ],
    "messages sent": [ <SERIALIZED MESSAGE>, ... ],
    "messages received": [ <SERIALIZED MESSAGE>, ... ]
  }
}
```

---

### Get a specific user

`GET` `/api/users/{user_id}/`

Response

```yaml
{
  "success": true,
  "data": {
    "id": <ID>,
    "username": <USER INPUT FOR USERNAME>,
    "name": <USER INPUT FOR NAME>,
    "friends": [ <SERIALIZED USER WITHOUT FRIENDS FIELD>, ... ],
    "friend requests": [ <SERIALIZED REQUESTS>, ... ],
    "messages sent": [ <SERIALIZED MESSAGE>, ... ],
    "messages received": [ <SERIALIZED MESSAGE>, ... ]
  }
}
```

---

### Send a friend request

`POST` `/api/request/{user_id}/`

Request

```yaml
{
  "receiver_id": <USER INPUT>, 
  "message": <USER INPUT>
}
```

Response

```yaml
{
  "success": true,
  "data": {
    "id": <ID>,
    "timestamp": <NOW>,
    "sender_id": <USER INPUT>,
    "receiver_id": <USER INPUT>, 
    "message": <USER INPUT>,
    "accepted": false
  }
}
```

---

### Approve a friend request

`POST` `/api/request/{user_id}/{request_id}/`

Request

```yaml
{
  "accepted": true or false
}
```

Response

```yaml
{
   "success": true,
  "data": {
    "id": <ID>,
    "timestamp": <NOW>,  // update timestamp
    "sender_id": <USER INPUT>,
    "receiver_id": <USER INPUT>, 
    "message": <USER INPUT>,
    "accepted": <USER INPUT FOR ACCEPTED>
  }
}
```

---

### Send a message

`POST` `/api/messages/{user_id}/`

Request

```yaml
{
  "receiver_id": <USER INPUT>,
  "message": <USER INPUT>
}
```

```yaml
{
  "success": true,
  "data": {
    "id": <ID>,
    "timestamp": <NOW>,
    "sender_id": <USER INPUT>,
    "receiver_id": <USER INPUT>,
    "message": <USER INPUT>,
    "read": false
  }
}
```

---

### Get all messages for a specific user

`GET` `/api/messages/{user_id}/`

Response

```yaml
{
  "success": true,
  "data": [ <SERIALIZED MESSAGE>, ...]
}
```

---

### Mark a specific message as read

`POST` `/api/messages/{user_id}/{message_id}/`

Response

```yaml
{
  "success": true,
  "data": {
    "id": <ID>,
    "timestamp": <NOW>,
    "sender_id": <USER INPUT>,
    "receiver_id": <USER INPUT>,
    "message": <USER INPUT>,
    "read": true
  }
}
```

