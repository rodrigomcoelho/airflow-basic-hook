from airflow.hooks.base import BaseHook
from airflow.models.connection import Connection
from requests import request
from requests.exceptions import HTTPError
from time import sleep
from json import dumps as json_dumps


class ZendeskHook(BaseHook):
    def __init__(self, conn_id: str):
        self._conn_id = self.get_conn(conn_id=conn_id)

    def get_conn(self, conn_id: str) -> Connection:
        return super().get_connection(conn_id)


    @property
    def auth(self) -> tuple[str, str]:
        return (self._conn_id.login, self._conn_id.password)

    def run(self, method: str, endpoint: str) -> dict:
        url = self._conn_id.host + endpoint
        try:
            response = request(
                method=method,
                url=url,
                auth=self.auth
            )
            response.raise_for_status()
        except HTTPError as http_error:
            self.log.error(http_error)
        else:
            sleep(0.5)
            return json_dumps(response.text)

    def get_rows(self, method: str, endpoint: str) -> list[dict]:
        rows = []

        rows += self.run(method, endpoint)

        return rows
