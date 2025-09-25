from django.db import models



class SiteSetting(models.Model):
    site_name = models.CharField(max_length=50, verbose_name='نام سایت')
    site_url = models.CharField(max_length=200, verbose_name='دامنه سایت')
    address = models.CharField(max_length=200, verbose_name='آدرس')
    phone_number = models.CharField(max_length=12, verbose_name="شماره تلفن همراه")
    office_number = models.CharField(max_length=12, verbose_name="شماره تلفن ثابت")
    email = models.EmailField(max_length=100, verbose_name="ایمیل")
    email2 = models.EmailField(max_length=100, verbose_name="ایمیل دوم", null=True, blank=True)
    copy_right = models.TextField(verbose_name='متن کپی رایت سایت')
    about_us_text = models.TextField(verbose_name='متن درباره ما سیات')
    site_logo = models.ImageField(upload_to='image/media', verbose_name='لوگو سایت')
    is_main_setting = models.BooleanField(verbose_name='تنظیمات اصلی')

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنظیمات'

    def __str__(self):
        return self.site_name
    

class FooterLinkBox(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")

    class Meta:
        verbose_name = 'دسته بندی لینک های فوتر'
        verbose_name_plural = 'دسته بندی لینک های فوتر'

    def __str__(self):
        return self.title
    

class FooterLink(models.Model):
    Ftitle = models.CharField(max_length=200, verbose_name='عنوان')
    url = models.URLField(max_length=500, verbose_name='لینک')
    footer_link_box = models.ForeignKey(FooterLinkBox, on_delete=models.CASCADE, verbose_name='دسته بندی', related_name='links')

    class Meta:
        verbose_name = 'لینک فوتر'
        verbose_name_plural = 'لینک های فوتر'

    def __str__(self):
        return self.Ftitle
    


class Banner(models.Model):
    small_title = models.CharField(max_length=200, verbose_name="متن کوتاه بالای عنوان")
    title = models.CharField(max_length=200, verbose_name="عنوان")
    description = models.TextField(verbose_name='توضیحات بنر')
    image = models.ImageField(upload_to='image/banner', verbose_name='تغییر بنر')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')

    class Meta:
        verbose_name = 'بنر'
        verbose_name_plural = 'بنر ها'

    def __str__(self):
        return self.title