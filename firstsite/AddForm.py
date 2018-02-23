from django import forms
 
# 5颗星Form学习资料:https://simpleisbetterthancomplex.com/article/2017/08/19/how-to-render-django-form-manually.html

# https://docs.djangoproject.com/en/2.0/topics/forms/modelforms/

# Widget 负责渲染
# Form 提供元信息
# Model数据库中的元信息
# ModelForm 可以将Model转成Form，这样就不用手写Form了
# https://docs.djangoproject.com/en/2.0/topics/forms/modelforms/
class AddForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()