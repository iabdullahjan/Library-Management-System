import unittest

books = []


def add_book(title):

    if title != "":
        books.append(title)
        return True

    return False


def search_book(title):

    return title in books


def delete_book(title):

    if title in books:
        books.remove(title)
        return True

    return False


class TestLibrarySystem(unittest.TestCase):

    def test_add_book(self):

        result = add_book("Python")
        self.assertTrue(result)

    def test_empty_book(self):

        result = add_book("")
        self.assertFalse(result)

    def test_search_book(self):

        add_book("Java")
        result = search_book("Java")
        self.assertTrue(result)

    def test_delete_book(self):

        add_book("C++")
        result = delete_book("C++")
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()