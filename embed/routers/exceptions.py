from fastapi import HTTPException, status


class NotFoundHTTPException(HTTPException):
    def __init__(self, msg: str):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=msg if msg else "Requested resource is not found",
        )


class AlreadyExistsHTTPException(HTTPException):
    def __init__(self, msg: str):
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail=msg if msg else "Document with specified id already exists",
        )

class InternalServerErrorHTTPException(HTTPException):
    def __init__(self, msg: str):
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=msg if msg else "Internal Server Error",
        )

