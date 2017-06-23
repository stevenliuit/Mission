# -*- coding: utf-8 -*-

from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect, render_to_response
from apps.models import *
from common.utils.account import is_authenticated, get_admin_privileges


class AuthMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        view_name = view_func.__name__

        if view_name in ['login','web_hooks']:
            return None

        if not is_authenticated(request):
            return redirect('login')

        request.session['current_view_name'] = view_name

        if view_name in ['index', 'profile', 'logout','test']:
            return None

        self.add_operation_log(request, view_name)

        admin_id = request.session['current_admin_id']
        admin = Admin.objects.get(id=admin_id)
        if admin.role_id == Role.ROLE_SUPPER:
            return None

        current_privilege = Privilege.objects.filter(view_func=view_name)
        if not current_privilege:
            jump_view = 'index'
            message = u'对不起,您请求的操作权限还没有添加,请联系管理员!'
            return render_to_response('error.html', locals())

        privileges = get_admin_privileges(admin_id)
        if not privileges.filter(id=current_privilege[0].id):
            jump_view = 'index'
            message = u'对不起,您没有该操作权限!'
            return render_to_response('error.html', locals())

        return None

    def add_operation_log(self, request, view_name):
        import simplejson

        if view_name in ['operation_log_list', 'operation_log_show']:
            return None

        admin_id = request.session['current_admin_id']

        admin = Admin.objects.get(id=admin_id)
        try:
            privilege = Privilege.objects.get(view_func=view_name)
        except Privilege.DoesNotExist:
            return None
        oplog = OperationLog()
        oplog.admin_name = admin.name
        oplog.admin_id = admin_id
        oplog.request_method = request.method
        oplog.query_string = request.META.get('QUERY_STRING', '')
        oplog.privilege_id = privilege.id
        oplog.ip = request.META['REMOTE_ADDR']
        oplog.change_data = simplejson.dumps(request.POST)

        oplog.save()













