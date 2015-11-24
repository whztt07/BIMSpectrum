import os
from datetime import timedelta


# default config
class BaseConfig(object):
    DEBUG = False
    # __file__ refers to the file config.py 
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
    APP_TEMP_FILE = os.path.join(APP_ROOT, 'tempfiles')
    
    MONGODB_URL=os.environ.get('MONGODB_URL')
    
    SECRET_KEY = os.environ.get('SECRET_KEY')
    STORMPATH_API_KEY_ID = os.environ.get('STORMPATH_API_KEY_ID')
    STORMPATH_API_KEY_SECRET = os.environ.get('STORMPATH_API_KEY_SECRET')
    STORMPATH_APPLICATION = os.environ.get('STORMPATH_APPLICATION')
    STORMPATH_COOKIE_DURATION = timedelta(minutes=30)
    STORMPATH_REGISTRATION_REDIRECT_URL = '/welcome'
    STORMPATH_ENABLE_MIDDLE_NAME = False
    STORMPATH_ENABLE_FORGOT_PASSWORD = True
    STORMPATH_ENABLE_FACEBOOK = True
    STORMPATH_ENABLE_GOOGLE = True
    STORMPATH_SOCIAL = {
        'FACEBOOK': {
            'app_id': os.environ.get('FACEBOOK_APP_ID'),
            'app_secret': os.environ.get('FACEBOOK_APP_SECRET'),
        },
        'GOOGLE': {
            'client_id': os.environ.get('GOOGLE_CLIENT_ID'),
            'client_secret': os.environ.get('GOOGLE_CLIENT_SECRET'),
        }
    }
    TESTING = True



class TestConfig(BaseConfig):
    DEBUG = True


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = False


class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False
