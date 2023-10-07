from datetime import datetime


class UserVerification:

    ruv: str
    user_id: str
    transaction_id: str
    created_at: datetime
    processed_at: datetime
    user: dict
    user_webhook: str
    task_status: str
    score: int = None
    status: str = None

    def load(self, data:dict) -> None:
        self.ruv = data.get("RUV")
        self.user_id = data.get("userIdentifier")
        self.transaction_id = data.get("transactionIdentifier")
        self.created_at = data.get("createdAt")
        self.processed_at = data.get("processedAt")
        self.user = data.get("user")
        self.user_webhook = data.get("userWebhook")
        self.task_status = data.get("task_status")
        self.score = data.get("score")
        self.status = data.get("status")

    def raw(self) -> dict:
        return {
            "RUV": self.ruv,
            "userIdentifier": self.user_id,
            "transactionIdentifier": self.transaction_id,
            "createdAt": self.created_at,
            "processedAt": self.processed_at,
            "user": self.user,
            "userWebhook": self.user_webhook,
            "task_status": self.task_status,
            "score": self.score,
            "status": self.status
        }

    def short(self) -> dict:
        data = self.raw()
        data.pop("user")
        data.pop("processedAt")
        data.pop("userWebhook")
        data.pop("score")
        data.pop("status")
        return data

    def resp(self) -> dict:
        return {
            "RUV": self.ruv,
            "userIdentifier": self.user_id,
            "transactionIdentifier": self.transaction_id,
            "createdAt": self.created_at,
            "status": self.status,
            "score": self.score
        }