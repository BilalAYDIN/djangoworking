from django.db import models
from django.urls import reverse
from django.utils.text import slugify           # Create your models here.
from ckeditor.fields import RichTextField


class Post(models.Model):
    user = models.ForeignKey('auth.User',verbose_name='Yazar', related_name='posts')
    esnaf = models.CharField(max_length=30,null=True, blank=True, verbose_name='İlgili Tezgah Elemanı')
    alımad = models.CharField(max_length=30,null=True, blank=True, verbose_name='Alım yapılan kişinin Adı-Soyadı')
    alımtc = models.IntegerField(null=True, blank=True, verbose_name='Alım yapılan kişinin TC Kimlik No')
    title = models.IntegerField(null=True, blank=True, verbose_name='Seri No')# başlık =title  null=True, blank=True,
    titleiki = models.CharField(max_length=120,null=True, blank=True, verbose_name='Model')# başlık =title  null=True, blank=True,
    titleuc = models.IntegerField(null=True, blank=True, verbose_name='Alınan Fiyat')# başlık =title  null=True, blank=True,
    content = models.TextField(max_length=200,null=True, blank=True,verbose_name='İçerik')  # metin =content  null=True, blank=True,
    publishing_date= models.DateTimeField(verbose_name='yayımlanma_tarihi', auto_now_add=True) # yayımlanma_tarihi =publishing_date
    satış_date= models.DateTimeField(verbose_name='Değişim tarihi', auto_now_add=True)
    image =models.ImageField(null=True, blank=True, verbose_name='Fotoğraf') # Bu alan isteğe bağlı olduğu için yazıldı (null=True, blank=True)
    tezgahfiyatı = models.IntegerField( null=True, blank=True, verbose_name='Tezgah Fiyatı')
    kacasatıldı = models.IntegerField(null=True, blank=True, verbose_name='Kaça Satıldığı')
    kazanc = models.IntegerField(null=True, blank=True, verbose_name='Kazanç')
    # topkaz = models.IntegerField(null=True, blank=True, verbose_name='Toplam Kazanç')
    slug = models.SlugField(unique=True, editable=False, max_length=130)
    confirm = models.NullBooleanField(null=True, blank=True, verbose_name ='Yayımlansınmı?',)
    contente = models.TextField(max_length=200,null=True, blank=True,verbose_name='Emanetci hakkındaki bilgiler..')
    contenth = models.TextField(max_length=200,null=True, blank=True,verbose_name='Hurda da ne için kullanılır..')
    contents = models.TextField(max_length=200, null=True, blank=True, verbose_name='Satın alan kişi hakkında bilgi..')


    # IntegerField KOYDUK RAKAM OLANLARA ÇÜNKÜ İNT LE TAMSAYI TANIMLAYIP İŞLEM YAPTIRICAZ. VE AYNI ZAMANDA FARKLI BİLGİ GİRİŞİNİ ENGELLİCEZ..


    def __str__(self):
        return self.title
    def __str__(self):
        return self.titleiki
    def __str__(self):
        return self.titleuc
    


    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'slug': self.slug})
       # return "/post/{}".format(self.id)


    def get_create_url(self):
        return reverse('post:create')

    def get_update_url(self):
        return reverse('post:update', kwargs={'slug': self.slug})

    def get_updatedate_url(self):
        return reverse('post:updatedate', kwargs={'slug': self.slug})

    def get_updateiade_url(self):
        return reverse('post:updateiade', kwargs={'slug': self.slug})

    def get_updateiadesat_url(self):
        return reverse('post:updateiadesat', kwargs={'slug': self.slug})

    def get_updateiadeem_url(self):
        return reverse('post:updateiadeem', kwargs={'slug': self.slug})

    def get_updateiadehu_url(self):
        return reverse('post:updateiadehu', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('post:delete', kwargs={'slug': self.slug})

    def get_deletex_url(self):
        return reverse('post:deletex', kwargs={'slug': self.slug})

    def _get_unique_slug(self):
        slug = slugify(self.titleiki.replace('ı','i'))
        unique_slug = slug
        counter = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug ='{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug

    def get_deletec_url(self):
        return reverse('post:deletec', kwargs={'slug': self.slug})


    def save(self,*args, **kwargs):
        self.slug = self._get_unique_slug()
        return super(Post,self).save(*args, **kwargs)



    # BURDA [AŞŞADA YANİ] YAPTIĞIMIZ ŞEY SON POSTU EN ÜSTE GÖSTERMESİ
    class Meta:
        ordering = ['-publishing_date']

class Comment(models.Model):
    post = models.ForeignKey('post.Post',related_name='comments', on_delete=models.CASCADE )
    name = models.CharField(max_length=200, verbose_name='İsim')
    content = models.TextField(verbose_name='Yorum')
    created_date = models.DateTimeField(auto_now_add=True)



