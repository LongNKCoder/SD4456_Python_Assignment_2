# SD4456_Python_Assignment_2
Assignment python django restful


Hi this is guide to use assignment
run `. start.sh` to setup with `python venv`
run `docker-compose up -d ` to setup with docker


## API endpoints:
| Method | Endpoint | Description |
| ------ | ------ | ----------- |
| `POST` | `/register` | Use to register. there are 3 parameters must have `username`, `password`, `email` |
| `POST`| `/login` | use to login. there are 2 parameters must have `username`, `password` it will return token to use  to call APIs. Don't forget it|
|`Token format`| `Token {token_value}` | it must send with header `Authorization` to call APIs|
| `GET`| `/posts/?user={id}` | use to get all post from other user that `Public`|
| `POST`| `/posts/` | use to post a post with user is an user that was authenticate with login token parameters need to |fill is `description` and `privacy`. `privacy` has 2 options is `Pub` and `Pri`
| `GET`| `/myposts` | use to get all post from user of that token|
| `GET`| `/dashboards` | use to get all post from user use token and user's friend with post privacy is `Pub`|
| `GET`| `/users` | use to get all username and their email|
| `GET`| `/friends/?user={id}` | use to get all friends of that user|
| `POST`| `/friends/` | use to make friends|
