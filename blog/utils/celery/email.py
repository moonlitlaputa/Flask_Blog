from flask_mail import Message
from flask import render_template, current_app

from blog import mail, celery


@celery.task()
def send_email(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    msg = Message(app.config['FLASK_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
                  sender=app.config['FLASK_MAIL_SENDER'],
                  recipients=[to])
    msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)
