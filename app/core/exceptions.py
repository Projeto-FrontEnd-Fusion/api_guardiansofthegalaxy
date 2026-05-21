class AppException(Exception):
    detail = "Erro de aplicação"
    error_code = "APPLICATION_ERROR"
    status_code = 500


class UserCreationError(AppException):
    detail = "Usuário não pode ser criado"
    error_code = "USER_NOT_CREATED"
    status_code = 500


class UploadFailedError(AppException):
    detail = "Upload falhou"
    error_code = "UPLOAD_FAILED"
    status_code = 500


class UserInvalidError(AppException):
    detail = "Email inválido"
    error_code = "USER_INVALID_ERROR"
    status_code = 400
