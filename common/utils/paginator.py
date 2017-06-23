# -*- coding: utf-8 -*-


from django.core.paginator import Paginator, EmptyPage, InvalidPage


def parse_query_string(query_string=''):
    if not query_string:
        return {}

    query_list = query_string.split('&')
    query_dict = {}

    for item in query_list:
        if not item:
            continue

        key, value = item.split('=')
        query_dict[key] = value

    return query_dict


def build_query_string(query_params):
    query_list = []

    for k, v in query_params.iteritems():
        query_list.append(k + '=' + v)

    return '&'.join(query_list)


def get_page_url(query_string, page=1):
    query_dict = parse_query_string(query_string)
    query_dict['page'] = str(page)

    return build_query_string(query_dict)


def page_list_return(total, current=1):
    """
    page
    分页，返回本次分页的最小页数到最大页数列表
    """
    min_page = current - 2 if current - 4 > 0 else 1
    max_page = min_page + 4 if min_page + 4 < total else total

    return range(min_page, max_page + 1)


def pages(post_objects, request, page_size=20):
    """
    page public function , return page's object tuple
    分页公用函数，返回分页的对象元组
    """
    query_string = request.META.get('QUERY_STRING', '')
    paginator = Paginator(post_objects, page_size)
    current_page = int(request.GET.get('page', '1'))

    page_range = page_list_return(len(paginator.page_range), current_page)

    try:
        page_objects = paginator.page(current_page)
    except (EmptyPage, InvalidPage):
        page_objects = paginator.page(paginator.num_pages)

    page_objects.show_first = 0
    if current_page >= 5:
        page_objects.show_first = 1
        page_objects.first_page_url = '?' + get_page_url(query_string, 1)

    page_objects.show_end = 0
    if current_page <= (len(paginator.page_range) - 3):
        page_objects.end_page_url = '?' + get_page_url(query_string, paginator.num_pages)
        page_objects.show_end = 1

    if page_objects.has_previous():
        page_objects.previous_disable_css = ''
        page_objects.previous_page_url = '?' + get_page_url(query_string, page_objects.previous_page_number())
    else:
        page_objects.previous_disable_css = 'disabled'
        page_objects.previous_page_url = '#'

    if page_objects.has_next():
        page_objects.next_disable_css = ''
        page_objects.next_page_url = '?' + get_page_url(query_string, page_objects.next_page_number())
    else:
        page_objects.next_disable_css = 'disabled'
        page_objects.next_page_url = '#'

    page_objects.page_urls = {}
    for page in page_range:
        page_objects.page_urls[page] = '?' + get_page_url(query_string, page)

    page_objects.current_page = current_page
    page_objects.page_range = page_range
    page_objects.end_page = paginator.num_pages
    page_objects.count = paginator.count

    return page_objects

