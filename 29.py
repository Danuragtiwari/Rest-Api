# CursorPagination:-
# The cursor-based pagination presents an opaque 'cursor' indicator that the client may use to page through the result set.This pagination styleonly present forward and reverse controls and does not allow the client to navigate to arbitrary positions.
# Cursor based pagination requires that there is a unique,unchanging ordering of items in the result set.This ordering might typically be creation timestamp on the records,as this presents a consistent ordering to paginate against.
# The default is to order by '-created'.This assumes that there must be a 'created' timestamp field on the model instances,and will present a 'timeline' style paginated view,with the most recently added items first.
# The CursorPagination class includes a number of attributes that may be overridden to modify the pagination style.
# To set these attributes you should override the CursorPagination class,and then enable your custom pagination class.
# page_size:-A numeric value indicating the page size.If set this overrides the PAGE_SIZE setting.Defaults to the same value as the PAGE_SIZE settings key.
# cursor_query_param:-A string value indicating the name of the cursor query parameter.Defaults to 'cursor'
# ordering:- This should be a string,or list of strings,indicating the field againt whch the cursor based pagination will be applied.For example:- ordering='slug',defaults to -created.This value may also be overridden by using OrderignFilter on the view.
# Template:-the name of a template to use when rendering pagination controls in the browsable API.May be overridden to  modify the rendering style,or set to None to disable HTML pagination controls completely.Defaults to 'rest_framework/pagination/previous_and_next.html'