import time
import urllib.request
import urllib.error
import bs4
import random
import socket


class ProxyPool:
    def __init__(self, proxies):
        self.__proxy_pool__ = [] if proxies is None else proxies
        self.__current_proxy__ = None
        self.__page_html__ = None

    def __is_captcha__(self):
        page_soup = bs4.BeautifulSoup(self.__page_html__, 'html.parser')
        return page_soup.text.find("Captcha") > 0

    def __is_available_proxy__(self, url, proxies):
        """
        Проверяет доступность прокси из списка.
        Возвращает первый доступный прокси или None, если все прокси не доступны.
        """
        for proxy in proxies:
            # Проверяем, что прокси начинается с 'https://', если нет - добавляем
            if not proxy.startswith('https'):
                proxy = f'https://{proxy}'  # Добавляем префикс 'https://', если его нет.

            proxy_dict = {
                #'http': proxy,
                'https': proxy,  # Для HTTPS-прокси используем 'https'
            }

            opener = urllib.request.build_opener(urllib.request.ProxyHandler(proxy_dict))
            opener.addheaders = [('User-agent', 'Mozilla/5.0')]

            try:
                # Пытаемся подключиться через прокси
                self.__page_html__ = opener.open(urllib.request.Request(url), timeout=10).read()
                print(f"proxy {proxy}: доступен")
                return proxy  # Возвращаем первый доступный прокси
            except Exception as detail:
                print(f"proxy {proxy}: {detail} - Недоступен")

        # Если все прокси недоступны
        print("Все прокси недоступны")
        return None


    def is_empty(self):
        return len(self.__proxy_pool__) == 0

    def get_available_proxy(self, url):
        print("The process of checking the proxies... Search an available one among them...")

        socket.setdefaulttimeout(5)
        found_proxy = False
        while len(self.__proxy_pool__) > 0 and found_proxy is False:
            proxy = random.choice(self.__proxy_pool__)

            is_available = self.__is_available_proxy__(url, proxy)
            is_captcha = self.__is_captcha__() if is_available else None

            if not is_available or is_captcha:
                if is_captcha:
                    print(f"proxy {proxy}: there is captcha.. trying another")
                else:
                    print(f"proxy {proxy}: unavailable.. trying another..")
                self.__proxy_pool__.remove(proxy)
                time.sleep(4)
                continue

            print(f"proxy {proxy}: available.. stop searching")
            self.__current_proxy__, found_proxy = proxy, True

        if self.__current_proxy__ is None:
            print(f"there are not available proxies..", end="\n\n")

        return self.__current_proxy__
