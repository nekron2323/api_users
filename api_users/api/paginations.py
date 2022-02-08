from collections import OrderedDict
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response


class UserListPagination(LimitOffsetPagination):
    limit_query_param = 'size'
    offset_query_param = 'page'

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('data', data),
            ('meta', OrderedDict([
                ('pagination', OrderedDict([
                    ('total', self.count),
                    ('page', self.offset),
                    ('size', self.limit)
                ]))
            ]))
        ]))
