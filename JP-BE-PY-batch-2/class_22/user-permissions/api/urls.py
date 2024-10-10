from django.urls import path
from .views_user import login_view, logout_view
from .views_book_1_override_global_permission import create_book as create_book_1, get_all_books as get_all_books_1, delete_book as delete_book_1
from .views_book_2_model_based import create_book as create_book_2, get_all_books as get_all_books_2, delete_book as delete_book_2
from .views_book_3_object_based import create_book as create_book_3, get_all_books as get_all_books_3, delete_book as delete_book_3

urlpatterns = [
    path("users/login", login_view),
    path("users/logout", logout_view),

    path("books_1/all", get_all_books_1),
    path("books_1/create", create_book_1),
    path("books_1/delete/<int:id>", delete_book_1),

    path("books_2/all", get_all_books_2),
    path("books_2/create", create_book_2),
    path("books_2/delete/<int:id>", delete_book_2),

    path("books_3/all", get_all_books_3),
    path("books_3/create", create_book_3),
    path("books_3/delete/<int:id>", delete_book_3),
]