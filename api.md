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
      "name": "Jack"
    },
    {
      "id": 2,
      "username": "mt456",
      "name": "Matt",
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
    "username": <USERNAME>,
    "name": <NAME>,
  }
}
```

### Delete a specific user

`DELETE` `/api/users/{user_id}/`

Response

```yaml
{
  "success": true,
  "data": {
    "id": <ID>,
    "username": <USERNAME>,
    "name": <NAME>,
  }
}
```

---

### Send a friend request

`POST` `/api/friends/{user_id}/`

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
    "message": <USER INPUT>
  }
}
```

---

### Approve a friend request

`POST` `/api/friends/request/{user_id}/`

Request

```yaml
{
  "request_id": <REQUEST ID>,
  "accepted": true or false
}
```

Response

```yaml
{
   "success": true,
  "data": {
    "id": <ID>,
    "timestamp": <TIMESTAMP>
    "sender_id": <USER INPUT>,
    "receiver_id": <USER INPUT>, 
    "message": <USER INPUT>
  }
}
```
---

### Get all friend requests

`GET` `/api/friends/request/{user_id}/`


Response

```yaml
{
   "success": true,
  "data": [
  {
    "id": <ID>,
    "timestamp": <TIMESTAMP>
    "sender_id": <USER INPUT>,
    "receiver_id": <USER INPUT>, 
    "message": <USER INPUT>
  },
  {
    "id": <ID>,
    "timestamp": <TIMESTAMP>
    "sender_id": <USER INPUT>,
    "receiver_id": <USER INPUT>, 
    "message": <USER INPUT>
  }
  ]
}
```
---

### Get all friends

`GET` `/api/friends/{user_id}/`

Response

```yaml
{
  "success": true,
  "data": [
    {
      "id": 1,
      "username": "jf123",
      "name": "Jack"
    },
    {
      "id": 2,
      "username": "mt456",
      "name": "Matt",
    }
  ]
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

