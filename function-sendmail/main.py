import functions_framework

# import necessary packages
from email.message import EmailMessage
import smtplib


@functions_framework.http
def email(name, dni, ruv, estado, createAt, emailTo):
    # create message object instance
    msg = EmailMessage()
    message = f" <h1><strong>MISO EMAIL&nbsp;</strong></h1> <h2><strong>Verificaci&oacute;n de usuario</strong></h2>  <h2><strong>Notifiaci&oacute;n al Usuario: </strong>{name}</h2>  <p>Se ha completado la verificaci&oacute;n del usuario con el siguienre resultado:</p>  <p>dni: {dni}</p>  <p>ruv: {ruv}</p>  <p>estado: {estado}</p>  <p>Fecha creaci&oacute;n: {createAt}</p>  <p>&nbsp;</p>  <p>Equipo Grupo 8</p>"

    # setup the parameters of the message
    password = "jmek wgba shnf msdr"
    msg["From"] = "misopruebas@gmail.com"
    msg["To"] = emailTo
    msg["Subject"] = "Miso Notificaciones"
    # add in the message body
    msg.add_header("Content-Type", "text/html")
    msg.set_payload(message)
    # create server
    server = smtplib.SMTP("smtp.gmail.com: 587")
    server.starttls()
    # Login Credentials for sending the mail
    server.login(msg["From"], password)
    # send the message via the server.
    server.sendmail(msg["From"], msg["To"], msg.as_string())
    server.quit()
    print("successfully sent email to %s:" % (msg["To"]))

@functions_framework.http
def email_card(name, lastfour, issuer, estado, createAt, emailTo):
    # create message object instance
    msg = EmailMessage()
    message = f" <h1><strong>MISO EMAIL&nbsp;</strong></h1> <h2><strong>Verificaci&oacute;n de Tarjeta</strong></h2>  <h2><strong>Notifiaci&oacute;n al Usuario: </strong>{name}</h2>  <p>Se ha completado la verificaci&oacute;n de la Terjeta de Credito Ingresada con el siguienre resultado:</p>  <p>Ultimos 4 digitos: {lastfour}</p>  <p>Emisor: {issuer}</p>  <p>estado: {estado}</p>  <p>Fecha creaci&oacute;n: {createAt}</p>  <p>&nbsp;</p>  <p>Equipo Grupo 8</p>"

    # setup the parameters of the message
    password = "jmek wgba shnf msdr"
    msg["From"] = "misopruebas@gmail.com"
    msg["To"] = emailTo
    msg["Subject"] = "Miso Notificaciones"
    # add in the message body
    msg.add_header("Content-Type", "text/html")
    msg.set_payload(message)
    # create server
    server = smtplib.SMTP("smtp.gmail.com: 587")
    server.starttls()
    # Login Credentials for sending the mail
    server.login(msg["From"], password)
    # send the message via the server.
    server.sendmail(msg["From"], msg["To"], msg.as_string())
    server.quit()
    print("successfully sent email to %s:" % (msg["To"]))


@functions_framework.http
def hello_http(request):
    request_json = request.get_json(silent=True)
    data = request.headers
    name = ""

    if data["secret-x"] == "d5f14860-f674-4248-be61-18bed307a49f":
        email(
            request_json["name"],
            request_json["dni"],
            request_json["ruv"],
            request_json["estado"],
            request_json["createAt"],
            request_json["emailTo"],
        )
        return "Succes!".format(name)
    elif data["secret-x"] == "d5f14860-f674-4248-be61-18bed307a4a0":
        email_card(
            request_json["name"],
            request_json["lastFourDigits"],
            request_json["issuer"],
            request_json["estado"],
            request_json["createAt"],
            request_json["emailTo"],
        )
        return "Succes!".format(name)
    else:
        return "Error!".format(name), 500
