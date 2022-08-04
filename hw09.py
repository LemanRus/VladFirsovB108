# Есть некоторый общий класс родитель Tag, который хранит в себе какой-то HTML тег (например: <tag></tag>).
# От Tag наследуются еще четыре класса Image, Input, Text (т. е <p></p>), Link (т. е <a></a>).
# С использованием указанных паттернов реализовать следующее поведение:
# Должна быть возможность создать необходимый тег, явно его не создавая, т. е не через img = Image(),
# а через фабричный метод или фабрику, например factory.create_tag(name).
class Tag:
    def get_html(self, *options):
        """
        Функция возвращает соответствующий тег.
        Принимает параметры, присоединяемые к тегу.
        Функция съест любой параметр, конкретный выбор за пользователем.
        """
        if options:
            return f"<tag {' '.join(options)}></tag>"


class Image(Tag):
    def get_html(self, *options):
        if options:
            return f"<img {' '.join(options)}></img>"


class Input(Tag):
    def get_html(self, *options):
        if options:
            return f"<input {' '.join(options)}></input>"


class Text(Tag):
    def get_html(self, *options):
        if options:
            return f"<p {' '.join(options)}></p>"


class Link(Tag):
    def get_html(self, *options):
        if options:
            return f"<a {' '.join(options)}></a>"


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
        except ValueError as ve:
            print("Недопустимый тег: {}".format(ve))
