class Url:
    BASE_PAGE = 'https://stellarburgers.nomoreparties.site/'
    LOGIN_PAGE = BASE_PAGE+'login'
    FORGOT_PASSWORD_PAGE = BASE_PAGE+'forgot-password'
    RESET_PASSWORD_PAGE = BASE_PAGE+'reset-password'
    ACCOUNT_PROFILE_PAGE = BASE_PAGE+'account/profile'
    ORDER_LIST_PAGE = BASE_PAGE + 'feed'
    ORDER_HISTORY_PAGE = BASE_PAGE+'account/order-history'
    CREATE_USER_HANDLE = BASE_PAGE+'api/auth/register'
    DELETE_USER_HANDLE = BASE_PAGE+'api/auth/user'
    ORDERS_HANDLE = BASE_PAGE+'api/orders'


class TestData:
    INGREDIENTS = "61c0c5a71d1f82001bdaaa6d"