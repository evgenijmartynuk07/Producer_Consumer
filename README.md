# Producer_Consumer

1. Celery generates tasks for a random user in the database once a minute.
2. When the user visits the page, they can see tasks that they need to delete.
3. After deleting a task, the Telegram bot sends a message to the chat about the successful completion of the task.

## Installation

Python3 must be already installed

The project needs to be launched directly in Docker, and all configurations will be automatically generated.

```shell
git clone https://github.com/evgenijmartynuk07/Producer_Consumer.git
cd Producer_Consumer
create .env based on .env.sample

docker build -t backend .
docker-compose up
```
You can use next users:
```shell
username: user1
password: user1
```
```shell
username: user2
password: user2
```
```shell
username: user3
password: user3
```