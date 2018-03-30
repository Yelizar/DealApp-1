"""will be deleted"""
from access.models import UserProfile
from random import choice


class UserCreater:

    LIST_OF_MANS_NAMES = ['Noah', 'Liam', 'Mason', 'Jacob', 'William', 'Ethan', 'James', 'Alexander',
                          'Michael', 'Benjamin', 'Elijah', 'Daniel', 'Aiden', 'Logan', 'Matthew', 'Lucas',
                          'Jackson', 'David', 'Oliver', 'Jayden', 'Joseph', 'Gabriel', 'Samuel', 'Carter',
                          'Anthony', 'John', 'Dylan', 'Luke', 'Henry', 'Andrew', 'Isaac', 'Christopher',
                          'Joshua', 'Wyatt', 'Sebastian', 'Owen', 'Caleb', 'Nathan', 'Ryan', 'Jack', 'Hunter',
                          'Levi', 'Christian', 'Jaxon', 'Julian', 'Landon', 'Grayson', 'Jonathan', 'Isaiah',
                          'Charles', 'Thomas', 'Aaron', 'Eli', 'Connor', 'Jeremiah', 'Cameron', 'Josiah',
                          'Adrian', 'Colton', 'Jordan', 'Brayden', 'Nicholas', 'Robert', 'Angel', 'Hudson',
                          'Lincoln', 'Evan', 'Dominic', 'Austin', 'Gavin', 'Nolan', 'Parker', 'Adam', 'Chase',
                          'Jace', 'Ian', 'Cooper', 'Easton', 'Kevin', 'Jose', 'Tyler', 'Brandon', 'Asher',
                          'Jaxson', 'Mateo', 'Jason', 'Ayden', 'Zachary', 'Carson', 'Xavier', 'Leo', 'Ezra',
                          'Bentley', 'Sawyer', 'Kayden', 'Blake', 'NathanielNoah']

    LIST_OF_GIRLS_NAMES = ['Emma', 'Olivia', 'Sophia', 'Ava', 'Isabella', 'Mia', 'Abigail', 'Emily',
                           'Charlotte', 'Harper', 'Madison', 'Amelia', 'Elizabeth', 'Sofia', 'Evelyn',
                           'Avery', 'Chloe', 'Ella', 'Grace', 'Victoria', 'Aubrey', 'Scarlett', 'Zoey',
                           'Addison', 'Lily', 'Lillian', 'Natalie', 'Hannah', 'Aria', 'Layla', 'Brooklyn',
                           'Alexa', 'Zoe', 'Penelope', 'Riley', 'Leah', 'Audrey', 'Savannah', 'Allison',
                           'Samantha', 'Nora', 'Skylar', 'Camila', 'Anna', 'Paisley', 'Ariana', 'Ellie',
                           'Aaliyah', 'Claire', 'Violet', 'Stella', 'Sadie', 'Mila', 'Gabriella', 'Lucy',
                           'Arianna', 'Kennedy', 'Sarah', 'Madelyn', 'Eleanor', 'Kaylee', 'Caroline',
                           'Hazel', 'Hailey', 'Genesis', 'Kylie', 'Autumn', 'Piper', 'Maya', 'Nevaeh',
                           'Serenity', 'Peyton', 'Mackenzie', 'Bella', 'Eva', 'Taylor', 'Naomi', 'Aubree',
                           'Aurora', 'Melanie', 'Lydia', 'Brianna', 'Ruby', 'Katherine', 'Ashley', 'Alexis',
                           'Alice', 'Cora', 'Julia', 'Madeline', 'Faith', 'Annabelle', 'Alyssa', 'Isabelle',
                           'Vivian', 'Gianna']

    USER_TYPE = ['buyer', 'supplier']

    EMAIL_TYPE = ['@gmail.com', '@mail.ru', '@yahoo.com', '@yandex.ru', '@tut.by']

    GENDER = [LIST_OF_GIRLS_NAMES, LIST_OF_MANS_NAMES]

    def __init__(self, counter):
        self.counter = counter
        self.creater()

    def creater(self):
        while self.counter != 0:
            new_object = UserProfile()
            new_object.username = choice(self.rdm_choice(self.GENDER))
            if new_object.username in self.LIST_OF_MANS_NAMES:
                self.LIST_OF_MANS_NAMES.remove(new_object.username)
            else:
                self.LIST_OF_GIRLS_NAMES.remove(new_object.username)
            new_object.email = new_object.username+self.rdm_choice(self.EMAIL_TYPE)
            new_object.user_type = self.rdm_choice(self.USER_TYPE)
            if new_object.user_type == 'buyer':
                new_object.photo = 'access/profile_photo/default-ava.png'
            else:
                new_object.photo = 'access/profile_photo/avatar-s.png'
            new_object.set_password('1234qwer')
            new_object.save()
            print(new_object)
            self.counter -= 1

    def rdm_choice(self, x):
        rdm = choice(x)
        return rdm
