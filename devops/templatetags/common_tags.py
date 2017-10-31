# -*- coding: utf-8 -*-

import common.utils.date as cdate

from django import template
from django.shortcuts import reverse
from common.utils.paginator import parse_query_string, build_query_string
from apps.models import Admin,Privilege, Role,eproject
from apps.models import   *
from common.utils.sessions import get_current_admin
from common.utils.crypt import jiemi

register = template.Library()

###自定义过滤器
@register.filter(name='int2str')
def int2str(value):
    """
    int 转换为 str
    """
    return str(value)


@register.filter(name='str2int')
def str2int(value):
    """
    str 转换为 int
    """
    return int(value)


@register.filter(name='strip_space')
def strip_space(value):
    """
    int 转换为 str
    """
    return value.strip()



@register.simple_tag
def get_dict_value(dict_val, key):
    """
    获取 字典指定 key 的 值
    """
    try:
        value = dict_val[key]
    except:
        value = None

    try:
        if not value:
            value = dict_val[int(key)]
    except:
        value = None

    return value


@register.simple_tag
def get_list_value(list_val, key):
    """
    获取 列表指定 key 的 值
    """
    try:
        value = list_val[int(key)]
    except:
        value = None

    return value


@register.inclusion_tag('paginator.html')
def paginator_tag(objects):
    """
    分页导航标签
    :param objects:
    :return:
    """
    return {'page_objects': objects}

###自定义标签
@register.simple_tag
def form_errors(form):
    """
    获取 列表指定 key 的 值
    """
    error_string = '<div class="alert alert-warning text-center"><div class="error-msg">'

    errors = form.errors
    for field, error in errors.iteritems():
        if form.fields.has_key(field):
            error_string += "<p>%s : %s</p>" % (form.fields[field].label, error.as_text())
        else:
            error_string += "<p>%s</p>" % (error.as_text())

    error_string += '</div></div>'
    return error_string


@register.simple_tag
def get_jump_url(jump_view, request, exclude='id'):
    """
    获取 列表指定 key 的 值
    """
    query_string = request.META.get('QUERY_STRING', '')
    params = parse_query_string(query_string)

    if params.has_key(exclude):
        params.pop(exclude)

    jump_url = build_query_string(params)

    return reverse(jump_view) + '?' + jump_url


@register.filter(name='get_timestamp')
def get_timestamp(date_str, format_str='%Y-%m-%d %H:%M:%S'):
    """
    获取 列表指定 key 的 值
    """
    return cdate.timestamp(date_str, format_str)


@register.filter(name='get_date')
def get_date(timestamp, format_str='%Y-%m-%d %H:%M:%S'):
    """
    获取 列表指定 key 的 值
    """
    return cdate.date(timestamp, format_str)


@register.simple_tag
def get_nav_bar(request):
    """
    获取 列表指定 key 的 值
    """
    from apps.models import Privilege

    try:
        view_name = request.session['current_view_name']
        privilege = Privilege.objects.get(view_func=view_name)
        privilege_name = privilege.privilege_name
        module_name = privilege.privilege_group.module.module_name

    except:
        privilege_name = ''
        module_name = ''

    module_html = '<a>'+module_name+'</a>' if module_name else ''
    privilege_html = '<li class="active"><strong>'+privilege_name+'</strong></li>' if privilege_name else ''

    html = u'''
            <h2>%s</h2>
            <ol class="breadcrumb">
                <li>
                    <a href="%s">首页</a>
                </li>
                <li>
                    %s
                </li>
                %s
            </ol>
    ''' % (privilege_name, reverse('index'), module_html, privilege_html)

    return html


@register.simple_tag
def get_left_menu(request):
    from apps.models import Admin, Privilege, Module, Menu

    current_view_name = request.session['current_view_name']
    current_admin_id = request.session['current_admin_id']

    admin = Admin.objects.get(id=current_admin_id)

    current_privilege = None
    if current_view_name not in ['index', 'profile']:
        current_privilege = Privilege.objects.get(view_func=current_view_name)

    if admin.is_super == Admin.IS_SUPPER:
        privileges = Privilege.objects.filter(status=Privilege.STATUS_OPEN)
    else:
        privileges = admin.role.privileges.filter(status=Privilege.STATUS_OPEN)

    privileges_ids = []
    for pri in privileges:
        privileges_ids.append(pri.id)

    modules = Module.objects.filter(status=1).order_by('list_order')

    html = ''
    for module in modules:
        active = ''
        li_html = ''

        if current_privilege and current_privilege.privilege_group.module_id == module.id:
            active = 'active'

        menus = Menu.objects.filter(module_id=module.id, status=1)
        for menu in menus:
            if menu.privilege_id in privileges_ids:
                try:
                    reverse(menu.privilege.view_func)
                except:
                    print 'view name not exists(%s)' % menu.privilege.view_func
                    continue
                if current_privilege and menu.privilege_id == current_privilege.id:
                    li_html += '<li class="active"><a href="%s">%s</a></li>' % (reverse(menu.privilege.view_func), menu.menu_name)
                else:
                    li_html += '<li><a href="%s">%s</a></li>' % (reverse(menu.privilege.view_func), menu.menu_name)

        if not li_html:
            continue

        html += '''
        <li id="module-%d" class="%s">
            <a><i class="fa fa-inbox"></i> <span class="nav-label">%s</span><span class="fa arrow"></span></a>
            <ul class="nav nav-second-level">
            %s
            </ul>
        </li>
        ''' % (module.id, active, module.module_name, li_html)

    return html


@register.simple_tag
def get_admin_name(id):
    return Admin.objects.get(id=id).name


@register.simple_tag
def get_admin_username(id):
    return Admin.objects.get(id=id).user_name
    #return admin.user_name

@register.simple_tag
def get_eproject_pname(id):
    return eproject.objects.get(id=id).pname

@register.simple_tag
def get_eservernum_tag(id):
    return eserver.objects.filter(eproject_id=id).count()

# @register.simple_tag
# def get_os_user_name(id):
#     return OsUser.objects.get(id=id).username
    #return osuser.username


# @register.simple_tag
# def get_auth_name(id):
#     return OsAuth.objects.get(id=id).auth_name
#
#
# @register.simple_tag
# def get_osuser_name(id):
#     return OsAuth.objects.get(id=id).os_user.username


@register.assignment_tag
def check_privilege(request, view_name):
    # try:
    #     privilege = Privilege.objects.get(view_func=view_name)
    #     current_admin = get_current_admin(request)
    #     privileges = current_admin.role.privileges.all()
    #
    #     for item in privileges:
    #         if privilege.id == item.id:
    #             return True
    # except:
    #     return False
    privilege = Privilege.objects.get(view_func=view_name)
    current_admin = get_current_admin(request)
    if current_admin.role.id == Role.ROLE_SUPPER:
        return True

    privileges = current_admin.role.privileges.filter(status=Privilege.STATUS_OPEN)

    for item in privileges:
        if privilege.id == item.id:
            return True

    return False


@register.assignment_tag
def get_current_admin_info(request):
    current_admin = get_current_admin(request)

    return current_admin


@register.simple_tag
def get_eprivs_ptype(id):
    pl={'1':'READ-ONLY','2':'READ-WRITE'}
    pyy= str(eprivs.objects.get(id=id).ptype)
    return pl[pyy]

@register.simple_tag
def get_eserver_host(id):
    return eserver.objects.get(id=id).host

@register.simple_tag
def get_eserver_dport(id):
    return eserver.objects.get(id=id).dport

@register.simple_tag
def get_eprivs_dname(id):
    return eprivs.objects.get(id=id).dname

@register.simple_tag
def get_eprivs_time(id):
    return eprivs.objects.get(id=id).created_at


@register.simple_tag
def hjiemi(vstr):
    try:
        newpas=jiemi(vstr)
    except Exception,e:
        return 'error'
    return newpas

@register.simple_tag
def avg_sec(id):
    sums=global_query_review_history.objects.get(id=id).Query_time_sum
    cnt=global_query_review_history.objects.get(id=id).ts_cnt
    avg_s=sums/cnt
    return  avg_s
