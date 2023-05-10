from django.contrib import admin
from .models import Header, HomePage, Title, HomePageCategory, HomePageCollection, YourNft, YourNftContent, HomeItemsPath, HomeItemsContent, Footer
from .models import GeneralTitle, ExploreTopItem, ExploreFirstItem, ExploreItem, ExploreTopSeller
from .models import DetailInfo, DetailContent
from .models import AuthorPage, AuthorContent
from .models import CreateGet, CreatePost, CreatePreview, CreatePreviewContent

# Register your models here.

admin.site.register(Header)
admin.site.register(HomePage)
admin.site.register(Title)
admin.site.register(HomePageCategory)
admin.site.register(HomePageCollection)
admin.site.register(YourNft)
admin.site.register(YourNftContent)
admin.site.register(HomeItemsPath)
admin.site.register(HomeItemsContent)
admin.site.register(Footer)
admin.site.register(GeneralTitle)
admin.site.register(ExploreTopItem)
admin.site.register(ExploreFirstItem)
admin.site.register(ExploreItem)
admin.site.register(ExploreTopSeller)
admin.site.register(DetailInfo)
admin.site.register(DetailContent)
admin.site.register(AuthorPage)
admin.site.register(AuthorContent)
admin.site.register(CreateGet)
admin.site.register(CreatePost)
admin.site.register(CreatePreview)
admin.site.register(CreatePreviewContent)