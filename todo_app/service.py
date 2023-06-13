from rest_framework.pagination import PageNumberPagination


class PaginationTasks(PageNumberPagination):
    page_size = 2
    max_page_size = 1000