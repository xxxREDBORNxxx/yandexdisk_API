from .json_schema_api import YadiskSchemas
from common import tools
from locators.yandex_api import YadiskEntryPoint


class YadiskApi:
    BASE_LINK = "https://cloud-api.yandex.net"
    HEADERS = {'Content-Type': 'application/json'}

    def __init__(self, session):
        self.session = session

    def create_folder(self, resource: str) -> None:
        """
        Метод создает папку на Яндекс Диске.
        :param resource: параметр относительного пути на яндекс диске к переименованному ресурсу.
         (Пример: 'disk:/my_folder').
        """
        url = f"{self.BASE_LINK}{YadiskEntryPoint.CREATE_FOLDER['source_path']}"
        response = self.session.put(url,
                                    headers=self.HEADERS,
                                    params={'path': resource})
        assert response.status_code == 201, response.text
        tools.validate_json(response.text, YadiskSchemas.CREATE_FOLDER)

    # TODO для расширенной проверки требуется также проверки имени, создания и модификации ресурса по метаданным
    def get_resource_info(self, resource) -> None:
        """
        Получение метаданных по ресурсу. Метод проверяет существование запрашиваемого ресурса на яндекс-диске
        по коду ответа 200.
        :param resource: параметр относительного пути на яндекс-диске. (Пример "disk:/my_folder/my_file")
        """
        url = f"{self.BASE_LINK}{YadiskEntryPoint.GETINFO['source_path']}"
        response = self.session.get(url,
                                    headers=self.HEADERS,
                                    params={'path': resource})
        assert response.status_code == 200, response.text

    def get_upload_link(self, resource: str) -> str:
        """
        :param resource: параметр относительного пути на яндекс-диске. (Пример "disk:/my_folder/my_file")
        :return ссылка для загрузки файла, действительна 30 мин
        """
        url = f"{self.BASE_LINK}{YadiskEntryPoint.GET_UPLOAD_LINK['source_path']}"
        response = self.session.get(url,
                                    headers=self.HEADERS,
                                    params={'path': resource,
                                            'overwrite': True})
        assert response.status_code == 200, response.text
        tools.validate_json(response.text, YadiskSchemas.GET_DOWNLOAD_LINK)
        return tools.get_json(response.text)["href"]

    def rename_resource(self, resource_old: str, resource_new: str) -> None:
        """
        :param resource_old: относительный путь на яндекс диске к переименуемому ресурсу.
         (Пример "disk:/my_folder/old_name_my_file)
        :param resource_new: относительный путь на яндекс диске к переименованному ресурсу.
         (Пример "disk:/my_folder/new_name_my_file)
        """
        url = f"{self.BASE_LINK}{YadiskEntryPoint.RENAME_RESOURCE['source_path']}"
        response = self.session.post(url,
                                     headers=self.HEADERS,
                                     params={"from": resource_old, "path": resource_new, 'overwrite': False})
        assert response.status_code == 201, response.text
        tools.validate_json(response.text, YadiskSchemas.RENAME_RESOURCE)

    def upload_resource(self, resource_link, path_file) -> None:
        """
        Метод для загрузки ресурса на Яндекс диск в открытой сессии с передачей токена.
        Возможен вариант загрузки файла по полученной ссылке без токена авторизации.
        :param path_file: локальный путь к загружаемому файлу.
        :param resource_link: ссылка для загрузки полученная методом get_download_link

        """
        with open(path_file, 'rb') as filedata:
            response = self.session.put(resource_link, files={'file': filedata})
        assert response.status_code == 201, response.text
