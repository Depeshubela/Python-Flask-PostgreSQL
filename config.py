import os 


class Config:
    #pjdir = os.path.abspath(os.path.dirname(__file__))
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.abspath(os.path.dirname(__file__)) + "/app_blog/static/data/data_register.sqlite"
    SECRET_KEY = b'\xb9k\xdf@\x0e\x1f(\xf2\xb0\xd0\xcb?Y\xdcN\x19G\x12e\xa8\x8b\xe5\xccS'

    #class EmailConfig:
    #DEBUG=False
    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT=465
    MAIL_USE_SSL=True #用SSL協定
    MAIL_DEFAULT_SENDER=('admin', 'sean940106@gmail.com') #寄信人
    MAIL_MAX_EMAILS=10 #一次最大送信數
    MAIL_USERNAME='sean940106@gmail.com' #寄信者信箱
    MAIL_PASSWORD='kqhedsyrohrgflcm' #寄信者密碼
    SECURITY_PASSWORD_SALT = "Liebe" 
    SESSION_PROTECTION = 'strong'