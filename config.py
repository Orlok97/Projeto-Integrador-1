from dotenv import load_dotenv
import os
load_dotenv()
class Config:
    SECRET_KEY=os.getenv('SECRET_KEY')
    DATABASE_URI=os.getenv('DATABASE_URI')
    EMAIL_USER=os.getenv('EMAIL_USER')
    EMAIL_PASSWORD=os.getenv('EMAIL_PASSWORD')
    ADMIN_EMAIL=os.getenv('ADMIN_EMAIL')
    ADMIN_PASSWORD=os.getenv('ADMIN_PASSWORD')