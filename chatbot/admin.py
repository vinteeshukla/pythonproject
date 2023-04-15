from django.contrib import admin

from chatbot.views import New_join_detail
from .models import DetailForm,MyModel,user,syllabus,text,Scratch_values,Gambit_container,New_chatbot_values,New_Gambit_container

admin.site.register(DetailForm)
admin.site.register(user)
admin.site.register(syllabus)
admin.site.register(text)
admin.site.register(Scratch_values)
admin.site.register(Gambit_container)
admin.site.register(New_chatbot_values)
admin.site.register(New_Gambit_container)
admin.site.register(MyModel)






