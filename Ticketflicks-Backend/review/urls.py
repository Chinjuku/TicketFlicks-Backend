from django.urls import path
from review import api

urlpatterns = [
    path('allreview/<uuid:movieId>/', api.all_review_movie),
    path('review/<uuid:reviewId>/', api.review),
    path('review/', api.post_review),
    path('reply/', api.reply),
    path('reply/<uuid:replyId>/', api.get_reply_by_id),
    path('changereview/<uuid:reviewId>/', api.update_del_review),
    path('changereply/<uuid:replyId>/', api.update_del_reply),
    path('countreview/', api.count_review),
    path('countreview/<uuid:movieId>/', api.count_review_id),
    path('countreply/', api.count_reply_id),
]