# Есть некоторый общий класс родитель Tag, который хранит в себе какой-то HTML тег (например: <tag></tag>).
# От Tag наследуются еще четыре класса Image, Input, Text (т. е <p></p>), Link (т. е <a></a>).
# С использованием указанных паттернов реализовать следующее поведение:
# Должна быть возможность создать необходимый тег, явно его не создавая, т. е не через img = Image(),
# а через фабричный метод или фабрику, например factory.create_tag(name).
class Tag:
    tag_name = "tag"

    def get_html(self, *options):
        """
        Функция возвращает соответствующий тег.
        Принимает параметры, присоединяемые к тегу.
        Функция съест любой параметр, конкретный выбор за пользователем.
        """
        return "<{0}{1}></{0}>".format(self.tag_name, (" " if options else "") + "".join(options))


class Image(Tag):
    tag_name = "img"


class Input(Tag):
    tag_name = "input"


class Text(Tag):
    tag_name = "p"


class Link(Tag):
    tag_name = "a"


class TagFactory:
    tags = {"image": Image, "input": Input, "p": Text, "a": Link, "": Tag}

    def create_tag(self, name):
        tag_to_create = self.tags.get(name)
        if tag_to_create:
            return tag_to_create()
        else:
            raise ValueError(name)


if __name__ == "__main__":
    factory = TagFactory()
    elements = ["image", "input", "p", "a", "", 34, "ham"]

    for el in elements:
        try:
            print(factory.create_tag(el).get_html("class="))
            print(factory.create_tag(el).get_html())
        except ValueError as ve:
            print("Недопустимый тег: {}".format(ve))
