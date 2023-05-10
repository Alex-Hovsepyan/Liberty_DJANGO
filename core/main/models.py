from django.db import models

# Create your models here.

class Header(models.Model):

    img = models.ImageField('Header Logo Image', upload_to='images')
    path1 = models.CharField('Header Path 1', max_length=50)
    path2 = models.CharField('Header Path 2', max_length=50)
    path3 = models.CharField('Header Path 3', max_length=50)
    path4 = models.CharField('Header Path 4', max_length=50)
    path5 = models.CharField('Header Path 5', max_length=50)

    class Meta:

        verbose_name = 'Header'
        verbose_name_plural = 'Header'

class HomePage(models.Model):

    title = models.CharField('HomePage Title', max_length=50)
    subtitle = models.CharField('HomePage subTitle', max_length=50)
    text = models.TextField('HomePage Text')
    btn_name1 = models.CharField('HomePage Button Name 1', max_length=30)
    btn_name2 = models.CharField('HomePage Button Name 2', max_length=30)
    img1 = models.ImageField('HomePage Image 1', upload_to='images')
    img2 = models.ImageField('HomePage Image 2', upload_to='images')
    
    class Meta:

        verbose_name = 'Home Page'
        verbose_name_plural = 'Home Page'

class Title(models.Model):

    title1 = models.CharField('Titles Title 1', max_length=80)
    colored_title1 = models.CharField('Titles Colored Title 1', max_length=50)
    title2 = models.CharField('Titles Title 2', max_length=80)
    colored_title2 = models.CharField('Titles Colored Title 2', max_length=50)
    title3 = models.CharField('Titles Title 3', max_length=80)
    colored_title3 = models.CharField('Titles Colored Title 3', max_length=50)
    title4 = models.CharField('Titles Title 4', max_length=80)
    colored_title4 = models.CharField('Titles Colored Title 4', max_length=50)
    title5 = models.CharField('Titles Title 5', max_length=80)
    colored_title5 = models.CharField('Titles Colored Title 5', max_length=50)
    title6 = models.CharField('Titles Title 6', max_length=80)
    colored_title6 = models.CharField('Titles Colored Title 6', max_length=50)
    title7 = models.CharField('Titles Title 7', max_length=80)
    colored_title7 = models.CharField('Titles Colored Title 7', max_length=50)
    title8 = models.CharField('Titles Title 8', max_length=80)
    colored_title8 = models.CharField('Titles Colored Title 8', max_length=50)
    title9 = models.CharField('Titles Title 1', max_length=80)
    
class HomePageCategory(models.Model):

    img = models.ImageField('HomePage Category Image', upload_to='images')
    title = models.CharField('HomePage Category Title', max_length=50)

    class Meta:

        verbose_name = 'Home Page Category'
        verbose_name_plural = 'Home Page Categories'

class HomePageCollection(models.Model):

    img = models.ImageField('HomePage Collection', upload_to='images')
    title = models.CharField('HomePage Collection', max_length=50)
    subtitle1 = models.CharField('HomePage SubTitle 1', max_length=50)
    subtitle1_info = models.CharField('HomePage Subtitle 1 Info', max_length=50)
    subtitle2 = models.CharField('HomePage SubTitle 2', max_length=50)
    subtitle2_info = models.CharField('HomePage Subtitle 2 Info', max_length=50)
    btn_name = models.CharField('HomePage Collection Button Name', max_length=40)

class YourNft(models.Model):

    title = models.CharField('Your Nft Title', max_length=50)
    btn_name = models.CharField('Your Nft Button Name', max_length=40)

class YourNftContent(models.Model):

    img = models.ImageField('Your Nft Image', upload_to='images')
    title = models.CharField('Your Nft Title', max_length=50)
    text = models.TextField('Your Nft Text')

class HomeItemsPath(models.Model):

    path1 = models.CharField('Home Items Path 1', max_length=50)
    path2 = models.CharField('Home Items Path 2', max_length=50)
    path3 = models.CharField('Home Items Path 3', max_length=50)
    path4 = models.CharField('Home Items Path 4', max_length=50)
    path5 = models.CharField('Home Items Path 5', max_length=50)

class HomeItemsContent(models.Model):

    code = models.CharField('Home Item Content Code', max_length=20)
    img1 = models.ImageField('Home Item Content Image 1', upload_to='images')
    title = models.CharField('Home Item Content Title', max_length=50)
    img2 = models.ImageField('Home Item Content Image 2', upload_to='images')
    name = models.CharField('Home Item Content Name', max_length=50)
    name_link = models.CharField('Home Item Content Name Link', max_length=50)
    subtitle1 = models.CharField('Home Item Content Subtitle 1', max_length=30)
    current_bid = models.CharField('Home Item Content Current Bid', max_length=40)
    bid_price = models.CharField('Home Item Content Bid Price', max_length=50)
    subtitle2 = models.CharField('Home Item Content Subtitle 2', max_length=30)
    last_bid = models.CharField('Home Item Content Last Bid', max_length=50)
    date = models.CharField('Home Item Content Date', max_length=50)
    btn_name = models.CharField('Home Item Content Button Name', max_length=50)
    text = models.TextField('Text')
    info1 = models.CharField('Info 1', max_length=50)
    info2 = models.CharField('Info 2', max_length=50)
    img3 = models.ImageField('Image 3', upload_to='images')

class Footer(models.Model):

    text = models.TextField('Footer Text')

    class Meta:

        verbose_name = 'Footer'
        verbose_name_plural = 'Footer'

class GeneralTitle(models.Model):

    title1 = models.CharField('General Title 1', max_length=50)
    subtitle1 = models.CharField('General Title Subtitle 1', max_length=80)
    page_name1 = models.CharField('General Title Page Name 1', max_length=50)
    title2 = models.CharField('General Title 2', max_length=50)
    subtitle2 = models.CharField('General Title Subtitle 2', max_length=80)
    page_name2 = models.CharField('General Title Page Name 2', max_length=50)
    title3 = models.CharField('General Title 3', max_length=50)
    subtitle3 = models.CharField('General Title Subtitle 3', max_length=80)
    page_name3 = models.CharField('General Title Page Name 3', max_length=50)
    title4 = models.CharField('General Title 4', max_length=50)
    subtitle4 = models.CharField('General Title Subtitle 4', max_length=80)
    page_name4 = models.CharField('General Title Page Name 4', max_length=50)
    title4 = models.CharField('General Title 4', max_length=50)
    subtitle4 = models.CharField('General Title Subtitle 4', max_length=80)
    page_name4 = models.CharField('General Title Page Name 4', max_length=50)
    title5 = models.CharField('General Title 5', max_length=50)
    subtitle5 = models.CharField('General Title Subtitle 5', max_length=80)
    page_name5 = models.CharField('General Title Page Name 5', max_length=50)
    title6 = models.CharField('General Title 6', max_length=50)
    subtitle6 = models.CharField('General Title Subtitle 6', max_length=80)
    page_name6 = models.CharField('General Title Page Name 6', max_length=50)
    btn_name1 = models.CharField('General Title Button Name 1', max_length=50)
    btn_name2 = models.CharField('General Title Button Name 2', max_length=50)
    

class ExploreTopItem(models.Model):

    inheritence = models.ForeignKey(HomeItemsContent, on_delete=models.CASCADE)
    img = models.ImageField('Image', upload_to='images')

class ExploreFirstItem(models.Model):

    btn_name1 = models.CharField('Button Name 1', max_length=40)
    profile_img1 = models.ImageField('Profile Image 1', upload_to='images')
    img1 = models.ImageField('Image 1', upload_to='images')
    title1 = models.CharField('Title 1', max_length=50)
    profile_img2 = models.ImageField('Profile Image 2', upload_to='images')
    img2 = models.ImageField('Image 2', upload_to='images')
    title2 = models.CharField('Title 2', max_length=50)
    subtitle1 = models.CharField('Subtitle 1', max_length=50)
    subtitle2 = models.CharField('Subtitle 2', max_length=50)
    subtitle3 = models.CharField('Subtitle 3', max_length=50)
    subtitle4 = models.CharField('Subtitle 4', max_length=50)
    info1 = models.CharField('Info 1', max_length=40)
    info2 = models.CharField('Info 2', max_length=40)
    info3 = models.CharField('Info 3', max_length=40)
    info4 = models.CharField('Info 4', max_length=40)
    btn_name2 = models.CharField('Button Name 2', max_length=40)

    class Meta:

        verbose_name = 'ExploreFirstItem'
        verbose_name_plural = 'ExploreFirstItem'

class ExploreItem(models.Model):

    profile_img = models.ImageField('Profile Image', upload_to='images')
    img = models.ImageField('Image', upload_to='images')
    title = models.CharField('Title', max_length=50)
    info1 = models.CharField('Info 1', max_length=50)
    info2 = models.CharField('Info 2', max_length=50)
    


class ExploreTopSeller(models.Model):

    img = models.ImageField('Image', upload_to='images')
    title = models.CharField('Title', max_length=50)
    subtitle = models.CharField('Subtitle', max_length=80)

class AuthorPage(models.Model):

    img = models.ImageField('Image', upload_to='images')
    name = models.CharField('Name', max_length=50)
    name_link = models.CharField('Name Link', max_length=50)
    like = models.CharField('Like', max_length=50)
    hand = models.CharField('Hand', max_length=50)
    dollar = models.CharField('Dollar', max_length=50)
    like_count1 = models.PositiveIntegerField('Likes Count 1')
    like_count2 = models.PositiveIntegerField('Likes Count 2')
    like_count3 = models.PositiveIntegerField('Likes Count 3')
    followers = models.CharField('Followers', max_length=60)
    btn_name = models.CharField('Button Name', max_length=40)

class AuthorContent(models.Model):

    profile_img = models.ImageField('Profile Image', upload_to='images')
    img = models.ImageField('Image', upload_to='images')
    title = models.CharField('Title', max_length=50)
    subtitle1 = models.CharField('Subtitle 1', max_length=50)
    subtitle2 = models.CharField('Subtitle 2', max_length=50)
    info1 = models.CharField('Info 1', max_length=50)
    info2 = models.CharField('Info 2', max_length=50)
    btn_name = models.CharField('Button Name', max_length=50)


    
class CreateGet(models.Model):

    title = models.CharField('Create GET title', max_length=50)
    description = models.CharField('Create GET Description', max_length=80)
    username = models.CharField('Create GET Username', max_length=50)
    price = models.CharField('Create GET Price', max_length=100)
    royalty = models.CharField('Create GET Royalty', max_length=50)
    file_name = models.CharField('Create GET File Name', max_length=40)
    btn_name = models.CharField('Create GET Button Name', max_length=50)

    class Meta:

        verbose_name = 'Create GET'
        verbose_name_plural = 'Create GET'

class CreatePost(models.Model):

    user_title = models.CharField('User Title', max_length=50)
    user_description = models.CharField('User Description', max_length=80)
    user_name = models.CharField('UserName', max_length=50)
    user_price = models.CharField('User Price', max_length=20)
    user_royalty = models.CharField('User Royalty', max_length=50)

    class Meta:

        verbose_name = 'Create POST'
        verbose_name_plural = 'Create POST'

class CreatePreview(models.Model):

    img = models.ImageField('Create Preview', upload_to='images')
    title = models.CharField('Create Preview Title', max_length=80)
    profile_img = models.ImageField('Create Preview Image', upload_to='images')
    name = models.CharField('Create Preview Name', max_length=50)
    name_link = models.CharField('Create Preview Name Link', max_length=50)
    text = models.TextField('Create Preview Text')

class CreatePreviewContent(models.Model):

    title = models.CharField('Create Preview Content Title', max_length=40)
    info1 = models.CharField('Create Preview Content Info 1', max_length=50)
    info2 = models.CharField('Create Preview Content Info 2', max_length=50)

class DetailInfo(models.Model):

    subtitle = models.CharField('Home Item Content Subtitle 3', max_length=30)
    bit_title = models.CharField('Bit Title', max_length=50)
    btn_name1 = models.CharField('Button Name 1', max_length=50)
    btn_name2 = models.CharField('Button Name 2', max_length=50)

class DetailContent(models.Model):

    img = models.ImageField('Image', upload_to='images')
    name = models.CharField('Name', max_length=50)
    name_link = models.CharField('Name Link', max_length=50)
    bid = models.CharField('Bid', max_length=50)
    datetime = models.CharField('Datetime', max_length=50)