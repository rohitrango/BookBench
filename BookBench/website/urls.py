from django.conf.urls import url
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^login/$', login_view, name='login_view'),
    url(r'^home/$', home_page, name='home_page'),
    url(r'^logout/$', logout_view, name='logout_view'),

    url(r'^register/$', register_view, name='register'),
    url(r'^registeradmin/$', register_admin_view, name='register_admin_view'),
    
    url(r'^add_books/$', add_books, name='add_books'),
    url(r'^add_publications/$', add_publications, name='add_publications'),
    url(r'^add_authors/$', add_authors, name='add_authors'),
    url(r'^add_genres/$', add_genres, name='add_genres'),
    url(r'^add_moderators/$', add_moderators, name = 'add_moderators'),
    
    url(r'^prefgenres/$', preferred_genres, name='preferred_genres'),
    url(r'^search/', advanced_search, name='advanced_search'),
    url(r'^book/(?P<ISBN>[a-zA-Z0-9\-]+)$', book_details, name='book_details'),
    url(r'^message/$', messages, name = 'message'),
    
    # details of per genre/author/publication
    url(r'^genre/(?P<ID>[a-zA-z0-9\-]+)', genre_details, name='genre_details'),
    url(r'^author/(?P<ID>[a-zA-z0-9\-]+)', author_details, name='author_details'),
    url(r'^publication/(?P<ID>[a-zA-z0-9\-]+)', publication_details, name='publication_details'),
    url(r'^profile/(?P<ID>[a-zA-z0-9]+)', user_details, name='user_details'),

    # search user who have the books
    url(r'^userbook/(?P<ISBN>[a-zA-Z0-9\-]+)$', userbook, name='userbook'),

    # api calls
    url(r'^api/update_rating$', update_rating_api, name='update_rating_api'),
    url(r'^api/update_review$', update_review_api, name='update_review_api'),
    url(r'^api/update_location$', update_location_api, name='update_location_api'),
    url(r'^api/update_review_helpful$', update_review_helpful_api, name='update_review_helpful_api'),
    url(r'^api/mod_toggle$', mod_toggle_api, name='mod_toggle_api'),
    url(r'^api/add_report$', add_report_api, name = 'add_report_api'),
    url(r'^api/delete_review$', delete_review_api, name = 'delete_review_api'),
    url(r'^api/report_user_api', report_user_api, name='report_user_api'),
    url(r'^api/unban_banned_user$', unban_banned_user, name='unban_banned_user'),

    url(r'^api/add_message$', add_message_api, name='add_message_api'),

    url(r'^check_report/$', check_report_view, name = 'check_report'),
    url(r'^delete_report/$', delete_report_api, name = 'delete_report_api'),
    url(r'^banned_users/$', banned_users, name='banned_users'),

    url(r'^check_report_user/$', check_report_user_view, name = 'check_report_user'),
    url(r'^delete_user/$', delete_user_api, name = 'delete_user_api'),
    url(r'^delete_report_user/$', delete_report_user_api, name = 'delete_report_user_api'),

    url(r'^api/wishlist$', view_wishlist, name='wishlist_api'),
    url(r'^api/owned_books$', view_owned_books, name='owned_books_api'),
    
    url(r'^$', main_login_page, name='main_login_page'),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)