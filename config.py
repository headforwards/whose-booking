import yaml
import os



def setup():
    try:
        stream = open('oauth_settings.yml', 'r')
        settings = yaml.load(stream, yaml.SafeLoader)
        for key in settings.keys():
            os.environ[key] = settings[key]

    except:
        pass