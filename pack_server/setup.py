from setuptools import setup, find_packages

setup(name='server_chat_pyqt_september12',
      version='0.2',
      description='Server packet',
      packages=find_packages(),  # ,Будем искать пакеты тут(включаем авто поиск пакетов)
      author_email='test@mail.ru',
      author=' AlexPy1',
      install_requeres=['PyQt5', 'sqlalchemy', 'pycruptodome', 'pycryptodomex']
      # зависимости которые нужно до установить
      )