from bs4 import BeautifulSoup, NavigableString
from ebooklib import epub
from googletrans import Translator


def open_epub():
    tag_exeption = ["code", 'a', 'strong', 'pre', 'span', 'html',
                    'body', "head", "em", "b", "i"]
    class_exeption = ['calibre1']
    book = epub.read_epub('Flask By Example рестр.epub')
    for item in book.get_items():
        if item.get_type() in [4, 9]:
            print('NAME : ', item.get_name())
            print('----------------------------------')
            print('ID : ', item.get_id())
            print('----------------------------------')
            print('ITEM : ', item.get_type())

            soup = BeautifulSoup(item.get_content(), features="xml")
            count = 0
            total_string = len(list(soup.descendants))

            for child in soup.descendants:
                if child.name not in tag_exeption and child.name and child.string:
                    if child.parent.name == 'code':
                        continue
                    tag_text_before = child.string
                    translation_text = translation_func(tag_text_before)
                    child.string = translation_text
                    count += 1
                    print(total_string, '->>', count)
                elif child.name not in tag_exeption and child.name:
                    new_contents = []

                    for content in child.contents:
                        if content.string and content.string not in ['\n', ' '] and not content.name and content.name not in tag_exeption:
                            content = NavigableString(translation_func(content.string))
                        new_contents.append(content)
                        new_contents.append(" ")
                    child.clear()
                    child.extend(new_contents)
                    count += 1
                    print(total_string, '->>', count)
            item.set_content(soup.encode())
            # contents = utils.parse_string(item.get_content())
            # html.open_in_browser(contents)
            print('==================================')
    epub.write_epub('Flask By Example_ru.epub', book, {})

def translation_func(text):
    translator = Translator()
    result = translator.translate(text, dest='ru')
    return result.text

def main():
    open_epub()

if __name__ == "__main__":
    main()