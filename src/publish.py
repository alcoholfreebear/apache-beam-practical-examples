
# import packages
import os 
import time
from pathlib import Path
from google.cloud import pubsub_v1

# publisher
project_id = Path('../../secrets/project_id.secret').read_text().strip()
pubsub_topic = f'projects/{project_id}/topics/housing'

publisher = pubsub_v1.PublisherClient()

with open('../data/housing_short.csv', 'rb') as f:
    for row in f:
        publisher.publish(pubsub_topic, row)
        time.sleep(1)
        
