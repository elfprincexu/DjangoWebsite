from django.utils.text import slugify
import random, string
import re
import datetime
import math
from django.utils.html import strip_tags



'''
random string_generator is located here:
'''

def random_string_generator(size = 6, chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_slug_generator(instance, new_slug= None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                    slug = slug,
                    randstr =random_string_generator(size=4)
        )
        return unique_slug_generator(instance, new_slug= new_slug)
    return slug


def count_words(html_string):

    # html_string = """
    #     <h1>this is a title</h1>
    # """

    words_string = strip_tags(html_string)
    matched_words = re.findall(r'\w+', words_string)
    count = len(matched_words)
    return count


def get_read_time(html_string):
    count = count_words(html_string)
    read_time_min = math.ceil(count/200.0) # assunming 200 words per minutes
    # read_time_sec = read_time_min * 60
    read_time = str(datetime.timedelta(minutes=read_time_min)) # 0:02:00
    return read_time









