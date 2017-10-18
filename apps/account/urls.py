from django.conf.urls import url

from apps.account import views as account_views

urlpatterns = [
    url(r'^module/list', account_views.module_list, name='module_list'),
    url(r'^module/add', account_views.module_add, name='module_add'),
    url(r'^module/edit', account_views.module_edit, name='module_edit'),
    url(r'^module/change_status', account_views.module_change_status, name='module_change_status'),

    url(r'^privilege_group/list', account_views.privilege_group_list, name='privilege_group_list'),
    url(r'^privilege_group/add', account_views.privilege_group_add, name='privilege_group_add'),
    url(r'^privilege_group/edit', account_views.privilege_group_edit, name='privilege_group_edit'),
    url(r'^privilege_group/change_status', account_views.privilege_group_change_status,name='privilege_group_change_status'),

    url(r'^menu/list', account_views.menu_list, name='menu_list'),
    url(r'^menu/add', account_views.menu_add, name='menu_add'),
    url(r'^menu/edit', account_views.menu_edit, name='menu_edit'),
    url(r'^menu/change_status', account_views.menu_change_status, name='menu_change_status'),

    url(r'^privilege/list', account_views.privilege_list, name='privilege_list'),
    url(r'^privilege/add', account_views.privilege_add, name='privilege_add'),
    url(r'^privilege/edit', account_views.privilege_edit, name='privilege_edit'),
    url(r'^privilege/change_status', account_views.privilege_change_status, name='privilege_change_status'),

    url(r'^operation_log/list', account_views.operation_log_list, name='operation_log_list'),
    url(r'^operation_log/show', account_views.operation_log_show, name='operation_log_show'),

    url(r'^admin/list', account_views.admin_list, name='admin_list'),
    url(r'^admin/add', account_views.admin_add, name='admin_add'),
    url(r'^admin/edit', account_views.admin_edit, name='admin_edit'),
    url(r'^admin/profile', account_views.admin_edit, name='admin_profile'),
    url(r'^admin/change_status', account_views.admin_change_status, name='admin_change_status'),

    url(r'^admin/list', account_views.admin_list, name='admin_list'),
    url(r'^admin/add', account_views.admin_add, name='admin_add'),
    url(r'^admin/edit', account_views.admin_edit, name='admin_edit'),
    url(r'^admin/profile', account_views.admin_edit, name='admin_profile'),
    url(r'^admin/change_status', account_views.admin_change_status, name='admin_change_status'),
    url(r'^admin/reset_pwd', account_views.admin_reset_pwd, name='admin_reset_pwd'),

    url(r'^role/list', account_views.role_list, name='role_list'),
    url(r'^role/add', account_views.role_add, name='role_add'),
    url(r'^role/edit', account_views.role_edit, name='role_edit'),
    url(r'^role/profile', account_views.role_edit, name='role_profile'),
    url(r'^role/change_status', account_views.role_change_status, name='role_change_status'),
]
