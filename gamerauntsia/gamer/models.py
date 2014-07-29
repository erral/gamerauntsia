from cssocialuser.models import CSAbstractSocialUser
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.contrib.auth.models import UserManager
from django.core.mail import send_mail
from django.conf import settings
from photologue.models import Photo
from django.utils.translation import ugettext as _

MEMBER_PHOTO_SLUG=getattr(settings,'PROFILE_PHOTO_DEFAULT_SLUG','no-profile-photo')

class GamerUser(CSAbstractSocialUser):
    nickname = models.CharField(max_length=64,null=True,blank=True)
    last_updated = models.DateTimeField(auto_now_add=True,editable=False)
    date_joined = models.DateTimeField(auto_now_add=True,editable=False,null=True,blank=True)

    objects = UserManager()

    def get_photo(self):
        if self.photo:
            return self.photo
        else:
            try:
                return Photo.objects.get(title_slug=MEMBER_PHOTO_SLUG)    
            except:
                return None 


    def getFullName(self):
        try:
            return self.get_full_name().strip() or self.username
        except:
            return self.username


    def get_profile(self):
        return self

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)
  
       
    class Meta:
        verbose_name = 'Erabiltzailea'
        verbose_name_plural = 'Erabiltzaileak'     