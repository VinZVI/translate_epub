import lxml.html as html
from bs4 import BeautifulSoup, NavigableString
from ebooklib import epub, utils
from googletrans import Translator


class TranslateEpub:
    """
        Класс TranslateEpub принимает путь до файла с расширением epub,
        возвращает переведенный документ с расширением epub.

        Variables:
            tag_exeption (list[str]):

        Attributes:
            epub_path (str): Путь до файла с расширением epub.
    """
    tag_exeption = ["code", 'a', 'strong', 'pre', 'span', 'html',
                    'body', "head", "em", "b", "i"]

    def __init__(self, epub_path: str):

        self.book = epub.read_epub(epub_path)
        self.items_array = []


    @staticmethod
    def __translation_func(text):
        translator = Translator()
        result = translator.translate(text, dest='ru')
        return result.text

    def get_items(self, print_items=False, el_numbers: list[int] = [4, 9]) -> list:
        """
        Функция get_items получает экземпляр класса epub,
        возвращает элементы книги epub.
        Вот список текущих типов элементов, которые вы можете использовать:
            0 - ITEM_UNKNOWN
            1 - ITEM_IMAGE
            2 - ITEM_STYLE
            3 - ITEM_SCRIPT
            4 - ITEM_NAVIGATION
            5 - ITEM_VECTOR
            6 - ITEM_FONT
            7 - ITEM_VIDEO
            8 - ITEM_AUDIO
            9 - ITEM_DOCUMENT
            10 - ITEM_COVER
            11 - ITEM_SMIL

        Variables:
            print_items (bool): True - напечатать все существующие в книге элементы,
                                False - получить результат без печати.
            el_numbers list[int]: Принимает список с номерами элементов книги
        """

        for item in self.book.get_items():
            if print_items:
                print('NAME : ', item.get_name())
                print('----------------------------------')
                print('ID : ', item.get_id())
                print('----------------------------------')
                print('ITEM : ', item.get_type())
                print('----------------------------------')
            if item.get_type() in el_numbers:
                self.items_array.append(item)

    def cook_soup(self, name_book: str = 'translated_book'):
        """
        Функция cook_soup получает элементы книги epub,
        переводит их и сохраняет в книгу формата epub.
        """
        for item in self.items_array:
            soup = BeautifulSoup(item.get_content(), features="xml")
            self.__child_translate(soup)
            item.set_content(soup.encode())
            print('==================================')
            print('Глава переведена.')
            self.__open_in_browser(item)
        epub.write_epub(f'{name_book}.epub', self.book, {})

    def __child_translate(self, soup):
        count = 0
        for child in soup.descendants:
            if child.name:

                if child.string and child.name not in TranslateEpub.tag_exeption:
                    if child.parent.name == 'code':
                        continue
                    tag_text_before = child.string
                    translation_text = self.__translation_func(tag_text_before)
                    child.string = translation_text
                    count += 1
                    print('->>', count)

                elif child.name not in TranslateEpub.tag_exeption:
                    new_contents = []
                    for content in child.contents:
                        if content.string and content.string not in ['\n', ' '] and not content.name and content.name not in TranslateEpub.tag_exeption:
                            content = NavigableString(self.__translation_func(content.string))
                        new_contents.append(content)
                        new_contents.append(" ")
                    child.clear()
                    child.extend(new_contents)
                    count += 1
                    print('->>', count)

    def __open_in_browser(self, item):
        contents = utils.parse_string(item.get_content())
        html.open_in_browser(contents)


if __name__ == '__main__':
    book_epub = TranslateEpub('Flask By Example рестр.epub')
    book_epub.get_items()
    book_epub.cook_soup()
