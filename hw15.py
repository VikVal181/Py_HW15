import os
import logging
import argparse
from collections import namedtuple

# Настройка логирования
logging.basicConfig(filename='directory_info.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Создание namedtuple для хранения информации о файлах и директориях
FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])


def collect_directory_info(directory_path):
    try:
        # Получаем список элементов в директории
        items = os.listdir(directory_path)

        # Итерируемся по каждому элементу
        for item in items:
            item_path = os.path.join(directory_path, item)

            # Получаем информацию о файле/директории
            is_directory = os.path.isdir(item_path)
            parent_directory = os.path.basename(directory_path)

            # Если это файл, получаем имя и расширение
            if not is_directory:
                name, extension = os.path.splitext(item)
            else:
                name, extension = item, None

            # Создаем объект FileInfo и выводим информацию в лог
            file_info = FileInfo(name, extension, is_directory, parent_directory)
            logging.info(file_info)

            # Если это директория, рекурсивно вызываем функцию для этой директории
            if is_directory:
                collect_directory_info(item_path)

    except Exception as e:
        logging.error(f"Error while collecting directory information: {str(e)}")


def main():
    parser = argparse.ArgumentParser(description='Collect information about files and directories.')
    parser.add_argument('directory_path', metavar='directory_path', type=str, help='Path to the directory')

    args = parser.parse_args()
    # Запускаем сбор информации
    collect_directory_info(args.directory_path)


if __name__ == "__main__":
    main()