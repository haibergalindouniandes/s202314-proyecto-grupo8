class TransactionAlreadyRequested(Exception):

    msg = "Another request for that transaction id is still in process."

    def __str__(self) -> str:
        return self.msg


class NoHeaderToken(Exception):

    msg = "Header Authorization token is not present in the request."

    def __str__(self) -> str:
        return self.msg


class InvalidToken(Exception):

    msg = "Token is not authorized for this request."

    def __str__(self) -> str:
        return self.msg
