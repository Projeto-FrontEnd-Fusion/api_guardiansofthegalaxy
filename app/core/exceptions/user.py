class AppException(Exception):
    detail = "Erro de aplicação"
    error_code = "APPLICATION_ERROR"
    status_code = 500


class UserCreationError(AppException):
    detail = "Usuário não pode ser criado"
    error_code = "USER_NOT_CREATED"
    status_code = 500
