from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta: #used when we send table to admin
        ordering = ('name',)
        verbose_name = "Category"  # the singular form of the object of the database table #تظهر كأسم للفورم بعد ما ادخل للجدول
        verbose_name_plural = "Categorys" #the plural form of the database table # تظهر كاسم للجدول

    def __str__(self):
        return self.name

    def get_absolute_url(self): # هذه الفانكشن مهمتها هي جلب الصنف او المنتج الذي تم تحديده من غير ما اعملها كود مخصوص
        return reverse('shop:product_list_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    Image = models.ImageField(blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField() #الكمية المتاحة
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',) # - تعني ترتيب عكسي
        index_together = (('id', 'slug'),) # when we use query #هيستخدم الاتنين مع بعض عشان يرجع المنتج
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])