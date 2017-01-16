from proxyserver.celery import app
from concurrent.futures import ThreadPoolExecutor

from proxyserver.apps.core import tools


@app.task
def add_proxy_to_db():
    with ThreadPoolExecutor(len(tools.call_scrappers())) as executor:
        for _ in executor.map(tools.take_proxy_from_scrapper, tools.call_scrappers()):
            pass


@app.task
def check_task():
    with ThreadPoolExecutor(len(tools.get_unchecked_proxies())) as executor:
        for _ in executor.map(tools.check_proxy_for_available, tools.get_unchecked_proxies()):
            pass
