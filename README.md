### Сбор данных с сайта объявлений об аренде и продаже недвижимости Циан

Cianparser - это библиотека Python 3 (версии 3.8 и выше) для парсинга сайта  [Циан](http://cian.ru).
С его помощью можно получить достаточно подробные и структурированные данные по краткосрочной и долгосрочной аренде, продаже квартир, домов, танхаусов итд.

### Установка
```bash
pip install cianparser
```

### Использование
```python
import cianparser

moscow_parser = cianparser.CianParser(location="Москва")
data = moscow_parser.get_flats(deal_type="sale", rooms=(1, 2), with_saving_csv=True, additional_settings={"start_page":1, "end_page":1})

print(data[0])
```

```
                              Preparing to collect information from pages..
The absolute path to the file: 
 /Users/macbook/some_project/cianparser/cian_parsing_result_flat_sale_1_2_moskva_12_Jan_2024_21_48_43_100892.csv 

The page from which the collection of information begins: 
 https://cian.ru/cat.php?engine_version=2&p=1&with_neighbors=0&region=1&deal_type=sale&offer_type=flat&room1=1&room2=1

Collecting information from pages with list of offers
 1 | 1 page with list: [=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>] 100% | Count of all parsed: 28. Progress ratio: 50 %. Average price: 45 547 801 rub
 2 | 2 page with list: [=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>] 100% | Count of all parsed: 56. Progress ratio: 100 %. Average price: 54 040 102 rub

The collection of information from the pages with list of offers is completed
Total number of parsed offers: 56.
{
    "author": "MR Group",
    "author_type": "developer",
    "url": "https://www.cian.ru/sale/flat/292125772/",
    "location": "Москва",
    "deal_type": "sale",
    "accommodation_type": "flat",
    "floor": 20,
    "floors_count": 37,
    "rooms_count": 1,
    "total_meters": 39.6,
    "price": 28623910,
    "district": "Беговой",
    "street": "Ленинградский проспект",
    "house_number": "вл8",
    "underground": "Белорусская",
    "residential_complex": "Slava"
}
```
### Инициализация CianParser
Параметры, используемые при инициализации парсера:
* __location__ - локация объявления, к примеру, _Санкт-Петербург_ (для просмотра доступных мест используйте _cianparser.list_locations())_

### Метод get_flats
Данный метод принимает следующий аргументы:
* __deal_type__ - тип объявления, к примеру, долгосрочная, краткосрочная аренда, продажа _("rent_long", "rent_short", "sale")_
* __rooms__ - количество комнат, к примеру, _1, (1,3, "studio"), "studio, "all"_; по умолчанию любое _("all")_
* __with_saving_csv__ - необходимо ли сохранение собираемых данных (в реальном времени в процессе сбора данных) или нет, по умолчанию _False_
* __with_extra_data__ - необходимо ли сбор дополнительных данных, но с кратным продолжительности по времени (см. ниже в __Примечании__), по умолчанию _False_
* __additional_settings__ - дополнительные настройки поиска (см. ниже в __Дополнительные настройки поиска__), по умолчанию _None_

Пример использования данного метода представлен выше

В проекте предусмотрен функционал корректного завершения в случае окончания страниц. По данному моменту, следует изучить раздел __Ограничения__

_**В настоящее время функционал доступен только по продажам (sale) и долгосрочном арендам (rent_long).**_

### Метод get_newobjects (даннные по новостройкам)
Данный метод принимает следующий аргументы:
* __with_saving_csv__ - необходимо ли сохранение собираемых данных (в реальном времени в процессе сбора данных) или нет, по умолчанию _False_

Пример:
```python
import cianparser

moscow_parser = cianparser.CianParser(location="Москва")
data = moscow_parser.get_newobjects(with_saving_csv=True)

print(data[0])
```
```
                              Preparing to collect information from pages..
The absolute path to the file: 
/Users/macbook/some_project/cianparser/cian_parsing_result_newobject_sale_1_1_moskva_13_Jan_2024_01_27_32_734734.csv 

The page from which the collection of information begins: 
 https://cian.ru/newobjects/list/?engine_version=2&p=1&with_neighbors=0&region=1&deal_type=sale&offer_type=newobject

Collecting information from pages with list of offers
 1 | 1 page with list: [=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>] 100% | Count of all parsed: 25. Progress ratio: 100 %.

The collection of information from the pages with list of offers is completed
Total number of parsed offers: 25.
{
    "name": "ЖК «SYMPHONY 34 (Симфони 34)»",
    "location": "Москва",
    "accommodation_type": "newobject",
    "url": "https://zhk-symphony-34-i.cian.ru",
    "full_location_address": "Москва, САО, Савеловский, 2-я Хуторская ул., 34",
    "year_of_construction": "2025",
    "house_material_type": "Монолитный",
    "finish_type": "Предчистовая, чистовая",
    "ceiling_height": "3,0 м",
    "class": "Премиум",
    "parking_type": "Подземная, гостевая",
    "floors_from": 36,
    "floors_to": 54,
    "builder": "Застройщик MR Group"
}
```

### Дополнительные настройки поиска
Пример:
```python
additional_settings = {
    "start_page":1,
    "end_page": 10,
    "is_by_homeowner": True,
    "min_price": 1000000,
    "max_price": 10000000,
    "min_balconies": 1,
    "have_loggia": True,
    "min_house_year": 1990,
    "max_house_year": 2023,
    "min_floor": 3,
    "max_floor": 4,
    "min_total_floor": 5,
    "max_total_floor": 10,
    "house_material_type": 1,
    "metro": "Московский",
    "metro_station": "ВДНХ",
    "metro_foot_minute": 45,
    "flat_share": 2,
    "only_flat": True,
    "only_apartment": True,
    "sort_by": "price_from_min_to_max",
}
```
* __start_page__ - страница, с которого начинается сбор данных
* __end_page__ - страница, с которого заканчивается сбор данных
* __is_by_homeowner__ - объявления, созданных только собственниками
* __min_price__ - цена от (в рублях)
* __max_price__ - цена до (в рублях)
* __min_balconies__ - минимальное количество балконов
* __have_loggia__ - наличие лоджи
* __min_house_year__ - год постройки дома от
* __max_house_year__ - год постройки дома до
* __min_floor__ - этаж от
* __max_floor__ - этаж до
* __min_total_floor__ - этажей в доме от
* __max_total_floor__ - этажей в доме до
* __house_material_type__ - тип дома (_см ниже возможные значения_)
* __metro__ - название метрополитена (_см ниже возможные значения_)
* __metro_station__ - станция метро (доступно при заданом metro)
* __metro_foot_minute__ - сколько минут до метро пешком
* __flat_share__ - с долями или без (1 - только доли, 2 - без долей)
* __only_flat__ - без апартаментов
* __only_apartment__ - только апартаменты
* __sort_by__ - сортировка объявлений (_см ниже возможные значения_)

#### Возможные значения поля **house_material_type**
- _1_ - киричный
- _2_ - монолитный
- _3_ - панельный
- _4_ - блочный
- _5_ - деревянный
- _6_ - сталинский
- _7_ - щитовой
- _8_ - кирпично-монолитный

#### Возможные значения полей **metro** и **metro_station**
Можно посмотреть используя **_cianparser.list_metro_stations()_**

#### Возможные значения поля **sort_by**
- "_price_from_min_to_max_" - сортировка по цене (сначала дешевле)
- "_price_from_max_to_min_" - сортировка по цене (сначала дороже)
- "_total_meters_from_max_to_min_" - сортировка по общей площади (сначала больше)
- "_creation_data_from_newer_to_older_" - сортировка по дате добавления (сначала новые)
- "_creation_data_from_older_to_newer_" - сортировка по дате добавления (сначала старые)

### Признаки, получаемые в ходе сбора данных с предложений по долгосрочной аренде недвижимости
* __district__ - район
* __underground__ - метро
* __street__ - улица
* __house_number__ - номер дома
* __floor__ - этаж
* __floors_count__ - общее количество этажей
* __total_meters__ - общая площадь
* __living_meters__ - жилая площади
* __kitchen_meters__ - площадь кухни
* __rooms_count__ - количество комнат
* __year_construction__ - год постройки здания
* __house_material_type__ - тип дома (киричный/монолитный/панельный итд)
* __heating_type__ - тип отопления
* __price_per_month__ - стоимость в месяц
* __commissions__ - комиссия, взымаемая при заселении
* __author__ - автор объявления
* __author_type__ - тип автора 
* __phone__ - номер телефона в объявлении
* __url__ - ссылка на объявление

Возможные значения поля __author_type__:
- __real_estate_agent__ - агентство недвижимости
- __homeowner__ - собственник
- __realtor__ - риелтор
- __official_representative__ - ук оф.представитель
- __representative_developer__ - представитель застройщика
- __developer__ - застройщик
- __unknown__ - без указанного типа

### Признаки, получаемые в ходе сбора данных с предложений по продаже недвижимости

Признаки __аналогичны__ вышеописанным, кроме отсутствия полей __price_per_month__ и __commissions__.

При этом появляются новые:
* __price__ - стоимость недвижимости
* __residential_complex__ - название жилого комплекса
* __object_type__ -  тип жилья (вторичка/новостройка)
* __finish_type__ - отделка

### Признаки, получаемые в ходе сбора данных по новостройкам
* __name__ - наименование ЖК
* __url__ - ссылка на страницу
* __full_location_address__ - полный адрес расположения ЖК
* __year_of_construction__ - год сдачи
* __house_material_type__ - тип дома (_см выше возможные значения_)
* __finish_type__ - отделка
* __ceiling_height__ - высота потолка
* __class__ - класс жилья
* __parking_type__ - тип парковки
* __floors_from__ - этажность (от)
* __floors_to__ - этажность (до)
* __builder__ - застройщик

### Сохранение данных
Имеется возможность сохранения собираемых данных в режиме реального времени. Для этого необходимо подставить в аргументе 
__with_saving_csv__ значение ___True___.

#### Пример получаемого файла при вызове метода __get_flats__ с __with_extra_data__ = __True__:

```bash
cian_parsing_result_flat_sale_1_1_moskva_12_Jan_2024_22_29_48_117413.csv
```
| author | author_type | url | location | deal_type | accommodation_type | floor | floors_count | rooms_count | total_meters | price_per_m2 | price | year_of_construction | object_type | house_material_type | heating_type | finish_type | living_meters | kitchen_meters | phone | district | street | house_number | underground | residential_complex
| ------ | ------ | ------ | ------ | ------ | ------ | ----------- | ---- | ---- | --------- | ------------------ | ----- | ------------ | ----------- | ------------ | --------------- | ----------- | ----------- | -------------------- | --- | --- | --- | --- | --- | ---
| White and Broughton | real_estate_agent | https://www.cian.ru/sale/flat/290499455/ | Москва | sale | flat | 3 | 40 | 1 | 45.5 | 709890 | 32300000 | 2021 | Вторичка | Монолитный | Центральное | -1 | 19.0 | 6.0 | +79646331510 | Хорошевский | Ленинградский проспект | 37/4 | Динамо | Прайм Парк
| ФСК | developer | https://www.cian.ru/sale/flat/288376323/ | Москва | sale | flat | 24 | 47 | 2 | 46.0 | 528900 | 24329400 | 2024 | Новостройка | Монолитно-кирпичный | -1 | Без отделки, предчистовая, чистовая | 18.0 | 15.0 | +74951387154 | Обручевский |  Академика Волгина | 2С1 | Калужская | Архитектор
| White and Broughton | real_estate_agent | https://www.cian.ru/sale/flat/292416804/ | Москва | sale | flat | 2 | 41 | 2 | 60.0 | 783333 | 47000000 | 2021 | Вторичка | -1 | Центральное | -1 | 43.0 | 5.0 | +79646331510 | Хорошевский | Ленинградский проспект | 37/5 | Динамо | Прайм Парк

#### Пример получаемого файла при вызове метода __get_newobjects__:

```bash
cian_parsing_result_newobject_sale_1_1_moskva_13_Jan_2024_01_27_32_734734.csv
```
| name | location | accommodation_type | url | full_location_address | year_of_construction | house_material_type | finish_type | ceiling_height | class | parking_type | floors_from | floors_to | builder
 | ----- | ------------ | ----------- | ------------ | --------------- | ----------- | ----------- | -------------------- | --- | --- | --- | --- | --- | ---
| ЖК «SYMPHONY 34 (Симфони 34)» | Москва | newobject | https://zhk-symphony-34-i.cian.ru | Москва, САО, Савеловский, 2-я Хуторская ул., 34 | 2025 | Монолитный | Предчистовая, чистовая | 3,0 м | Премиум | Подземная, гостевая | 36 | 54 | Застройщик MR Group
| ЖК «Коллекция клубных особняков Ильинка 3/8» | Москва | newobject | https://zhk-kollekciya-klubnyh-osobnyakov-ilinka-38-i.cian.ru | Москва, ЦАО, Тверской, ул. Ильинка | 2024 | Монолитно-кирпичный, монолитный | Без отделки | от 3,35 м до 6,0 м | Премиум | Подземная, гостевая | 3 | 5 | Застройщик Sminex-Интеко
| ЖК «Victory Park Residences (Виктори Парк Резиденсез)» | Москва | newobject | https://zhk-victory-park-residences-i.cian.ru | Москва, ЗАО, Дорогомилово, ул. Братьев Фонченко | 2024 | Монолитный | Чистовая | — | Премиум | Подземная | 10 | 11 | Застройщик ANT Development


### Cloudflare, CloudScraper
Для обхода блокировки в проекте задействован **CloudScraper** (библиотека **cloudscraper**), который позволяет успешно обходить защиту **Cloudflare**.

Вместе с тем, это не гарантирует отсутствие возможности появления _у некоторых пользователей_ теста **CAPTCHA** при долговременном непрерывном использовании.

### Ограничения
Сайт выдает списки с объявлениями <ins>__лишь до 54 странцы включительно__</ins>. Это примерно _28 * 54 = 1512_ объявлений.
Поэтому, если имеется желание собрать как можно больше данных, то следует использовать более конкретные запросы (по количеству комнат). 

К примеру, вместо того, чтобы при использовании указывать _rooms=(1, 2)_, стоит два раза отдельно собирать данные с параметрами _rooms=1_ и _rooms=2_ соответственно.

Таким образом, максимальная разница может составить 1 к 6 (студия, 1, 2, 3, 4, 5 комнатные квартиры), то есть 1512 к 9072.

### Примечание
1. В некоторых объявлениях отсутсвуют данные по некоторым признакам (_год постройки, жилые кв метры, кв метры кухни итп_).
В этом случае проставляется значение ___-1___ либо ___пустая строка___ для числового и строкового типа поля соответственно.

2. Для отсутствия блокировки по __IP__ в данном проекте задана пауза (___в размере 4-5 секунд___) после сбора информации с
каждой отдельной взятой страницы.

3. Не рекомендутся производить несколько процессов сбора данных параллельно (одновременно) на одной машине (см. пункт 2).

4. Имеется флаг __with_extra_data__, при помощи которого можно дополнительно собирать некоторые данные, но при этом существенно (___в 5-10 раз___) замедляется процесс по времени, из-за необходимости заходить на каждую страницу с предложением. 
Соответствующие данные: ___площадь кухни, год постройки здания, тип дома, тип отделки, тип отопления, тип жилья___  и ___номер телефона___.

5. Данный парсер не будет работать в таком инструменте как [Google Colaboratory](https://colab.research.google.com/). 
См. [подробности](https://github.com/lenarsaitov/cianparser/issues/1)

6. Если в проекте не имеется подходящего локации (неожидаемое значение аргумента __location__) или иными словами его нет в списке **_cianparser.list_locations()_**, то прошу сообщить, буду рад добавить.
