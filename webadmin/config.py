class Config:
    SECRET_KEY = "supersecretkey"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost/webadmin"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
