from rest_framework.exceptions import APIException


class OutOfStock(APIException):
    status_code = 409
    default_detail = 'Requested book is temporarily out of stock, try again later.'
    default_code = 'books_out_of_stock'
