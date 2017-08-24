from rest_framework.pagination import LimitOffsetPagination
from rest_framework.utils.urls import remove_query_param, replace_query_param
from Anonymous_message.settings import HTTPS


# 将url的 HTTP 改成HTTPS
class HTTPSLimitOffsetPagination(LimitOffsetPagination):
    def get_next_link(self):
        if self.offset + self.limit >= self.count:
            return None

        url = self.request.build_absolute_uri()
        if HTTPS:
            url = 'https' + url.lstrip('http')
        url = replace_query_param(url, self.limit_query_param, self.limit)

        offset = self.offset + self.limit
        return replace_query_param(url, self.offset_query_param, offset)

    def get_previous_link(self):
        if self.offset <= 0:
            return None

        url = self.request.build_absolute_uri()
        if HTTPS:
            url = 'https' + url.lstrip('http')
        url = replace_query_param(url, self.limit_query_param, self.limit)

        if self.offset - self.limit <= 0:
            return remove_query_param(url, self.offset_query_param)

        offset = self.offset - self.limit
        return replace_query_param(url, self.offset_query_param, offset)
