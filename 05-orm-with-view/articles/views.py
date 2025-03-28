from django.shortcuts import render, redirect
from .models import Article


# 메인 페이지를 응답하는 함수 (+ 전체 게시글 목록)
def index(request):
    # DB에 전체 게시글 요청 후 가져오기
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

# 특정 단일 게시글의 상세 페이지를 응답(+단일 게시글 조회회)
def detail(request, pk):        # urls에서 사용한 변수명과 동일해야한다.(pk)
    
    # pk로 들어온 정수 값을 활용 해 DB에 id가 pk인 게시글을 조회 요청
    article = Article.objects.get(pk=pk)      # 왼쪽의 pk는 DB의 id값. 오른쪽의 pk는 변수명(바꿀수 있다.)
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)

# 게시글을 작성하기 위한 페이지를 제공하는 함수
def new(request):
    return render(request, 'articles/new.html')

# 사용자로부터 데이터를 받아 저장하고 저장이 완료되었다는 페이지를 제공하는 함수
def create(request):
    # 사용자로 부터 받은 데이터를 추출
    title= request.POST.get('title')
    content = request.POST.get('content')
    

    # DB에 저장 요청 세가지 방법
    # 1.
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 2.
    article = Article(title = title, content = content)
    # 유효성 검사 진행
    article.save()

    #3. 유효성 검사 코드를 할 수 없다.
    # Article.objects.create(title = title, content = content)
    # return render(request, 'articles/create.html')
    # 메인페이지로 돌아감
    # return redirect('articles:index')

    # 디테일 페이지로 이동
    return redirect('articles:detail', article.pk)

def delete(request, pk):
    # 어떤 게시글을 지우는지 먼저 조회
    article = Article.objects.get(pk=pk)
    # DB에 삭제 요청
    article.delete()
    return redirect('articles:index')

def edit(request, pk):
    # 몇번 게시글 정보를 보여줄지 조회
    article = Article.objects.get(pk=pk)
    context = {
        'article' = article,
    }
    return render(request, 'articles/edit.html', context)