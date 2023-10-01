
class UserNative():
    email : str
    dni : str
    fullName : str
    phone : str
    
    def __init__(self, email, dni, fullName, phone):
        self.email = email
        self.dni = dni
        self.fullName = fullName
        self.phone = phone
        
    def obj_to_dict(self):  # for build json format
        return {
            "email": self.email,
            "dni": self.dni,
            "fullName": self.fullName,
            "phone": self.phone
        }

class TrueNative():
    transactionIdentifier : str
    userIdentifier : str
    userWebhook : str
    user : UserNative
    
    def __init__(self, transactionIdentifier, userIdentifier, userWebhook, user):
        self.transactionIdentifier = transactionIdentifier
        self.userIdentifier = userIdentifier
        self.userWebhook = userWebhook
        self.user = user
        
    def obj_to_dict(self):  # for build json format
        return {
            "transactionIdentifier": self.transactionIdentifier,
            "userIdentifier": self.userIdentifier,
            "userWebhook": self.userWebhook,
            "user": self,
        }