import os
from dotenv import load_dotenv
from appium.options.android import UiAutomator2Options
from selene_in_action import utils


class AppConfig:
    def __init__(self):
        # Загружаем переменные окружения из файла .env
        load_dotenv(dotenv_path=utils.file.abs_path_from_project('.env'))

        # Инициализируем переменные окружения
        self.remote_url = os.getenv('REMOTE_URL')
        self.device_name = os.getenv('DEVICE_NAME')
        self.app_name = os.getenv('APP_NAME')
        self.appWaitActivity = os.getenv('APP_WAIT_ACTIVITY')
        self.app_local = utils.file.abs_path_from_project(os.getenv('APP'))
        self.app_bstack = os.getenv('APP')
        self.platformName = os.getenv('PLATFORM_NAME')
        self.platformVersion = os.getenv('PLATFORM_VERSION')
        self.userName = os.getenv('USER_NAME')
        self.accessKey = os.getenv('ACCESS_KEY')
        self.runs_on_bstack = self.app_bstack.startswith('bs://')

    def to_driver_options(self, context: str):
        options = UiAutomator2Options()

        if context in ['local_emulator', 'real_local']:
            options.set_capability('remote_url', self.remote_url)
            options.set_capability('appWaitActivity', self.appWaitActivity)
            options.set_capability('app', self.app_local)

        if context == 'bstack':
            options.set_capability('remote_url', self.remote_url)
            options.set_capability('deviceName', self.device_name)
            options.set_capability('platformName', self.platformName)
            options.set_capability('platformVersion', self.platformVersion)
            options.set_capability('appWaitActivity', self.appWaitActivity)
            options.set_capability('app', self.app_bstack)
            options.set_capability(
                'bstack:options', {
                    'projectName': 'Wikipedia',
                    'buildName': 'Wikipedia',
                    'sessionName': 'Wikipedia',
                    'userName': self.userName,
                    'accessKey': self.accessKey,
                },
            )

        return options


# Инициализация конфигурации
config = AppConfig()
