# Translate EPUB

Translate EPUB - это приложение для перевода электронных книг в формате EPUB. Оно позволяет пользователю переводить книги на различные языки, чтобы расширить доступ к контенту на неизвестных языках.

[![Python Version](https://img.shields.io/badge/python-3.10-brightgreen.svg)](https://python.org)
[![Flask Version](https://img.shields.io/badge/beautifulsoup4-4.11.1-brightgreen.svg)](https://djangoproject.com)


### Зависимости
Перед использованием приложения убедитесь, что у вас установлены следующие зависимости:

* lxml (версия 4.6.3 или выше)
* BeautifulSoup (версия 4.9.3 или выше)
* ebooklib (версия 0.17.1 или выше)
* googletrans (версия 4.0.0-rc1 или выше)

Установка зависимостей может быть выполнена с помощью pip:

```bash
pip install lxml
pip install beautifulsoup4
pip install ebooklib
pip install googletrans==4.0.0-rc1
```
### Использование
Импортируйте необходимые модули:
```python
import lxml.html as html
from bs4 import BeautifulSoup, NavigableString
from ebooklib import epub, utils
from googletrans import Translator
```

Импортируйте класс TranslateEpub из модуля:
```python
from translate_epub import TranslateEpub
```

Создайте экземпляр класса TranslateEpub, указав путь к файлу EPUB:
```python
book_epub = TranslateEpub('path/to/book.epub')
```

Получите элементы книги EPUB, которые нужно перевести:
```python
book_epub.get_items()
```

Переведите элементы книги и сохраните результат в новый файл EPUB:
```python
book_epub.cook_soup()
```

Запустите программу:
```python
if __name__ == '__main__':
    book_epub = TranslateEpub('path/to/book.epub')
    book_epub.get_items()
    book_epub.cook_soup()
```

Примечание: Приложение будет переводить текст элементов книги с помощью сервиса _Google Translate_ на русский язык. Вы можете изменить целевой язык, изменив значение `dest` в методе `__translation_func` класса `TranslateEpub`.

### Лицензия
Это приложение распространяется под лицензией MIT. Подробности смотрите в файле LICENSE.

