# -*- coding: utf-8 -*-
from apps.models import *


def get_current_role_id(request):
    try:
        current_role_id = request.session['current_role_id']
    except:
        current_role_id = 0

    return current_role_id


def get_current_admin_id(request):
    try:
        current_admin_id = request.session['current_admin_id']
    except:
        current_admin_id = 0

    return current_admin_id


def get_current_admin(request):
    try:
        admin = Admin.objects.get(id=get_current_admin_id(request))
    except:
        admin = None

    return admin


def get_current_role(request):
    try:
        role = Role.objects.get(id=get_current_role_id(request))
    except:
        role = None

    return role


def get_current_privileges(request):
    try:
        current_admin = get_current_admin(request)
        if current_admin.role_id == Role.ROLE_SUPPER:
            privileges = Privilege.objects.all()
        else:
            privileges = current_admin.role.privileges.all()
    except:
        return []

    return privileges

