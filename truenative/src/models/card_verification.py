from datetime import datetime


class CardVerification:

    ruv: str
    transaction_id: str
    created_at: datetime
    processed_at: datetime
    card: dict
    token: str
    task_status: str
    issuer: str
    status: str = None

    def load(self, data:dict) -> None:
        self.ruv = data.get("RUV")
        self.transaction_id = data.get("transactionIdentifier")
        self.created_at = data.get("createdAt")
        self.processed_at = data.get("processedAt")
        self.card = data.get("card")
        self.token = data.get("token")
        self.task_status = data.get("task_status")
        self.issuer = data.get("issuer")
        self.status = data.get("status")

    def raw(self) -> dict:
        return {
            "RUV": self.ruv,
            "transactionIdentifier": self.transaction_id,
            "createdAt": self.created_at,
            "processedAt": self.processed_at,
            "card": self.card,
            "token": self.token,
            "task_status": self.task_status,
            "status": self.status,
            "issuer": self.issuer
        }

    def short(self) -> dict:
        data = self.raw()
        data.pop("card")
        data.pop("processedAt")
        data.pop("status")
        return data

    def resp(self) -> dict:
        return {
            "RUV": self.ruv,
            "transactionIdentifier": self.transaction_id,
            "createdAt": self.created_at,
            "status": self.status
        }
