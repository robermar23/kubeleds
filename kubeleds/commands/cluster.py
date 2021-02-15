import click, json
from click.core import Context
from kubernetes.client.api.core_v1_api import CoreV1Api
from kubeleds import console
from kubernetes import client

_v1=CoreV1Api

@click.command("get_cluster_nodes", short_help="Login to a cluster and get node data")
@click.pass_context
@click.argument("api_host", required=True, type=click.STRING)
@click.argument("api_token", required=True, type=click.STRING)
#@click.argument("verify_ssl", required=False, default=True, type=click.BOOL)
@click.argument("data_key", required=False, default="get_cluster_nodes", type=click.STRING)
def get_cluster_nodes(ctx, api_host, api_token, data_key):
    """This command will let you login in to a get the status of various resource types in a given cluster

    Examples:

    /b
        
    """
    console.print("api_host:" + api_host)
    console.print("api_token:" + api_token)
    #console.print("verify_ssl:" + str(verify_ssl))

    aToken = api_token
    aConfiguration= client.Configuration()
    aConfiguration.host = api_host
    aConfiguration.verify_ssl = True
    aConfiguration.api_key = {"authorization": "Bearer " + aToken}

    aApiClient = client.ApiClient(aConfiguration)
    v1 = client.CoreV1Api(aApiClient)

    nodes = v1.list_node()
    node_statuses = []

    console.print("Node Count: " + str(len(nodes.items)))
    
    for node in nodes.items:
        #console.print(node.metadata.name)
        node_status = NodeStatus(node)
        #json_status = json.dumps(node_status.__dict__)
        node_statuses.append(node_status)

    ctx.obj[data_key] = node_statuses

    return node_statuses

class NodeStatus:
    def __init__(self, node_info):
        self.set_name(node_info.metadata.name)
        self.set_status_conditions(node_info)

    def get_name(self):
        return self._name
    
    def get_status_conditions(self):
        return self._status_conditions
    
    def set_name(self, value):
        self._name = value

    def set_status_conditions(self, node):
        self._status_conditions = {}
        for cond in node.status.conditions:
            #console.print(cond)
            cond_result = False
            if cond.type == "Ready":
                if cond.status == "True":
                    cond_result = True
            else:
                if cond.status == "False":
                    cond_result = True

            self._status_conditions[cond.type] = cond_result

# @cluster.resultcallback()
# def process_commands(processors):
#     stream = ()

#     for processor in processors:
#         stream = processor(stream)

#     for _ in stream:
#         pass


# def processor(f):
#     def new_func(*args, **kwargs):
#         def processor(stream):
#             return f(stream, *args, **kwargs)

#         return processor
    
#     return update_wrapper(new_func, f)

# def generator(f):
#     @processor
#     def new_func(stream, *args, **kwargs):
#         yield from stream
#         yield from f(*args, **kwargs)

#     return update_wrapper(new_func, f)
