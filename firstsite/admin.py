from django.contrib import admin
# Register your models here.

from django.contrib import admin
from .models import HeaderLink
from .models import Post
from .forms import PostModelForm
from .visibleblogfilter import *
from django.db.models import Q
from django.utils.html import format_html
from django.core.urlresolvers import reverse
from django.conf.urls import include, url
from django import forms
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from . import views
import mysite

class InputFilter(admin.SimpleListFilter):
    
    template = 'admin/input_filter.html'

    def lookups(self, request, model_admin):
        # Dummy, required to show the filter.
        return ((),)

    def choices(self, changelist):
        # Grab only the "all" option.
        all_choice = next(super().choices(changelist))
        all_choice['query_parts'] = (
            (k, v)
            for k, v in changelist.get_filters_params().items()
            if k != self.parameter_name
        )
        yield all_choice

class PostContentFilter(InputFilter):
    parameter_name = 'content'
    title = 'content'
    def queryset(self, request, queryset):
        if self.value() is not None:
            queryvalue = self.value()
            return queryset.filter(
                Q(content__contains = queryvalue)
            )

class PostTitleFilter(InputFilter):
    parameter_name = 'title'
    title = 'title'

    def queryset(self, request, queryset):
        if self.value() is not None:
            queryvalue = self.value()
            return queryset.filter(
                Q(title__contains = queryvalue)
            )


def posttitle_upper(modeladmin, request, queryset):
    for post in queryset:
        post.title = post.title.upper()
        post.save()
posttitle_upper.short_description = "title uppercase "


def posttitle_lower(modeladmin, request, queryset):
    for post in queryset:
        post.title = post.title.lower()
        post.save()
posttitle_lower.short_description = "title lowercase "



class AccountActionForm(forms.Form):
    comment = forms.CharField(
        required=False,
        widget=forms.Textarea,
    )
    send_email = forms.BooleanField(
        required=False,
    )
    @property
    def email_subject_template(self):
        return 'email/account/notification_subject.txt'
    @property
    def email_body_template(self):
        raise NotImplementedError()
    
    def form_action(self, account, user):
        raise NotImplementedError()
    
    def save(self, account, user):
        
        account, action = self.form_action(account, user)
        
        if self.cleaned_data.get('send_email', False):
            pass
        return account, action


class WithdrawForm(AccountActionForm):
    amount = forms.IntegerField(
        min_value=1,
        max_value=10000,
        required=True,
        help_text='How much to withdraw?',
    )
    email_body_template = 'email/account/withdraw.txt'
    field_order = (
        'amount',
        'comment',
        'send_email',
    )
    
    def form_action(self, account, user):
        
        print("do form_action....")
#         return Account.withdraw(
#             id=account.pk,
#             user=account.user,
#             amount=self.cleaned_data['amount'],
#             withdrawn_by=user,
#             comment=self.cleaned_data['comment'],
#             asof=timezone.now(),
#         )

class PostAdmin(admin.ModelAdmin):
    list_display = ("title" ,"meta_description","content","show","account_actions")
    search_fields = ['title', 'meta_description',"content"]
    
#     list_filter = ("title","created_on")
    list_filter = (PostContentFilter,PostTitleFilter, )
    
    
    actions = [posttitle_upper, posttitle_lower]
    
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            url(
                r'^(?P<account_id>.+)/withdraw/$',
                self.admin_site.admin_view(self.process_withdraw),
                name='account-withdraw',
            ),
        ]
        return custom_urls + urls
    
    def account_actions(self, obj):
        
        return format_html(
            '<a class="button" href="{}">Withdraw</a>',
            reverse('admin:account-withdraw', args=[obj.pk]),
        )
    account_actions.short_description = 'Account Actions'
    account_actions.allow_tags = True
    
    
    def process_withdraw(self, request, account_id, *args, **kwargs):
        return self.process_action(
            request=request,
            account_id=account_id,
            action_form=WithdrawForm,
            action_title='Withdraw',
            )
#     form = PostModelForm

    def process_action(self,request,account_id,action_form,action_title):

        account = self.get_object(request, account_id)
        if request.method != 'POST':
            form = action_form()
        else:
            form = action_form(request.POST)
            if form.is_valid():
#                 form.save(account, request.user)
                url = reverse(
                    'post',
                    )
                return HttpResponseRedirect(url)
#                 url = views.post
            else:
                self.message_user(request, 'Success')
                url = reverse(
                    'admin:account_account_change',
                   args=[account.pk],
                    current_app=self.admin_site.name,
                )
                return HttpResponseRedirect(url)
        context = self.admin_site.each_context(request)
        context['opts'] = self.model._meta
        context['form'] = form
        context['account'] = account
        context['title'] = action_title
        return TemplateResponse(
            request,
            'admin/account_action.html',
            context,
        )



class HeaderLinkAdmin(admin.ModelAdmin):
#     Post.meta_description
#     HeaderLink._meta
    flist = [x.name for x in HeaderLink._meta.get_fields()]
    flist.remove("content")
    list_display = tuple(flist)
#     list_display = [HeaderLink._meta.get_all_field_names()]
#     list_display = ("id" ,"name","url","titletext","detailtext")

admin.site.register(HeaderLink, HeaderLinkAdmin)
# admin.site.register(Post)
admin.site.register(Post, PostAdmin)





