import os
from waitress import serve
import yaml

from my_project import create_app

DEVELOPMENT_PORT = 5000
PRODUCTION_PORT = 8080
HOST = "0.0.0.0"
DEVELOPMENT = "development"
PRODUCTION = "production"
FLASK_ENV = "FLASK_ENV"
ADDITIONAL_CONFIG = "ADDITIONAL_CONFIG"

if __name__ == '__main__':
    flask_env = os.environ.get(FLASK_ENV, DEVELOPMENT).lower()
    config_yaml_path = os.path.join(os.getcwd(), 'config', 'app.yml')

    with open(config_yaml_path, "r", encoding='utf-8') as yaml_file:
        config_data_dict = yaml.load(yaml_file, Loader=yaml.FullLoader)
        additional_config = config_data_dict[ADDITIONAL_CONFIG]

        if flask_env == DEVELOPMENT:
            config_data = config_data_dict[DEVELOPMENT]
            config_data[
                'SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:23436703@localhost:5000/Discord'
            app = create_app(config_data, additional_config)
            app.run(port=DEVELOPMENT_PORT, debug=True)

        elif flask_env == PRODUCTION:
            config_data = config_data_dict[PRODUCTION]
            config_data[
                'SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:23436703@localhost:5000/Discord'
            serve(create_app(config_data, additional_config), host=HOST, port=PRODUCTION_PORT)

        else:
            raise ValueError(f"Перевірте змінну середовища ОС '{FLASK_ENV}'")
