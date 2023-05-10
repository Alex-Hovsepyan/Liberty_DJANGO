from django.shortcuts import render, redirect
from .models import Header, HomePage, Title, HomePageCategory, HomePageCollection, YourNft, YourNftContent, HomeItemsPath, HomeItemsContent, Footer
from .models import GeneralTitle, ExploreTopItem, ExploreFirstItem, ExploreItem, ExploreTopSeller
from .models import DetailInfo, DetailContent
from .models import AuthorPage, AuthorContent
from .models import CreateGet, CreatePost, CreatePreview, CreatePreviewContent
from .forms import CreateModelForm

from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def double_content():
    header_content = Header.objects.all()[0]
    titles = Title.objects.all()[0]
    footer = Footer.objects.all()[0]
    general_title = GeneralTitle.objects.all()[0]
    homepage_nft = YourNft.objects.all()[0]
    homepage_nft_content = YourNftContent.objects.all()

    return [header_content, titles, footer, general_title, homepage_nft, homepage_nft_content]

def index(request):
    homepage1 = HomePage.objects.all()[0]
    homepage_category = HomePageCategory.objects.all()
    homepage_collection = HomePageCollection.objects.all()
    home_items_path = HomeItemsPath.objects.all()[0]
    home_items_content = HomeItemsContent.objects.all()

    return render(request, 'main/index.html', context={
        'header_content':double_content()[0],
        'homepage1':homepage1,
        'titles':double_content()[1],
        'homepage_category':homepage_category,
        'homepage_collection':homepage_collection,
        'homepage_nft':double_content()[4],
        'homepage_nft_content':double_content()[5],
        'home_items_path':home_items_path,
        'home_items_content':home_items_content,
        'footer':double_content()[2],
        'link':'index'
    
    })

def explore(request):
    explore_top_items = ExploreTopItem.objects.all()
    explore_first_item = ExploreFirstItem.objects.all()[0]
    explore_items = ExploreItem.objects.all()
    explore_top_seller = ExploreTopSeller.objects.all()

    return render(request, 'main/explore.html', context={
        'header_content':double_content()[0],
        'titles':double_content()[1],
        'footer':double_content()[2],
        'general_title':double_content()[3],
        'explore_top_items':explore_top_items,
        'explore_first_item':explore_first_item,
        'explore_items':explore_items,
        'explore_top_seller':explore_top_seller,
	    'link':'explore'
    })

def author(request):
    author = AuthorPage.objects.all()[0]
    author_content = AuthorContent.objects.all()

    return render(request, 'main/author.html', context={
        'header_content':double_content()[0],
        'titles':double_content()[1],
        'footer':double_content()[2],
        'general_title':double_content()[3],
        'author':author,
        'author_content':author_content,
        'homepage_nft':double_content()[4],
        'homepage_nft_content':double_content()[5],
	    'link':'author'
	
    })
    

def create(request):
    if request.method == 'POST':
        form = CreateModelForm(request.POST)
        if form.is_valid():
            CreatePost.objects.create(**form.cleaned_data)
            return redirect('create')
    else:
        form = CreateModelForm()

    create_get = CreateGet.objects.all()[0]
    create_preview = CreatePreview.objects.all()[0]
    create_preview_content = CreatePreviewContent.objects.all()

    return render(request, 'main/create.html', context={
        'header_content':double_content()[0],
        'titles':double_content()[1],
        'footer':double_content()[2],
        'general_title':double_content()[3],
        'create_get':create_get,
        'create_preview':create_preview,
        'create_preview_content':create_preview_content,
		'link':'create'
        
    })

def index_detail(request, id):
    home_one_item = HomeItemsContent.objects.get(pk=id)
    details_info = DetailInfo.objects.all()[0]
    details_content = DetailContent.objects.all()
    return render(request, 'main/index_detail.html', context={
        'home_one_item':home_one_item,
        'header_content':double_content()[0],
        'titles':double_content()[1],
        'footer':double_content()[2],
        'general_title':double_content()[3],
        'details_info':details_info,
        'details_content':details_content,
        'homepage_nft':double_content()[4],
        'homepage_nft_content':double_content()[5],
        'link':'index_detail'
    })


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render(request=request, template_name="main/register.html", context={
		"register_form":form,
        'header_content':double_content()[0],
        'titles':double_content()[1],
        'footer':double_content()[2],
        'general_title':double_content()[3],
        'link':'login'
    })

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="main/login.html", context={
		"login_form":form,
		'header_content':double_content()[0],
        'titles':double_content()[1],
        'footer':double_content()[2],
        'general_title':double_content()[3],
        'link':'login'
	})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("index")