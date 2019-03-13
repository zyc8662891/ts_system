import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "untitled.settings")
django.setup()

from appo.models import *

detail = AuthorDetail.objects.create(age=20, telephone=13333334444, info="Owen简介")
author = Author.objects.create(name='Owen', author_detail=detail)
detail = AuthorDetail.objects.create(age=19, telephone=14356789900, info="Zero简介")
author = Author.objects.create(name='Zero', author_detail=detail)
detail = AuthorDetail.objects.create(age=20, telephone=16678906677, info="Egon简介")
author = Author.objects.create(name='Egon', author_detail=detail)
detail = AuthorDetail.objects.create(age=21, telephone=18900123456, info="Lxx简介")
author = Author.objects.create(name='Lxx', author_detail=detail)
detail = AuthorDetail.objects.create(age=17, telephone=16875435678, info="Yhh简介")
author = Author.objects.create(name='Yhh', author_detail=detail)

Publish.objects.create(name="老男孩出版社", address="上海浦东")
Publish.objects.create(name="小女孩出版社", address="上海虹桥")
Publish.objects.create(name="金沙江出版社", address="北京朝阳")

Book.objects.create(name='西游记', price=33.33, publish_date='2018-1-1', publish_id=3)
Book.objects.create(name='东游记', price=33.33, publish_date='2018-2-2', publish_id=3)
Book.objects.create(name='爱丽莎', price=55.55, publish_date='2018-3-3', publish_id=2)
Book.objects.create(name='古都佑', price=66.55, publish_date='2019-2-2', publish_id=2)
Book.objects.create(name='拍死你', price=88.88, publish_date='2016-6-6', publish_id=1)
Book.objects.create(name='妮妞斯', price=48.99, publish_date='2018-6-6', publish_id=1)

Book.objects.all()[0].author.add(1, 2)
Book.objects.all()[1].author.add(1, 2, 5)
Book.objects.all()[2].author.add(4)
Book.objects.all()[3].author.add(4)
Book.objects.all()[4].author.add(1, 3, 4)
Book.objects.all()[5].author.add(4, 5)