# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect

from apps.account.forms import *

from common.utils.paginator import pages
from common.utils.date import date, timestamp
from common.utils.sessions import *
from common.utils.crypt import md5, gen_rand_password

import simplejson as json


# 模块管理(module).
def module_list(request):
    query_string = request.META.get('QUERY_STRING', '')
    module_name = request.GET.get('module_name', '').strip()

    objects = Module.objects.all().order_by('-id')
    if module_name:
        objects = Module.objects.filter(module_name__contains=module_name).order_by('-id')

    page_objects = pages(objects, request)

    return render_to_response('account/module_list.html', locals())


def module_add(request):
    """
    添加模块 VIEW
    """
    if request.method == 'POST':
        form = ModuleAddForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['module_name']
            if Module.objects.filter(module_name=name):
                emg = u'添加失败, 此模块 %s 已存在!' % name
            else:
                form.save()
                return redirect('module_list')
        else:
            emg = u'模块: 添加失败'

    latest_object = Module.objects.latest('id')
    if latest_object:
        latest_id = latest_object.id + 100
    else:
        latest_id = 100

    return render_to_response('account/module_add.html', locals(), request)


def module_edit(request):
    """
    编辑模块 VIEW
    """
    pk_id = request.GET.get('id', '')

    module = Module.objects.get(id=pk_id)
    if request.method == 'POST':
        form = ModuleForm(request.POST, instance=module)
        if form.is_valid():
            name = form.cleaned_data['module_name']
            val_module = Module.objects.filter(module_name=name).exclude(id=pk_id)
            if val_module:
                emg = u'添加失败, 此模块 %s 已存在!' % name
            else:
                form.save()
                return redirect('module_list')
        else:
            emg = u'模块: 添加失败'

    return render_to_response('account/module_edit.html', locals(), request)


def module_change_status(request):
    """
    状态变更 VIEW
    """
    jump_view = 'module_list'
    query_string = request.META.get('QUERY_STRING', '')
    pk_id = request.GET.get('id', '')

    try:
        module = Module.objects.get(id=pk_id)
    except:
        module = None

    if not module:
        message = '更新失败,不存在该模块ID'
        return render_to_response('error.html', locals())

    module.status = Module.STATUS_CLOSE if module.status == Module.STATUS_OPEN else Module.STATUS_OPEN
    module.save()

    message = '状态更新成功'

    return render_to_response('success.html', locals())


# 权限组管理(privilege_group).
def privilege_group_list(request):
    query_string = request.META.get('QUERY_STRING', '')
    group_name = request.GET.get('group_name', '').strip()

    objects = PrivilegeGroup.objects.all().order_by('-id')
    if group_name:
        objects = PrivilegeGroup.objects.filter(group_name__contains=group_name)

    objects.order_by('-id')

    page_objects = pages(objects, request)

    return render_to_response('account/privilege_group_list.html', locals())


def privilege_group_add(request):
    """
    添加权限组 VIEW
    """
    if request.method == 'POST':
        form = PrivilegeGroupForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['group_name']
            module_id = request.POST.get('module')
            if PrivilegeGroup.objects.filter(group_name=name):
                emg = u'添加失败, 此权限组 %s 已存在!' % name
            else:
                privilege_group = form.save(commit=False)

                try:
                    latest_object = PrivilegeGroup.objects.filter(module_id=module_id).latest('id')
                    privilege_group.id = latest_object.id + 1
                except:
                    privilege_group.id = int(module_id) * 10 + 1

                privilege_group.save()
                form.save_m2m()

                return redirect('privilege_group_list')
        else:
            emg = u'模块: 添加失败'

    modules = Module.objects.all()


    return render_to_response('account/privilege_group_add.html', locals())


def privilege_group_edit(request):
    """
    编辑模块 VIEW
    """
    pk_id = request.GET.get('id', '')

    privilege_group = PrivilegeGroup.objects.get(id=pk_id)
    if request.method == 'POST':
        form = PrivilegeGroupForm(request.POST, instance=privilege_group)
        if form.is_valid():
            name = form.cleaned_data['group_name']
            val_module = PrivilegeGroup.objects.filter(group_name=name).exclude(id=pk_id)
            if val_module:
                emg = u'添加失败, 此权限组 %s 已存在!' % name
            else:
                form.save()
                return redirect('privilege_group_list')
        else:
            emg = u'权限组: 添加失败'

    modules = Module.objects.all()
    return render_to_response('account/privilege_group_edit.html', locals(), request)


def privilege_group_change_status(request):
    """
    状态变更 VIEW
    """
    jump_view = 'privilege_group_list'
    pk_id = request.GET.get('id', '')

    try:
        privilege_group = PrivilegeGroup.objects.get(id=pk_id)
    except:
        privilege_group = None

    if not privilege_group:
        message = '更新失败,不存在该权限组ID'
        return render_to_response('error.html', locals())

    privilege_group.status = PrivilegeGroup.STATUS_CLOSE if privilege_group.status == PrivilegeGroup.STATUS_OPEN else \
        PrivilegeGroup.STATUS_OPEN
    privilege_group.save()

    message = '状态更新成功'

    return render_to_response('success.html', locals())


# 权限组管理(menu).
def menu_list(request):
    query_string = request.META.get('QUERY_STRING', '')
    menu_name = request.GET.get('menu_name', '').strip()

    objects = Menu.objects.all().order_by('-id')
    if menu_name:
        objects = Menu.objects.filter(menu_name__contains=menu_name)

    objects.order_by('-id')

    page_objects = pages(objects, request)

    return render_to_response('account/menu_list.html', locals())


def get_ajax_privileges(request):
    module_id = request.GET.get('mid', '')

    objects = Privilege.objects.filter(privilege_group__module__id=module_id)

    data = {}
    for privilege in objects:
        data[privilege.id] = privilege.privilege_name

    return json.dumps(data)


def menu_add(request):
    """
    添加权限组 VIEW
    """
    act = request.GET.get('act', '')
    if act == 'get_ajax_privileges':
        return HttpResponse(get_ajax_privileges(request))

    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['menu_name']
            module_id = request.POST.get('module', '')
            if Menu.objects.filter(menu_name=name):
                emg = u'添加失败, 此菜单 "%s" 已存在!' % name
            else:
                menu = form.save(commit=False)

                try:
                    latest_object = Menu.objects.filter(module_id=module_id).latest('id')
                    menu.id = latest_object.id + 1
                except:
                    menu.id = int(module_id) * 10 + 1

                menu.save()
                form.save_m2m()
                return redirect('menu_list')
        else:
            emg = u'菜单: 添加失败'

    modules = Module.objects.all()
    return render_to_response('account/menu_add.html', locals())


def menu_edit(request):
    """
    编辑菜单 VIEW
    """
    pk_id = request.GET.get('id', '')

    menu = Menu.objects.get(id=pk_id)
    if request.method == 'POST':
        form = MenuForm(request.POST, instance=menu)
        if form.is_valid():
            name = form.cleaned_data['menu_name']
            val_module = Menu.objects.filter(menu_name=name).exclude(id=pk_id)
            if val_module:
                emg = u'添加失败, 此权限组 %s 已存在!' % name
            else:
                form.save()
                return redirect('menu_list')
        else:
            emg = u'权限组: 添加失败'

    modules = Module.objects.all()
    return render_to_response('account/menu_edit.html', locals(), request)


def menu_change_status(request):
    """
    菜单状态变更 VIEW
    """
    jump_view = 'menu_list'
    pk_id = request.GET.get('id', '')

    try:
        menu = Menu.objects.get(id=pk_id)
    except:
        menu = None

    if not menu:
        message = '更新失败,不存在该菜单ID'
        return render_to_response('error.html', locals())

    menu.status = Menu.STATUS_CLOSE if menu.status == Menu.STATUS_OPEN else \
        Menu.STATUS_OPEN
    menu.save()

    message = '菜单状态更新成功'

    return render_to_response('success.html', locals())


# 权限管理(privilege).
def privilege_list(request):
    query_string = request.META.get('QUERY_STRING', '')
    privilege_name = request.GET.get('privilege_name', '').strip()
    privilege_group_id = request.GET.get('privilege_group_id', '')

    objects = Privilege.objects.all().order_by('-id')
    if privilege_name:
        objects = Privilege.objects.filter(privilege_name__contains=privilege_name)

    if privilege_group_id:
        objects = objects.filter(privilege_group_id=privilege_group_id)

    objects.order_by('-id')

    page_objects = pages(objects, request)

    privilege_groups = PrivilegeGroup.objects.all()
    return render_to_response('account/privilege_list.html', locals())


def privilege_add(request):
    """
    添加权限 VIEW
    """
    if request.method == 'POST':
        form = PrivilegeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['privilege_name']
            group_id = request.POST.get('privilege_group')
            if Privilege.objects.filter(privilege_name=name):
                emg = u'添加失败, 此权限 %s 已存在!' % name
            else:
                privilege = form.save(commit=False)

                try:
                    latest_object = Privilege.objects.filter(privilege_group_id=group_id).latest('id')
                    privilege.id = latest_object.id + 1
                except:
                    privilege.id = int(group_id) * 100 + 1

                privilege.save()
                form.save_m2m()

                return redirect('privilege_list')
        else:
            emg = u'权限: 添加失败'

    privilege_groups = PrivilegeGroup.objects.all()
    return render_to_response('account/privilege_add.html', locals())


def privilege_edit(request):
    """
    编辑权限 VIEW
    """
    pk_id = request.GET.get('id', '')

    privilege = Privilege.objects.get(id=pk_id)
    if request.method == 'POST':
        form = PrivilegeForm(request.POST, instance=privilege)
        if form.is_valid():
            name = form.cleaned_data['privilege_name']
            val_module = Privilege.objects.filter(privilege_name=name).exclude(id=pk_id)
            if val_module:
                emg = u'添加失败, 此权限 %s 已存在!' % name
            else:
                form.save()
                return redirect('privilege_list')
        else:
            emg = u'权限: 添加失败'

    privilege_groups = PrivilegeGroup.objects.all()
    return render_to_response('account/privilege_edit.html', locals(), request)


def privilege_change_status(request):
    """
    状态变更 VIEW
    """
    jump_view = 'privilege_list'
    pk_id = request.GET.get('id', '')

    try:
        privilege = Privilege.objects.get(id=pk_id)
    except:
        privilege = None

    if not privilege:
        message = '更新失败,不存在该权限ID'
        return render_to_response('error.html', locals())

    privilege.status = Privilege.STATUS_CLOSE if privilege.status == Privilege.STATUS_OPEN else \
        Privilege.STATUS_OPEN
    privilege.save()

    message = '状态更新成功'

    return render_to_response('success.html', locals())


# 账号管理(admin).
def admin_list(request):
    query_string = request.META.get('QUERY_STRING', '')
    name = request.GET.get('name', '').strip()
    email = request.GET.get('email', '').strip()
    role_id = request.GET.get('role_id', '')

    objects = Admin.objects.all().order_by('-id')
    if role_id and name and email:
        print 111
        objects=Admin.objects.filter(role_id=role_id).filter(name__contains=name).filter(email__contains=email)
    if role_id and name and not email:
        print 222
        objects=Admin.objects.filter(role_id=role_id).filter(name__contains=name)
    if role_id and email and not name:
        print 333
        objects=Admin.objects.filter(role_id=role_id).filter(email__contains=email)
    if name and email and not role_id:
        print 444
        objects=Admin.objects.filter(name__contains=name).filter(email__contains=email)
    if name and not role_id and not email:
        print 55
        objects = Admin.objects.filter(name__contains=name)

    if role_id and not email and not name:
        print 666
        objects = objects.filter(role_id=role_id)

    if email and not role_id and not name:
        print 777
        objects = Admin.objects.filter(email__contains=email)

    objects.order_by('-id')

    page_objects = pages(objects, request)

    roles = Role.objects.all()
    current_role_id = get_current_role_id(request)
    return render_to_response('account/admin_list.html', locals())


def admin_add(request):
    """
    添加账号 VIEW
    """
    import uuid
    from common.utils.account import server_add_user, user_add_mail

    current_admin = get_current_admin(request)
    if not current_admin or current_admin.is_super != Admin.IS_SUPPER:
        jump_view = 'admin_list'
        message = '对不起, 您没有添加账号的权限'
        return render_to_response('error.html', locals())

    if request.method == 'POST':
        form = AdminForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            pids = request.POST.getlist('pids', [])
            if Admin.objects.filter(name=name):
                emg = u'添加失败, 此账号 %s 已存在!' % name
            else:
                admin = form.save()

                pwd = request.POST.get('pwd')
                password = pwd if pwd else gen_rand_password()
                admin.pwd = md5(password)

                if pids:
                    checked_projects = Project.objects.in_bulk(pids)
                    admin.projects = checked_projects

                admin.uuid = uuid.uuid4().get_hex()
                admin.save()

                # user_add_mail(admin)

                return redirect('admin_list')
        else:
            emg = u'账号: 添加失败'

    roles = Role.objects.all()
    projects = Project.objects.all()
    return render_to_response('account/admin_add.html', locals())


def admin_edit(request):
    """
    编辑账号 VIEW
    """
    current_admin = get_current_admin(request)
    if not current_admin or current_admin.is_super != Admin.IS_SUPPER:
        jump_view = 'admin_list'
        message = '对不起, 您没有添加账号的权限'
        return render_to_response('error.html', locals())

    pk_id = request.GET.get('id', '')

    admin = Admin.objects.get(id=pk_id)
    org_role_id = admin.role_id
    if request.method == 'POST':
        form = AdminEditForm(request.POST, instance=admin)
        if form.is_valid():
            admin = form.save(commit=False)

            pwd = request.POST.get('pwd')
            if pwd:
                admin.pwd = md5(pwd)

            # pids = request.POST.getlist('pids', [])
            # if pids:
            #     checked_projects = Project.objects.in_bulk(pids)
            #     admin.projects = checked_projects
            # else:
            #     admin.projects = []

            admin.save()
            form.save_m2m()
            return redirect('admin_list')
        else:
            emg = u'账号: 添加失败'

    roles = Role.objects.all()
    # projects = Project.objects.all()

    # project_ids = []
    # for project in admin.projects.all():
    #     project_ids.append(project.id)
    return render_to_response('account/admin_edit.html', locals(), request)


def admin_change_status(request):
    """
    状态变更 VIEW
    """
    current_admin = get_current_admin(request)
    if not current_admin or current_admin.is_super != Admin.IS_SUPPER:
        jump_view = 'admin_list'
        message = '对不起, 您没有添加账号的权限'
        return render_to_response('error.html', locals())

    jump_view = 'admin_list'
    pk_id = request.GET.get('id', '')

    try:
        admin = Admin.objects.get(id=pk_id)
    except:
        admin = None

    if not admin:
        message = '更新失败,不存在该账号ID'
        return render_to_response('error.html', locals())

    admin.status = Admin.STATUS_CLOSE if admin.status == Admin.STATUS_OPEN else \
        Admin.STATUS_OPEN
    admin.save()

    message = '状态更新成功'

    return render_to_response('success.html', locals())


def admin_reset_pwd(request):
    """
    重置账号密码 VIEW
    """
    import uuid
    from common.utils.account import server_add_user, user_add_mail

    current_admin = get_current_admin(request)
    if not current_admin or current_admin.is_super != Admin.IS_SUPPER:
        jump_view = 'admin_list'
        message = '对不起, 您没有添加账号的权限'
        return render_to_response('error.html', locals())

    jump_view = 'admin_list'
    pk_id = request.GET.get('id', '')

    try:
        admin = Admin.objects.get(id=pk_id)
    except:
        admin = None

    if not admin:
        message = u'更新失败,不存在该账号ID'
        return render_to_response('error.html', locals())

    password = gen_rand_password()
    admin.pwd = md5(password)
    admin.uuid = uuid.uuid4().get_hex()
    admin.save()

    # ssh_key_pwd = gen_rand_password()
    # server_add_user(admin.name, ssh_key_pwd)
    # Todo: 推送公钥至所有关联服务器
    # user_add_mail(admin, password=password, ssh_key_pwd=ssh_key_pwd)

    message = u'密码更新成功,谨记:"%s"' % password

    return render_to_response('success.html', locals())


# 角色管理(role).
def role_list(request):
    query_string = request.META.get('QUERY_STRING', '')
    role_name = request.GET.get('role_name', '').strip()
    role_group_id = request.GET.get('role_group_id', '')

    objects = Role.objects.all().order_by('-id')
    if role_name:
        objects = Role.objects.filter(role_name__contains=role_name)

    if role_group_id:
        objects = objects.filter(role_group_id=role_group_id)

    objects.order_by('-id')

    page_objects = pages(objects, request)

    return render_to_response('account/role_list.html', locals())


def role_add(request):
    """
    添加角色 VIEW
    """
    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['role_name']
            if Role.objects.filter(role_name=name):
                emg = u'添加失败, 此角色 %s 已存在!' % name
            else:
                role = form.save()
                pids = request.POST.getlist('pids', [])
                print pids
                if pids:
                    checked_privileges = Privilege.objects.in_bulk(pids)
                    role.privileges = checked_privileges

                role.save()
                return redirect('role_list')
        else:
            emg = u'角色: 添加失败'

    modules = Module.objects.all()
    return render_to_response('account/role_add.html', locals())


def role_edit(request):
    """
    编辑角色 VIEW
    """
    pk_id = request.GET.get('id', '')

    role = Role.objects.get(id=pk_id)
    if request.method == 'POST':
        form = RoleForm(request.POST, instance=role)
        if form.is_valid():
            name = form.cleaned_data['role_name']
            val_role = Role.objects.filter(role_name=name).exclude(id=pk_id)
            if val_role:
                emg = u'添加失败, 此角色 %s 已存在!' % name
            else:
                role = form.save()
                pids = request.POST.getlist('pids', [])
                if pids:
                    checked_privileges = Privilege.objects.in_bulk(pids)
                    role.privileges = checked_privileges
                else:
                    role.privileges = []

                role.save()

                return redirect('role_list')
        else:
            emg = u'角色: 添加失败'

    modules = Module.objects.all()

    privilege_ids = []
    for privilege in role.privileges.all():
        privilege_ids.append(privilege.id)

    return render_to_response('account/role_edit.html', locals(), request)


def role_change_status(request):
    """
    状态变更 VIEW
    """
    jump_view = 'role_list'
    pk_id = request.GET.get('id', '')

    try:
        role = Role.objects.get(id=pk_id)
    except:
        role = None

    if not role:
        message = u'更新失败,不存在该角色ID'
        return render_to_response('error.html', locals())

    role.status = Role.STATUS_CLOSE if role.status == Role.STATUS_OPEN else \
        Role.STATUS_OPEN
    role.save()

    message = u'状态更新成功'

    return render_to_response('success.html', locals())


# 操作日志管理(operation_log)
def operation_log_list(request):
    import datetime
    admin_name = request.GET.get('admin_name', '').strip()
    privilege_name = request.GET.get('privilege_name', '').strip()
    begin_date = request.GET.get('begin_date', '').strip()
    end_date = request.GET.get('end_date', '').strip()

    privilege_group_id = request.GET.get('privilege_group_id', '')

    objects = OperationLog.objects.all().order_by('-id')
    if admin_name:
        objects = OperationLog.objects.filter(admin_name__contains=admin_name)

    if privilege_name:
        objects = objects.filter(privilege__privilege_name__contains=privilege_name)

    if begin_date:
        objects = objects.filter(create_at__gte=begin_date)

    if end_date:
        print end_date,type(end_date)
        tt = end_date.split('-')
        t2 = datetime.datetime(int(tt[0]), int(tt[1]), int(tt[2]))
        t3 = t2 + datetime.timedelta(1)
        objects = objects.filter(create_at__lte=t3)

    objects.order_by('-id')

    page_objects = pages(objects, request)

    privilege_groups = PrivilegeGroup.objects.all()
    return render_to_response('account/operation_log_list.html', locals())


def operation_log_show(request):
    pk_id = request.GET.get('id', '')
    log = OperationLog.objects.get(id=pk_id)

    return render_to_response('account/operation_log_detail.html', locals())
