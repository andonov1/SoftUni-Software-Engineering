class Cat:
    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')
        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')
        self.sleepy = False


from unittest import TestCase, main


class CatTests(TestCase):
    def test_cat_size_is_correct_after_eating(self):
        cat = Cat('Test cat')

        cat.eat()
        self.assertEqual(1, cat.size)

    def test_cat_is_fed_after_eating(self):
        cat = Cat('Test cat')

        cat.eat()
        self.assertTrue(cat.fed)

    def test_cat_cannot_eat_already_fed_raise(self):
        cat = Cat('Test cat')
        cat.eat()

        with self.assertRaises(Exception) as ex:
            cat.eat()
        self.assertEqual('Already fed.', str(ex.exception))

    def test_cat_cannot_sleep_if_not_fed_raise(self):
        cat = Cat('Test cat')

        with self.assertRaises(Exception) as ex:
            cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_cat_is_not_sleepy_after_sleep(self):
        cat = Cat('Test cat')
        cat.eat()
        cat.sleep()

        self.assertFalse(cat.sleepy)


if __name__ == '__main__':
    main()