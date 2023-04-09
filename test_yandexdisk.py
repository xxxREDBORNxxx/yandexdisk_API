import pytest
from YaDisk.yandex_disk_api import YadiskApi


@pytest.mark.api
@pytest.mark.parametrize('path, folder_name, file_name, new_file_name',
                         [('disk:/', 'test_api', 'API_workfile.pdf', 'API_workfile_new.pdf')])
def test_task_api_yandex_disk(yadisk_session, config, path, folder_name, file_name, new_file_name):
    """
    Описание теста по заданию в файле API_workfile.pdf
    Перед запуском теста необходимо:
     1. проверить, что папка folder_name: 'test_api' отсутствует на яндекс-диске,
    т.к. тест уйдет в except при попытке создания файла с тем же именем.
     2. или изменить имя папки в parametrize.
    Это сделано для защиты от переполнения диска, т.к. отсутствует метод удаления создаваемых ресурсов.

    """
    path_folder = f"{path}{folder_name}"
    path_file = f"{path}{folder_name}/{file_name}"
    path_rename_file = f"{path}{folder_name}/{new_file_name}"

    api_yadisk = YadiskApi(yadisk_session)

    api_yadisk.create_folder(path_folder)
    link = api_yadisk.get_upload_link(path_file)
    api_yadisk.upload_resource(link, file_name)
    api_yadisk.rename_resource(path_file, path_rename_file)
    api_yadisk.get_resource_info(path_rename_file)
