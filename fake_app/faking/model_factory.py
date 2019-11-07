import factory

from . import models


class ActorFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Author

    name = factory.Faker("name")
    age = factory.Faker("random_int", max=100)


class PublisherFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Publisher

    name = factory.Faker("company")


class BookFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Book

    name = factory.Faker("sentence", nb_words=3)
    pages = factory.Faker("random_int", min=1, max=1000)
    price = factory.Faker("random_int", max=200)
    rating = factory.Faker("random_int", min=1, max=10)
    pubdate = factory.Faker("date")
    publisher = factory.SubFactory(PublisherFactory)

    @factory.post_generation
    def authors(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for author in extracted:
                self.authors.add(author)


class StoreFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Store

    name = factory.Faker("company")

    @factory.post_generation
    def books(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for book in extracted:
                self.books.add(book)


def fake_batch(size: int) -> None:
    for f in (
        ActorFactory,
        PublisherFactory,
        BookFactory,
        StoreFactory,
    ):
        f.create_batch(size)
