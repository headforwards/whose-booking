import yaml
import os

os.environ['app_id'] = ''
os.environ['app_secret'] = ''
os.environ['tenant_id'] = ''
os.environ['user_id'] = ''

def setup():
    try:
        stream = open('oauth_settings.yml', 'r')
        settings = yaml.load(stream, yaml.SafeLoader)
        for key in settings.keys():
            os.environ[key] = settings[key]
    except:
        pass