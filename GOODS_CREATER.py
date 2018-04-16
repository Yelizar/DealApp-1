from suppliers.models import Goods
from access.models import UserProfile
from random import randrange
from shutil import copy
from DealApp.settings import BASE_DIR
import os
import USER_CREATER


class GoodsCreater(USER_CREATER.UserCreater):

    LIST_OF_GOODS_NAMES = ('Apple', 'Apricot', 'Avocado', 'Banana', 'Bilberry', 'Blackberry',
                           'Blackcurrant', 'Blueberry', 'Boysenberry', "Buddha's",
                           'Crab apples', 'Currant', 'Cherry', 'Cherimoya', 'Chico fruit',
                           'Cloudberry', 'Coconut', 'Cranberry', 'Cucumber', 'Custard apple',
                           'Damson', 'Date', 'Dragonfruit', 'Durian', 'Elderberry', 'Feijoa',
                           'Fig', 'Goji berry', 'Gooseberry', 'Grape', 'Raisin', 'Grapefruit',
                           'Guava', 'Honeyberry', 'Huckleberry', 'Jabuticaba', 'Jackfruit',
                           'Jambul', 'Jujube', 'Juniper berry', 'Kiwano', 'Kiwifruit', 'Kumquat',
                           'Lemon', 'Lime', 'Loquat', 'Longan', 'Lychee', 'Mango', 'Mangosteen',
                           'Marionberry', 'Melon', 'Cantaloupe', 'Honeydew', 'Watermelon',
                           'Miracle fruit', 'Mulberry', 'Nectarine', 'Nance', 'Olive', 'Orange',
                           'Blood orange', 'Clementine', 'Mandarine', 'Tangerine', 'Papaya',
                           'Passionfruit', 'Peach', 'Pear', 'Persimmon', 'Plantain', 'Plum',
                           'Prune (dried plum)', 'Pineapple', 'Plumcot (or Pluot)', 'Pomegranate',
                           'Pomelo', 'Purple mangosteen', 'Quince', 'Raspberry', 'Salmonberry',
                           'Rambutan', 'Redcurrant', 'Salal berry', 'Salak', 'Satsuma', 'Soursop',
                           'Star fruit', 'gonzoberry', 'Strawberry', 'Tamarillo', 'Tamarind',
                           'Ugli fruit', 'Yuzu')

    LIST_OF_DESCRIPTION = ('The waterfall at Skakavac is one of the most attractive sites in the vicinity of Sarajevo.',
                           'Hottie is a slang term for a physically attractive person.',
                           'A new study has revealed that bald men may actually be happier than men with hair.',
                           'Ethan is haunted by dreams of a beautiful girl he has never met.',
                           'A new study breaks down the foods most strongly associated with chubby children.',
                           "We must preserve Wisconsin's clean water, clean air, and natural heritage.",
                           'It was a dazzling diamond, and it impressed her enormously.',
                           'We saw sudden splashes of color in the drab landscape.',
                           'She had an elegant figure and she walked well.',
                           'The government welfare checks were used to buy fancy motorcycles and iphones.',
                           'There are two principal causes of flabby arms.',
                           'Glamorous shoes are perfect for finishing off evening ensembles in style.',
                           'She wore a gorgeous Victorian gown.',
                           "We're so proud of our splendid, handsome boy.",
                           'In this valley were magnificent gardens planted by Hassen ben Sabah.',
                           "We don't see many muscular women in popular culture.",
                           'White rabbits have large, broad, and muscular bodies.',
                           'The boss prefers his female employees to wear plain clothing to work.',
                           'When shopping, choose plump blueberries with no old, crushed berries.',
                           'The males had the most unusual colors and unsightly patterns.',
                           'Ashy skin is usually whitish or grayish in color.',
                           'She had black hair and eager blue eyes.',
                           'John noticed a green ribbon on a branch.',
                           'The girl had icy blue lips, similar to that of a corpse.',
                           'Lemon colored bridesmaid dresses brighten-up any wedding.',
                           'Her toenails shine with freshly applied, mango polish.',
                           'The wings and tail are brown with purple edgings.',
                           'The forewings are whitish with distinct red markings.',
                           'There are orange and yellow bands on the abdomen.',
                           'When his wife gave birth to a son, he was the proudest man alive .',
                           "We're hoping for better results tomorrow.",
                           'She was a very careful worker.',
                           'Gulliver was a clever young man, who loved to travel.',
                           'Perhaps this is a clever forgery to put us on the wrong scent.',
                           "It remains Winterhalter's most famous work.",
                           'He was a gifted pilot, a good fellow, and had both wit and humor in him.',
                           'As a gifted young woman, she excelled academically and exhibited leadership.',
                           'Of the three, she is perhaps the most gifted painter.',
                           'Standing on the hallowed precincts of the quarter-deck, they were careful not to speak.',
                           'Her work has made her an important role model.',
                           'Everyone was searching for an easy, inexpensive solution to the problem.',
                           'He abhors mushy bananas and mealy peaches.',
                           'Rambutan is an odd fruit that looks like a furry strawberry.',
                           'The poor peasants were forced to sell the young girls to the powerful communist party leaders.',
                           'The shy girls from the village had very little experience with men.',
                           'The village girls had tender skin which was very sensitive to the touch.',
                           'I saw the tender regard which he cast upon her.',
                           'Shahar claims to be uninterested in the theory of feminism.')

    LIST_OF_SUPPLIERS = UserProfile.objects.filter(user_type='supplier')

    LIST_OF_PICTURES = ('suppliers/goods/1.jpg', 'suppliers/goods/2.jpg', 'suppliers/goods/3.jpg',
                        'suppliers/goods/4.jpg', 'suppliers/goods/11.jpg', 'suppliers/goods/18.jpg',
                        'suppliers/goods/5.jpg', 'suppliers/goods/12.jpg', 'suppliers/goods/19.jpg',
                        'suppliers/goods/6.jpg', 'suppliers/goods/13.jpg', 'suppliers/goods/20.jpg',
                        'suppliers/goods/7.jpg', 'suppliers/goods/14.jpg', 'suppliers/goods/21.jpg',
                        'suppliers/goods/8.jpg', 'suppliers/goods/15.jpg', 'suppliers/goods/22.jpg',
                        'suppliers/goods/9.jpg', 'suppliers/goods/16.jpg', 'suppliers/goods/23.jpg',
                        'suppliers/goods/10.jpg', 'suppliers/goods/17.jpg', 'suppliers/goods/24.jpg',
                        'suppliers/goods/25.jpg', 'suppliers/goods/26.jpg',
                        )
    root = 'suppliers/username/goods/'

    def user_goods_directory_path(self, new_object, filename):
        try:
            os.makedirs(BASE_DIR + '/media/suppliers/'+str(new_object.supplier.username)+'/goods/')
        except FileExistsError:
            """"""
        file = copy(BASE_DIR+'/media/'+filename, BASE_DIR+'/media/suppliers/'+str(new_object.supplier.username)+'/goods/')
        return file

    def __init__(self):
        super(GoodsCreater, self).__init__(0)
        counter = 300
        while counter != 0:
            new_object = Goods()
            new_object.supplier = self.rdm_choice(self.LIST_OF_SUPPLIERS)
            new_object.name = self.rdm_choice(self.LIST_OF_GOODS_NAMES)
            new_object.price = randrange(0, 100)
            path = self.user_goods_directory_path(new_object, self.rdm_choice(self.LIST_OF_PICTURES))
            new_object.picture = path
            new_object.description = self.rdm_choice(self.LIST_OF_DESCRIPTION)
            new_object.save()
            print(new_object)
            counter -= 1