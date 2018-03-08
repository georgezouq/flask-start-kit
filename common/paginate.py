from flask import request

DEFAULT_PAGE_SIZE = 10
DEFAULT_PAGE_NUMBER = 1


def paginate(query, schema):
    page = request.args.get('page', type=int, default=DEFAULT_PAGE_NUMBER)
    per_page = request.args.get('page_size', type=int, default=DEFAULT_PAGE_SIZE)

    page_obj = query.paginate(page=page, per_page=per_page)

    return {
        'page': {
            'total': page_obj.total,
            'pages': page_obj.pages,
            'per_page': per_page,
            'currentPage': page
        },
        'results': schema.dump(page_obj.items).data
    }
