# -*- coding: utf-8 -*-

from django.forms import ModelForm
from apps.models import *


class ModuleForm(ModelForm):
    class Meta:
        model = Module
        fields = ['module_name', 'list_order', 'status']


class ModuleAddForm(ModelForm):
    class Meta:
        model = Module
        fields = ['id', 'module_name', 'list_order', 'status']


class PrivilegeGroupForm(ModelForm):
    class Meta:
        model = PrivilegeGroup
        fields = ['group_name', 'module', 'status']


class MenuForm(ModelForm):
    class Meta:
        model = Menu
        fields = ['module', 'privilege', 'menu_name', 'target', 'target_url', 'status']


class PrivilegeForm(ModelForm):
    class Meta:
        model = Privilege
        fields = ['privilege_group', 'privilege_name', 'request_path', 'view_func', 'status']


class RoleForm(ModelForm):
    class Meta:
        model = Role
        fields = ['role_name', 'description', 'status']


class AdminForm(ModelForm):
    class Meta:
        model = Admin
        fields = ['name', 'user_name', 'email', 'tel', 'role', 'status']


class AdminEditForm(ModelForm):
    class Meta:
        model = Admin
        fields = ['user_name', 'role', 'email', 'tel', 'status']


class ProfileEditForm(ModelForm):
    class Meta:
        model = Admin
        fields = ['user_name', 'tel']

