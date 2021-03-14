from django.urls import path
from . import views

urlpatterns = [
    path('carrot/', views.board_list),
    path('carrot/<int:sell_id>', views.sell_detail),
    path('carrot/<int:sell_id>', views.sell_create),
    path('carrot/<int:sell_id>', views.sell_update_and_delete),
    path('carrot/<int:sell_id>/comment/', views.comment_list),
    path('carrot/<int:sell_id>/comment/<int:comment_id>', views.comment_create),
    path('carrot/<int:sell_id>/comment/<int:comment_id>', views.comment_update_and_delete),
]