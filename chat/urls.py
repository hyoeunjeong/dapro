from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("messages/new/", views.chat_message_new),
    #
    # /chat/puzzle/mario/
    # /chat/puzzle/toy/
    # /chat/puzzle/running/
    # puzzle/ 주소 에 문자열 패턴이 있고, 뒤에 / 가 있으면
    path("puzzle/<str:name>/", views.puzzle_room),  # ADDED
    path("puzzle/", views.puzzleroom_list),
    # FastAPI
    # @app.get("/chat/puzzle/{name}")
    # def room(name: str): pass
]
