import json
import logging
from service.userutils import *

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    logger.info("handler here!")
    httpMethod = event.get('httpMethod')
    if httpMethod == 'GET':
        return get_user(event, context)
    elif httpMethod == 'POST':
        return create_user(event, context)