import configparser
import os.path


def check_config():
    if os.path.isfile('template_bot/utils/config.ini'):
        return('Using existing config.')
    else:
        config = configparser.ConfigParser()
        config['Settings'] = {'Bot_token': 'token',
                              'Bot_prefix': '-',
                              'DB_host': 'localhost',
                              'DB_db': 'database',
                              'DB_user': 'username',
                              'DB_pass': 'password',
                              'bot_id': '0'}
        with open('template_bot/utils/config.ini', 'w') as config_file:
            config.write(config_file)
        return('Config file does not exist. Creating with default values.\nAdjust config and restart.')

def read(setting):
    config = configparser.ConfigParser()
    config.read('template_bot/utils/config.ini')
    return(config['Settings'][setting])


def db_config():
    db_config = {'host': str(read('DB_host')),
                 'database': str(read('DB_db')),
                 'user': str(read('DB_user')),
                 'password': str(read('DB_pass'))}
    return(db_config)