# from cms.plugin_base import CMSPluginBase
# from cms.plugin_pool import plugin_pool
# from cms.models.pluginmodel import CMSPlugin
# from django.utils.translation import ugettext_lazy as _
# from .models import Hello
# 
# @plugin_pool.register_plugin
# class HelloPlugin(CMSPluginBase):
#     model = Hello
#     name = _("Hello Plugin")
#     render_template = "hello_plugin.html"
#     cache = False
# 
#     def render(self, context, instance, placeholder):
#         context = super(HelloPlugin, self).render(context, instance, placeholder)
#         return context