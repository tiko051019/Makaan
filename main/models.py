from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


#---------------------------------------------------------
#-------------------------Home----------------------------
#---------------------------------------------------------

class MainInfo(models.Model):
    img = models.ImageField('Image',upload_to='main_image')
    name = models.CharField('Company name',max_length=255)
    address = models.CharField('Address',max_length=255)
    phone = PhoneNumberField('Phonenumber')
    email = models.EmailField('Email')
    twitter = models.URLField('Twitter')
    facebook = models.URLField('facebook')
    youtube = models.URLField('youtube')
    linkedin = models.URLField('linkedin')


    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Main Info'
        verbose_name_plural = 'Main Info'



class ImageCycle(models.Model):
    img1 = models.ImageField('Image cycle1',upload_to='images',null = True)
    img2 = models.ImageField('Image cycle2',upload_to='images',null = True)



class HomeStatus(models.Model):
    text1 = models.CharField('part1',max_length=255)
    text2 = models.CharField('part2',max_length=255)
    text3 = models.CharField('part3',max_length=255)
    text4 = models.CharField('part4',max_length=255)
    but_text = models.CharField('Button text',max_length=255)

    def __str__(self):
        return 'homestatus1'



class Properties(models.Model):
    property_icon = models.ImageField('property_icon',upload_to='icons')
    property_name = models.CharField('property_name',max_length=30)
    availability = models.IntegerField('availability')

    def __str__(self):
        return self.property_name
    


class MoreInfo(models.Model):
    img = models.ImageField('img',upload_to='images')
    text1 = models.CharField('text1',max_length=255)
    text2 = models.CharField('text2',max_length=255)

    def __str__(self):
        return 'MoreInfo'



class SubMoreInfo(models.Model):
    key = models.ForeignKey(MoreInfo,on_delete=models.CASCADE,related_name='moreinfo_rn')
    lines = models.CharField('Lines',max_length=255)

    def __str__(self):
        return f'{self.key}'
    


class PropertyListing(models.Model):
    img = models.ImageField('image',upload_to='images')
    goal = models.CharField('For rent/sell?',max_length=255)
    name = models.CharField('name',max_length=30)
    price = models.IntegerField('Price')
    info = models.CharField('About property',max_length=255)
    adress = models.CharField('Adress',max_length=255)
    teritory = models.IntegerField('teritory(sqmt)')
    bedrooms = models.IntegerField('bedrooms number')
    bathrooms = models.IntegerField('bathrooms number')

    def __str__(self):
        return 'property'
    


class ContactAgent(models.Model):
    AgentImg = models.ImageField('AgentImage',upload_to='images')
    text1 = models.CharField('text1',max_length=255)
    text2 = models.CharField('text2',max_length=255)

    def __str__(self):
        return 'agent'
    


class PropertyAgents(models.Model):
    img = models.ImageField('AgentImg',upload_to='images')
    name = models.CharField('Full name',max_length=50)
    designation = models.CharField('Designation',max_length=30)
    facebook = models.URLField('FaceBook')
    twitter = models.URLField('Twitter')
    instagram = models.URLField('Instagram')

    def __str__(self):
        return 'PropertyAgents'
    


class ClientOpinions(models.Model):
    name = models.CharField('Client name',max_length=50)        
    img = models.ImageField('ClientImg',upload_to='images')
    comment = models.TextField('Comment')
    profession = models.CharField('Profession',max_length=30)

    def __str__(self):
        return 'Comments'
    


class Gallery(models.Model):
    images = models.ImageField('Gallery',upload_to='images')

    def __str__(self):
        return 'Gallery'


#---------------------------------------------------------
#------------------------About----------------------------
#---------------------------------------------------------

class AboutStatus(models.Model):
    img = models.ImageField('image',upload_to='images')
    text = models.CharField('Some text',max_length=255)
    word1 = models.CharField('word1',max_length=255)
    word2 = models.CharField('word2',max_length=255)
    word3 = models.CharField('word3',max_length=255)

    def __str__(self):
        return 'AboutStatus'
    

#---------------------------------------------------------
#------------------------Contact--------------------------
#---------------------------------------------------------

class ContactModel(models.Model):
    name = models.CharField('Your name',max_length=255,blank=True)
    email = models.EmailField('Your Email',blank=True)
    subject = models.CharField('Subject',max_length=255)
    message = models.TextField('Message')

    def __str__(self):
        return self.name