import click, json
from click.core import Context
from kubernetes.client.api.core_v1_api import CoreV1Api
from kubeleds import console
from kubernetes import client
from kubernetes.client.rest import ApiException

@click.command("get_namespaced_pods", short_help="Login to a cluster and get pod data for a given namespace")
@click.pass_context
@click.argument("api_host", required=True, type=click.STRING)
@click.argument("api_token", required=True, type=click.STRING)
@click.argument("namespace", required=True, type=click.STRING)
@click.argument("verify_ssl", required=False, default=True, type=click.BOOL)
@click.argument("data_key", required=False, default="get_namespaced_pods", type=click.STRING)
def get_namespaced_pods(ctx, api_host, api_token, namespace, verify_ssl, data_key):
    """This command will let you login in to a get the status of pods in the passed namespace

    Examples:

    /b
        
    """
    console.print("api_host:" + api_host)
    console.print("api_token:" + api_token)
    console.print("namespace:" + namespace)
    #console.print("verify_ssl:" + str(verify_ssl))

    aToken = api_token
    aConfiguration= client.Configuration()
    aConfiguration.debug = True
    aConfiguration.host = api_host
    aConfiguration.verify_ssl = verify_ssl
    aConfiguration.api_key = {"authorization": "Bearer " + aToken}

    with client.ApiClient(aConfiguration) as aApiClient:
        v1 = client.CoreV1Api(aApiClient)

        pod_statuses = []

        try:
            
            response = v1.list_namespaced_pod(namespace=namespace, _preload_content=False, watch=False)
            #response = v1.list_namespaced_pod(namespace=namespace, _preload_content=False, watch=False)
            pods = json.loads(response.data)

            with open('pods.json', 'w') as outfile:
                json.dump(pods["items"], outfile)

            console.print("Pods Count: " + str(len(pods["items"])))
            
            for pod in pods["items"]:
                #console.print(node.metadata.name)
                pod_status = PodStatus(pod)
                #json_status = json.dumps(node_status.__dict__)
                #node_statuses[node_status.get_name()] = node_status
                pod_statuses.append(pod_status)

            ctx.obj[data_key] = pod_statuses
        except ApiException as e:
            console.print("Kubernetes error: %s\n" % e)

        return pod_statuses

class PodStatus:
    def __init__(self, pod_info):
        self.set_name(pod_info["metadata"]["name"])
        self.set_status_conditions(pod_info)

    def __getitem__(self, item):
        console.print(item)
        return getattr(self, item)

    def get_name(self):
        return self._name
    
    def get_status_conditions(self):
        return self._status_conditions
    
    def set_name(self, value):
        self._name = value

    def set_status_conditions(self, pod):
        self._status_conditions = {}
        for cond in pod["status"]["conditions"]:
            #console.print(cond)
            cond_result = False
            if cond["type"] == "Ready":
                if cond["status"] == "True":
                    cond_result = True
            else:
                if cond["status"] == "False":
                    cond_result = True

            self._status_conditions[cond["type"]] = cond_result

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
