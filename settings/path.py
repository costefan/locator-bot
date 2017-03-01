import os


PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_ROOT = os.path.join(PROJECT_ROOT, 'logs')
if not os.path.exists(LOG_ROOT):
    os.makedirs(LOG_ROOT)
