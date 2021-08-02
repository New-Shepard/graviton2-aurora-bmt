from aws_cdk import core
from artifacts import (
    assets,
    infra,
    db,
    cloud9,
)

class AuroraGraviton2ScenarioStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        assets.BenchmarkAssets(self)

        network = infra.Network(self, 'Network')
        db.Aurora(self, 'db', bmt_vpc=network.vpc)
        cloud9.Cloud9(self, 'workspace', bmt_vpc=network.vpc)
