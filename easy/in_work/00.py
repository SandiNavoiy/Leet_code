import zipfile
import os

# Путь к архиву
zip_path = "secrets.zip"

def calculate_json_size(zip_path):
    total_size = 0

    # Открываем архив
    with zipfile.ZipFile(zip_path, 'r') as archive:
        # Получаем список всех файлов в архиве
        for file_info in archive.infolist():
            # Проверяем расширение файла
            if file_info.filename.endswith('.json'):
                total_size += file_info.file_size

    return total_size


if os.path.exists(zip_path):
    json_size = calculate_json_size(zip_path)
    print(f"Суммарный размер файлов .json: {json_size} байт")
else:
    print(f"Архив {zip_path} не найден.")