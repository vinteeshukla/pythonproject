from django.urls import path
from . import views



urlpatterns = [
    path('next/home.html',views.homepage, name="homepage"),
    path('flow/',views.flowChart, name="flowchartpage"),
    path('next/',views.viewname, name = "database"),
    path('scrap/',views.beautifulSoup, name = "beautifulSoup"),
    path('newhome/',views.newhomepage,name='newhomepage'),
    path('json/',views.json,name='json'),
    path('newpost/',views.PII,name='pii'),
    path('next/newpostx/',views.post_new,name='post_new'),
    path('newjoindetails/',views.New_join_detail,name='new_join_detail'),
    path('newjoinjson/',views.json_New_join,name='newjoinjson'),
    path('next/Gambit1_delete/',views.gambit_container_delete,name='Gambit1_delete'),
    path('next/Gambit_container_add/',views.gambit_container_add,name='Gambit_container_add'),
    path('next/retain_nodes/',views.retain_nodes,name='retain_nodes'),
    path('next/update_nodes/',views.update_nodes,name='update_nodes'),

    path('update/<str:name>', views.update, name='update'),
    path('next/update/updaterecord/<str:detail_id>', views.updaterecord, name='update'),
    path('next/mainPage_request/', views.main_chatbot_page, name='update'),
    path('Json_scratch/', views.Json_scratch, name='new_json_scratch'),
    path('newx/', views.viewhome, name='scratch_home'),
    path('new_chatbot_entry/', views.new_chatbot_gambit, name='scratch_home'),
    path('next/new_gambit_connection/', views.New_Gambit_container_value, name='new_gambit_connection'),
    path('next/delete1/', views.delete1, name='delete'),
    path('next/update1/', views.update1, name='update'),
    path('next/updaterecord1/', views.updaterecord1, name='update'),
    path('next/write_file/', views.writetofile, name='write_file/'),
    path('next/read_file/', views.readfile, name='read_file/'),
    path('next/json_format/', views.json_format, name='json_format'),
    path('next/json_update/', views.json_update_view, name='json_update'),
    path('next/json_delete/', views.json_delete, name='json_delete'),
    path('next/new_chat_detail/', views.New_chat_detail, name='new_chat_detail'),
    path('next/form_values/', views.form_data, name='form_values'),
    path('next/node_delete/', views.chatbotname_del, name='node_delete'),
 
    
]