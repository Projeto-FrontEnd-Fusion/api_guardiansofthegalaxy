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


class TestimonialError(AppException):
    detail = "erro ao processar depoimento"
    error_code = "TESTIMONIAL_ERROR"
    status_code = 500


class TestimonialContentBlocked(AppException):
    detail = "O depoimento contem conteudo inadequado. Por favor, revise seu texto antes de enviar."
    error_code = "TESTIMONIAL_CONTENT_BLOCKED"
    status_code = 400


  

    