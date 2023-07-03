from rest_framework import filters


class CustomSearchFilter(filters.SearchFilter):
    search_param = 'search'
    operator = 'and'
