# -*- coding: utf-8 -*-
from django.utils.deprecation import MiddlewareMixin


class OperationLogMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        return None

