import datetime
import logging
import random

import azure.functions as func


def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)

    # Aqui escribiría mi código

    lista= ["Carla", "Chema", "Marta", "Manuel"]

    print(f"Hola {random.choice(lista)}")