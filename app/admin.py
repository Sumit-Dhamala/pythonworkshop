from django.contrib import admin
from . models import Question, Answer


class AnswerInline(admin.TabularInline):
    model = Answer
    max_num = 4
    min_num = 4


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    list_display = ['title', 'created_at']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
