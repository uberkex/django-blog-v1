from django.contrib import admin
from article.models import Article, Category


# Register your models here.

# admin.site.register(Article)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # Makalelerin listelendiği sayfadaki tabloda gözükecek bilgiler
    list_display = ('title', 'author', 'status', 'created_date')

    # Detay sayfasına gitmek için neye tıklayacağımızı seçiyoruz, link verilen özellik
    list_display_links = ('title', 'created_date')

    # Detayına girmeden değiştirebileceğimiz özelliği seçiyoruz
    list_editable = ('status',)

    # Arama özelliği ekler ve aşağıdaki özelliklere göre arama yapabiliriz
    search_fields = ('title', 'author')

    # Sağ tarafa bir filtre ekler
    list_filter = ('status',)

    # En önemlisi, otomatik slug oluşturur, başlığa göre
    prepopulated_fields = {'slug': ('title', 'author')}

    # gözükmeyen fieldları görmek için
    readonly_fields = ('created_date', 'updated_date')

    class Meta:
        model = Article

admin.site.register(Category)