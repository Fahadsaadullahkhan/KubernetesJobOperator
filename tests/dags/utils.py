import os
from airflow_kubernetes_job_operator.kube_api import KubeObjectKind
import warnings
import logging
import sys

print_version = str(sys.version).replace("\n", " ")
logging.info(f"""
-----------------------------------------------------------------------
Executing dags in python version: {print_version}
-----------------------------------------------------------------------
""")

warnings.filterwarnings("ignore", category=DeprecationWarning)

# KubeObjectKind.register_global_kind(
#     KubeObjectKind("HCJob", "hc.dto.cbsinteractive.com/v1alpha1", parse_kind_state=KubeObjectKind.parse_state_job)
# )


default_args = {"owner": "tester", "start_date": "1/1/2020", "retries": 0}

REPO_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
DAGS_PATH = os.path.join(REPO_PATH, "tests", "dags")


def resolve_file(fpath: str):
    if fpath.startswith("."):
        if fpath.startswith("./"):
            fpath = os.path.join(DAGS_PATH, fpath[2:])
        else:
            fpath = os.path.join(DAGS_PATH, fpath)
    return os.path.abspath(fpath)
