class UserCreationError(Exception):
    detail = "Usuário não pode ser criado"
    error_code = "USER_NOT_CREATED"
