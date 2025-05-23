from django.contrib import admin

from .models import Question, Choice


#class ChoiceInline(admin.StackedInline):
#    model = Choice
#    extra = 3


class ChoiceInline(admin.TabularInline):
        model = Choice
        extra = 3

#quarta versio
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter=["pub_date"]
    search_fields=["question_text"]
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]


#tercera versio
#class QuestionAdmin(admin.ModelAdmin):
#    fieldsets = [
#        (None, {"fields": ["question_text"]}),
#        ("Date information", {"fields": ["pub_date"]}),
#    ]


admin.site.register(Question, QuestionAdmin)

#segona versio
#class QuestionAdmin(admin.ModelAdmin):
#    fields = ["pub_date", "question_text"]
#admin.site.register(Question, QuestionAdmin)


#primera versio
#admin.site.register(Question)


#primera versio dels choices
#admin.site.register(Choice)