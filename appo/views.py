from django.shortcuts import render,reverse,redirect,HttpResponse
from django .views import View
from appo.models import User,Book,Publish,Author,AuthorDetail
from django.core.paginator import Paginator
# Create your views here.
def login_check(func):
    def inner(request,*args,**kwargs):
        is_login = request.COOKIES.get('is_login',None)
        url = request.get_full_path()
        print(url)
        if is_login:
            return func(request,*args,**kwargs)
        return redirect('/show_login/?return_url=%s' %url)
    return inner

def logout(request):
    #将登录状态的cookie清除
    response = redirect('/')
    response.delete_cookie('usr')
    response.delete_cookie('is_login')
    return response






def home(request):
    return render(request,'index.html')

def show_login(request):
    if request.method == 'GET':
        title = "登录"
        header = "登 录 窗 口"
        return render(request,'show_login.html',locals())
    if request.method == 'POST':
        usr = request.POST.get('usr',None)
        pwd = request.POST.get('pwd',None)
        anniu = request.POST.get('anniu',None)
        print(usr,pwd,anniu)

        user = User.objects.filter(usr=usr,pwd=pwd).first()
        if user:
            print('登录成功')
            #在cookie中保存登录信息
            return_url = request.GET.get('return_url', '/show_book')
            print(return_url)
            response = redirect(return_url)
            response.set_cookie('usr',usr) #当前登录用户
            response.set_cookie('is_login',True)
            return response
        else:
            print('登录失败')
            url = reverse('show_login')
            return redirect(url)
@login_check
def show_author(request):
    title = "作者详情"
    header = "图书管理系统"
    author_list = Author.objects.all()
    return render(request, 'show_author.html', locals())
@login_check
def show_book(request):
    title = "图书详情"
    header = "图书管理系统"
    book_list = Book.objects.all()
    paginator = Paginator(book_list,3)
    #对象总个数
    count = paginator.count
    #总分页数
    num_pages = paginator.num_pages
    #页码列表(可迭代对象)
    page_range = paginator.page_range
    current_num = int(request.GET.get('page',1))
    if current_num < 1:
        current_num = 1
        return redirect('/show_book/?page=%s' % current_num)
    elif current_num > num_pages:
        current_num = num_pages
        return redirect('/show_book/?page=%s' %current_num)
    current_page = paginator.page(current_num)
    #通过page_range来控制页面版面
    if current_num < 4:
        page_range = range(2,5)
    elif current_num > num_pages -3:
        page_range = range(num_pages-3,num_pages)
    else:
        page_range = range(current_num-1,current_num+2)
    return render(request, 'show_book.html',locals())



@login_check
def show_publish(request):
    title = "出版社详情"
    header = "图书管理系统"
    publish_list = Publish.objects.all()
    return render(request,'show_publish.html',locals())


@login_check
def update_book(request):
    title = "编辑图书"
    header="编辑图书"
    if request.method == 'GET':
        book_id = request.GET.get('id',None)
        publish_list = Publish.objects.all()
        author_list = Author.objects.all()
        book = Book.objects.filter(pk=book_id).first()
        return render(request,'update_book.html',locals())
    if request.method == 'POST':
        book_id = request.POST.get('book_id',None)
        name = request.POST.get('name',None)
        price = request.POST.get('price',None)
        publish_date = request.POST.get('publish_date',None)
        publish_id = request.POST.get('publish_id',None)
        author_ids = request.POST.getlist('author_ids',None)

        book_query = Book.objects.filter(pk=book_id)
        book_query.update(name=name,price=price,publish_date=publish_date,publish_id = publish_id)
        book_query.first().author.set(author_ids)
        return  redirect(reverse('show_book'))
@login_check
def update_author(request):
    title = '编辑作者'
    header = "编辑作者"
    if request.method == 'GET':
        author_id = request.GET.get('id',None)
        book_list = Book.objects.all()
        author = Author.objects.filter(pk=author_id).first()
        return render(request,'update_author.html',locals())
    if request.method == 'POST':
        author_id = request.POST.get('author_id',None)
        name = request.POST.get('name',None)
        age = request.POST.get('age',None)
        telephone = request.POST.get('telephone',None)
        info = request.POST.get('info',None)
        book_ids = request.POST.getlist('book_ids',None)

        author_query = Author.objects.filter(pk=author_id)
        author_detail_query = AuthorDetail.objects.filter(pk=author_id)
        author_query.update(name=name)
        author_detail_query.update(age=age,telephone=telephone,info=info)
        author_query.first().book_set.set(book_ids)
        return  redirect(reverse('show_author'))

@login_check
def update_publish(request):
    title = "编辑出版社"
    header = "编辑出版社"
    if request.method == 'GET':
        publish_id = request.GET.get('id',None)
        book_list = Book.objects.all()
        publish = Publish.objects.filter(pk=publish_id).first()
        return render(request,'update_publish.html',locals())
    if request.method == 'POST':
        publish_id = request.POST.get('publish_id',None)
        name = request.POST.get('name',None)
        address = request.POST.get('address',None)
        book_ids = request.POST.getlist('book_ids',None)

        publish_query = Publish.objects.filter(pk=publish_id)
        publish_query.update(name=name,address=address)
        print(publish_query.first().book_set.all())
        publish_query.first().book_set.all().update(publish_id=None)
        for id in book_ids:
            book = Book.objects.filter(pk=id)
            book.update(publish_id=publish_id)
            book_list = Book.objects.all()
        return  redirect(reverse('show_publish'))

@login_check
def add_book(request):
    title = '新增图书'
    header = '新增图书'
    if request.method == 'GET':
        book_id = request.GET.get('id', None)
        publish_list = Publish.objects.all()
        author_list = Author.objects.all()
        book = Book.objects.filter(pk=book_id).first()
        return render(request, 'update_book.html', locals())
    if request.method == 'POST':
        name = request.POST.get('name', None)
        price = request.POST.get('price', None)
        publish_date = request.POST.get('publish_date', None)
        publish_id = request.POST.get('publish_id', None)
        author_ids = request.POST.getlist('author_ids', None)
        book = Book.objects.create(name=name, price=price, publish_date=publish_date, publish_id=publish_id)
        book.author.add(*author_ids)
        return redirect(reverse('show_book'))
@login_check
def add_author(request):
    title = "新增作者"
    header = "新增作者"
    if request.method == 'GET':
        # author_id = request.GET.get('id', None)
        book_list = Book.objects.all()
        # author = Author.objects.filter(pk=author_id).first()
        return render(request, 'add_author.html', locals())
    if request.method == 'POST':
        # author_id = request.POST.get('author_id', None)
        name = request.POST.get('name', None)
        age = request.POST.get('age', None)
        telephone = request.POST.get('telephone', None)
        info = request.POST.get('info', None)
        auther_detail = AuthorDetail.objects.create(age=age,telephone=telephone,info=info)
        author = Author.objects.create(name=name,author_detail=auther_detail)
        book_ids = request.POST.getlist('book_ids', None)
        author.book_set.add(*book_ids)
        return redirect(reverse('show_author'))
@login_check
def add_publish(request):
    title = "新增出版社"
    header = "新增出版社"
    if request.method == 'GET':
        publish_id = request.GET.get('id', None)
        book_list = Book.objects.all()
        publish = Publish.objects.filter(pk=publish_id).first()
        return render(request, 'update_publish.html', locals())
    if request.method == 'POST':
        publish_id = request.POST.get('publish_id', None)
        name = request.POST.get('name', None)
        address = request.POST.get('address', None)
        book_ids = request.POST.getlist('book_ids', None)

        # publish_query = Publish.objects.filter(pk=publish_id)
        publish=Publish.objects.create(name=name, address=address)
        for id in book_ids:
            book = Book.objects.filter(pk=id)
            book.update(publish_id=publish.id)
            book_list = Book.objects.all()
        return redirect(reverse('show_publish'))

@login_check
def delete_book(request,book_id):
    print(book_id)
    Book.objects.filter(pk=book_id).delete()
    return HttpResponse('删除成功')
@login_check
def delete_author(request,author_id):
    print(author_id)
    Author.objects.filter(pk=author_id).delete()
    return HttpResponse('删除成功')
@login_check
def delete_publish(requeset,publish_id):
    print(publish_id)
    Publish.objects.filter(pk=publish_id).delete()
    return HttpResponse('删除成功')

def add_session(request):
    request.session['usr'] = 'abc'
    request.session['is_login'] = False
    request.session['test'] = 123
    print(request.session.session_key)
    res = request.session.exists(request.session.session_key)
    print(res)
    return HttpResponse('add success')

def get_session(request):
    usr = request.session.get('usr',None)
    is_login = request.session.get('te')



