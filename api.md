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
    "friends": [<SERIALIZED USER>, ... ],
    "groups": [<SERIALIZED GROUP>, ... ]
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

`POST` `/api/users/{user_id}/friends/requests/`

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
    "sender_id": <USER INPUT>,
    "receiver_id": <USER INPUT>, 
    "timestamp": <NOW>,
    "message": <USER INPUT>
  }
}
```

---

### Approve a friend request

`PUT` `/api/users/{user_id}/friends/requests/`

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

`GET` `/api/users/{user_id}/friends/requests/`


Response

```yaml
{
   "success": true,
  "data": [
  {
    "id": <ID>,
    "sender_id": <USER INPUT>,
    "receiver_id": <USER INPUT>, 
    "timestamp": <TIMESTAMP>,
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

`GET` `/api/users/{user_id}/friends/`

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

### Remove a friend

`PUT` `/api/users/{user_id}/friends/`

Request

```yaml
{
  "friend_id": <ID>
}
```

Response

```yaml
{
  "success": true,
  "data": {
    "id": <ID>,
    "username": <USERNAME>,
    "name": <NAME>
  }
}
```

### Create a group

`POST` `/api/groups/`

Request

```yaml
{
  "creator_id": <ID>,
  "name": <NAME (OPTIONAL)>,
  "other_user_ids": [ <ID>, ... ]
}
```

Response

```yaml
{
  "success": true,
  "data": {
    "id": <ID>,
    "name": <NAME>,
    "members": [<SERIALIZED USER (NO FRIENDS, GROUPS)>, ... ],
    "messages": [<SERIALIZED MESSAGE>, ... ]
  }
}
```

---

### Get a specific group

`GET` `/api/groups/{group_id}/`

Response

```yaml
{
  "success": true,
  "data": {
    "id": <ID>,
    "name": <NAME>,
    "members": [<SERIALIZED USER (NO FRIENDS, GROUPS)>, ... ],
    "messages": [<SERIALIZED MESSAGE>, ... ]
  }
}
```

### Delete a specific group

`DELETE` `/api/groups/{group_id}/`

Response

```yaml
{
  "success": true,
  "data": {
    "id": <ID>,
    "name": <NAME>,
    "members": [<SERIALIZED USER (NO FRIENDS, GROUPS)>, ... ],
    "messages": [<SERIALIZED MESSAGE>, ... ]
  }
}
```

--- 

### Add a user to a group

`PUT` `/api/groups/members/`

Request

```yaml
{
  "group_id": <ID>,
  "user_id": <ID>
}
```

Response

```yaml
{
  "success": true,
  "data": {
    "id": <ID>,
    "name": <NAME>,
    "members": [<SERIALIZED USER (NO FRIENDS, GROUPS)>, ... ],
    "messages": [<SERIALIZED MESSAGE>, ... ]
  }
}
```

--- 

### Remove a user from a group

`PUT` `/api/groups/members/remove/`

Request

```yaml
{
  "group_id": <ID>,
  "user_id": <ID>
}
```

Response

```yaml
{
  "success": true,
  "data": {
    "id": <ID>,
    "name": <NAME>,
    "members": [<SERIALIZED USER (NO FRIENDS, GROUPS)>, ... ],
    "messages": [<SERIALIZED MESSAGE>, ... ]
  }
}
```

--- 

### Send a message to a group

`POST` `/api/users/{user_id}/messages/group/`

Request

```yaml
{
  "group_id": <ID>,
  "message": <MESSAGE>
}
```

Response

```yaml
{
  "success": true
  "data": {
    "id": <ID>,
    "sender_id": <ID>,
    "group_id": <ID>,
    "timestamp": <TIMESTAMP>,
    "message": <MESSAGE>
  }
}
```

---

### Send a message to a user

`POST` `/api/users/{user_id}/messages/`

Request

```yaml
{
  "receiver_id": <ID>,
  "message": <MESSAGE>
}
```

Response

```yaml
{
  "success": true
  "data": {
    "id": <ID>,
    "sender_id": <ID>,
    "group_id": <ID>,
    "timestamp": <TIMESTAMP>,
    "message": <MESSAGE>
  }
}
```

---