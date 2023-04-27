from airflow.models.baseoperator import BaseOperator
from sbf.cliente.sensors.zendesk import ZendeskHook


class ZendeskOperator(BaseOperator):
    def __init__(self, *args, conn_id: str, **kwargs):
        super().__init__(*args, **kwargs)
        self.zendesk_hook = ZendeskHook(conn_id=conn_id)
