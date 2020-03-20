import elasticapm
from elasticapm.transport.http import Transport
from nameko.extensions import DependencyProvider

class ElasticAPMReporter(DependencyProvider):
    def setup(self):
        elastic_apm_config = self.container.config.get('ELASTIC_APM', {})
        elastic_apm_config.update({'transport_class': Transport})
        self.client = elasticapm.Client(elastic_apm_config)
        elasticapm.instrument()

    def get_dependency(self, worker_ctx):
        return self.client

    def worker_setup(self, worker_ctx):
        self.client.begin_transaction('nameko')

    def worker_result(self, worker_ctx, result, exc_info):
        service_name = "%s.%s" % (
            worker_ctx.container.service_name,
            worker_ctx.entrypoint.method_name
        )
        status = 'OK' if exc_info is None else 'ERROR'
        self.client.end_transaction(service_name, status)
