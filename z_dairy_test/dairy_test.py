import  re
text = """
I have a dream that my four little children will one day live in a nation where they will not be judged by the color of their skin but by the content of their character. I have a dream today.

I have a dream that one day down in Alabama, with its vicious racists, . . . one day right there in Alabama little black boys and black girls will be able to join hands with little white boys and white girls as sisters and brothers. I have a dream today.

I have a dream that one day every valley shall be exalted, every hill and mountain shall be made low, the rough places will be made plain, and the crooked places will be made straight, and the glory of the Lord shall be revealed, and all flesh shall see it together.

This is our hope. . . With this faith we will be able to hew out of the mountain of despair a stone of hope. With this faith we will be able to transform the jangling discords of our nation into a beautiful symphony of brotherhood. With this faith we will be able to work together, to pray together, to struggle together, to go to jail together, to stand up for freedom together, knowing that we will be free one day. . . .

And when this happens, and when we allow freedom ring, when we let it ring from every village and every hamlet, from every state and every city, we will be able to speed up that day when all of God's children, black men and white men, Jews and Gentiles, Protestants and Catholics, will be able to join hands and sing in the words of the old Negro spiritual: "Free at last! Free at last! Thank God Almighty, we are free at last!"
  """

"""
1.读取文件；
2.去除所有标点符号和换行符，并把所有大写变成小写；
3.合并相同的词，统计每个词出现的频率，并按照词频从大到小排序；
4.将结果按行输出到文件 out.txt。
"""

def parse(text):
    # 去除标点符号和换行符
    text = re.sub('[^\w]',' ',text)

    # 转成小写
    text = text.lower()

    word_list = text.split(' ')

    word_list = filter(None,word_list)

    word_cnt = {}
    for word in word_list:
        if word not in word_cnt:
            word_cnt[word] = 0
        word_cnt[word] += 1
    print(word_cnt)

    sorted_word_cnt = sorted(word_cnt.items(),key=lambda kv:kv[1],reverse=True)

    print(sorted_word_cnt)
    return sorted_word_cnt

'''
每次从家里向 Dropbox 网盘写入不超过 5GB 的数据，而公司电脑一旦侦测到新数据，就立即拷贝到本地，然后删除网盘上的数据。
等家里电脑侦测到本次数据全部传入公司电脑后，再进行下一次写入，直到所有数据都传输过去。
根据这个想法，你计划在家写一个 server.py，在公司写一个 client.py 来实现这个需求。
提示：我们假设每个文件都不超过 5GB。你可以通过写入一个控制文件（config.json）来同步状态。
不过，要小心设计状态，这里有可能产生 race condition。
你也可以通过直接侦测文件是否产生，或者是否被删除来同步状态，这是最简单的做法。
'''

# parse(text)
l = [(2,3),(5,2)]
s = [a-b if a>b else a+b for a,b in l]
'''
将文件中逐行读取的一个完整语句，按逗号分割单词，去掉首位的空字符，并过滤掉长度小于等于 3 的单词，最后返回由单词组成的列表。
'''
t = ' Today ,is ,Sunday!'
t2 = [s.strip() for s in t.split(",") if len(s.strip())>3]
# print(t2)

list = [1,5,7,4,2,90,50,34]
r = [value for index,value in enumerate(list) if index>=5]
# print(r)


attributes = ['name', 'dob', 'gender']
values = [['jason', '2000-01-01', 'male'], ['mike', '1999-01-01', 'male'],['nancy', '2001-02-01', 'female']]

v_l = []
for data in values:
    v_l.append((dict(zip(attributes,data))))
# print(v_l)

v_2 = [dict(zip(attributes,v)) for v in values]
# print(v_2)

# expected output:
# [{'name': 'jason', 'dob': '2000-01-01', 'gender': 'male'},
# {'name': 'mike', 'dob': '1999-01-01', 'gender': 'male'},
# {'name': 'nancy', 'dob': '2001-02-01', 'gender': 'female'}]
a=1
b=9

def add():
    a = 0
    a += 1

def en(mi):
    def num(base):
        return base ** mi
    return num

# ra = en(3)
# print(ra(3))




s = [(lambda x: x*x)(x) for x in range(10)]
s1 = [(lambda x:x**x) (x) for x in range(10)]
# print(s1)


d = {'mike': 10, 'lucy': 2, 'ben': 30}
d1 = sorted(d.items(),key=lambda x:x[1])
# print(d1)


class Entity():
    def __init__(self, object_type):
        print('parent class init called')
        self.object_type = object_type

    def get_context_length(self):
        raise Exception('get_context_length not implemented')

    def print_title(self):
        print(self.title)


class Document(Entity):
    def __init__(self, title, author, context):
        print('Document class init called')
        Entity.__init__(self, 'document')
        self.title = title
        self.author = author
        self.__context = context

    def get_context_length(self):
        return len(self.__context)


class Video(Entity):
    def __init__(self, title, author, video_length):
        print('Video class init called')
        Entity.__init__(self, 'video')
        self.title = title
        self.author = author
        self.__video_length = video_length

    def get_context_length(self):
        return self.__video_length


# harry_potter_book = Document('Harry Potter(Book)', 'J. K. Rowling',
#                              '... Forever Do not believe any thing is capable of thinking independently ...')
# harry_potter_movie = Video('Harry Potter(Movie)', 'J. K. Rowling', 120)

# print(harry_potter_book.object_type)
# print(harry_potter_movie.object_type)

# harry_potter_book.print_title()
# harry_potter_movie.print_title()

# print(harry_potter_book.get_context_length())
# print(harry_potter_movie.get_context_length())


class SearchEngineBase(object):
    def __init__(self):
        pass

    def add_corpus(self, file_path):
        with open(file_path, 'r') as fin:
            text = fin.read()
        self.process_corpus(file_path, text)

    def process_corpus(self, id, text):
        raise Exception('process_corpus not implemented.')

    def search(self, query):
        raise Exception('search not implemented.')

def main(search_engine):
    for file_path in ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt']:
        search_engine.add_corpus(file_path)

    while True:
        query = input()
        results = search_engine.search(query)
        print('found {} result(s):'.format(len(results)))
        for result in results:
            print(result)

class SimpleEngine(SearchEngineBase):
    def __init__(self):
        super(SimpleEngine, self).__init__()
        self.__id_to_texts = {}

    def process_corpus(self, id, text):
        self.__id_to_texts[id] = text

    def search(self, query):
        results = []
        for id, text in self.__id_to_texts.items():
            if query in text:
                results.append(id)
        return results

# search_engine = SimpleEngine()
# main(search_engine)


import copy
x = [1]
x.append(x)
# print(x)
# print(len(x))
# print(id(x))

y = copy.deepcopy(x)
# print(print)
# print(id(y))

# 以下命令的输出是？
# print(x == y)


l1 = [1, 2, 3]
l2 = [1, 2, 3]
l3 = l2
# print(l1 is l2)
# print(id(l1))
# print(id(l2))
# print(l2 is l3)


a = 1
b = 1
c = b
# print(a is b)
# print(b is c)


def func(a,b):
    a = 10
    b = 20

# a = 1
# b = 2
# func(a,b)
# print(a,b)

def my_decorator(func):
    def wrapper():
        print("wrapper of decorator")
        func()
    return wrapper

@my_decorator
def greet():
    print('hello world')


# greet()
# class Myclass:
#     data = 1
#
# instance = Myclass()

# Myclass = type('Myclass',(),{'data':1})
# instance = Myclass()
#
# print(Myclass())
# print(instance.data)


#
# class Mymeta(type):
#     def __init__(self, name, bases, dic):
#         super().__init__(name, bases, dic)
#         print('===>Mymeta.__init__')
#         print(self.__name__)
#         print(dic)
#         print(self.yaml_tag)
#
#     def __new__(cls, *args, **kwargs):
#         print('===>Mymeta.__new__')
#         print(cls.__name__)
#         return type.__new__(cls, *args, **kwargs)
#
#     def __call__(cls, *args, **kwargs):
#         print('===>Mymeta.__call__')
#         obj = cls.__new__(cls)
#         cls.__init__(cls, *args, **kwargs)
#         return obj
#
#
# class Foo(metaclass=Mymeta):
#     yaml_tag = '!Foo'
#
#     def __init__(self, name):
#         print('Foo.__init__')
#         self.name = name
#
#     def __new__(cls, *args, **kwargs):
#         print('Foo.__new__')
#         return object.__new__(cls)


# foo = Foo('foo')

#1+2+3+...+n的平方等于1的立方加上2的立方直到n的立方

# def generator(k):
#     i = 1
#     while True:
#         yield i ** k
#         i += 1
#
# gene_1 = generator(1)
# gene_3 = generator(3)
#
# def sum(n):
#     sum0,sum3 = 0,0
#     for i in range(n):
#         sum0 += next(gene_1)
#         sum3 += next(gene_3)
#
#     sum0 = sum0*sum0
#     print(sum0,sum3)
#
# sum(10)

#判断字符串是否为另一个字符串的子字符串
#"ace"是"abcde"的一个子序列，而"aec"不是

str1 = 'abcde'
subs = 'aec'

def sub_s(s1,s2):
    for i in s2:
        j = 0
        while j<len(s1):
            if s1[j] == i:
                s1 = s1[j:]
            j += 1

    print("true")

sub_s(str1,subs)






































