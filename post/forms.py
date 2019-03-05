from django import forms
from .models import Post, Comment
from captcha.fields import ReCaptchaField

class PostForm(forms.ModelForm):
   # captcha = ReCaptchaField()              BURAYI KAPATIP YORUMU DOLDURDUK ÇÜNKÜ İNSANLAR OTOMATİK YORUM YAPABİLİR PROGRAMLARLA SONUÇTA SİTEYİ ZARAR VEREBİLİR

    class Meta:
        model = Post
        fields = [
            'esnaf',
            'alımad',
            'alımtc',
            'title',
            'titleiki',
            'titleuc',
            'content',
            'image',
            'confirm',
            'tezgahfiyatı',
            'contents',
            'contente',
            'contenth',
            'kacasatıldı',
            'kazanc',



           # 'publishing_date',           bu çıktı çünkü otomatik doldurmak için ayarladık.
        ]



class CommentForm(forms.ModelForm):
   # captcha = ReCaptchaField()

    class Meta:
        model = Comment
        fields = [
            'name',
            'content',

        ]
