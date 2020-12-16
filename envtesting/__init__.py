import logging
import os
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    nombre_env= os.environ['NOMBRE']
    return func.HttpResponse(
        f"El ambiente se llama: {nombre_env}",
        status_code=200
    )
