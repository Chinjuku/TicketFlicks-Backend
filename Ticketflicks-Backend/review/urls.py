from django.urls import path
from review import api

urlpatterns = [
    path('review/<uuid:movieId>/', api.review),
    path('reply/<uuid:reviewId>/', api.reply),
    path('changereview/<uuid:reviewId>/', api.update_del_review),
    path('changereply/<uuid:replyId>/', api.update_del_reply),
]