# LimitOffsetPagination:-
# This pagination style mirrors the syntax used when looking up multiple database records.The client includes both a 'limit' and an 'offset' query parameter.The limit indicated the maximum numbed is equivalent to the page_size in the other styles.The offset indicates the starting position of the query in relation of the complete set of unpaginated items.
# To enable the LimitOffsetPagination style globally,use the following configuration :
# REST_FRAMEWORK={
#     'DEFAULT_PAGINATION_CLASS':'rest_framework.pagination.LimitOffsePagination'
# }

# url/?limit=4&offset=6

# The LimitOffsetPagination class includes a number of attributes that may be overridden to modify the pagination style.
# To set these attributes you should override the LimitOffsetPagination class,and then enable your custom pagination class.
#default_limit:-A numeric value indicating the limit to use if one is not provided by the client in a query parameter.Defaults to the same value as the PAGE_SIZE settings key.
# limit_query-_param:-A string value indicating the name of the 'limit' query parameter.Defaults to 'limit'.
# offset_query_param:-A string value indicating the name of the 'offset' query parameter.Defaults to 'offset'
# max_limit:-If set this is a numeric value indicating the maximum allowable limit that may be requested by the client.Defaults to None.
# template:-The name of the template tomuse when rendering the pagination controls in the browsable API.May be overridden to modify the rendering style, or set to None to disable HTML pagination controls completely.Defaults to 'rest_framework/pagination/numbers.html'. 