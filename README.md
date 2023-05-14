<h1>FastAPI websocket chat room</h1>

Simple chat room for multiple users - build with FastAPI and websockets.
Multiple users can chat in one room (separate web browser instances).<br>

Case study of socket realtime connection usage.<br>

JQuery (for testing) on front side, will be replaced by Vue3 shortly.


## Installation

Install codebase:

```
$ git clone https://github.com/forDeFan/FastAPI_live_chat.git
$ cd FastAPI_live_chat
```

Recommended - create virtual environment and install dependencies

```
pip install -r requirements.txt
```

## To run the app

While in project root

```
$ uvicorn app.backend.main:app --reload
```

Docs available at<br>http://127.0.0.1:8000/docs


## Interaction

Go to: http://127.0.0.1:8000 <br>
Set up your nick (it will be placed into cookie) and chat with other users in same room.