from django.db import models
# from django.shortcuts import reverse
from django.utils import timezone

# Менеджер постов (бизнес логика)
class PostManager(models.Manager):

	#Самые нове вопрсы:
	def post_new(self):
		return self.order_by('-created_date')

	# Наибольшее количество лайков
	def post_hot(self):
		return self.order_by('-likes')

	# Список по тегу 
	def post_tag(slef, tag):
		return self.filter(tags=tag)

	# Страница вопроса
	# def get_question(self, pk)
	# 	return self.filter (pk=pk)

# Модель вопроса
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    tags = models.ManyToManyField('Tag', related_name='posts')
    likes = models.IntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now)

    objects = PostManager()

    def publish(self):
        self.created_date = timezone.now()
        self.save()	

    def __str__(self):
        return self.title

# Модель тега
class Tag(models.Model):
	tag_name = models.CharField(max_length=15)
	# slug = models.SlugField(max_length=50, unique=True, blank=True)

# Модель ответа
class Answer(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField()
    lieks = models.IntegerField(default=0)
    created_date = models.DateTimeField(
            default=timezone.now)

class Profile(models.Model):
	name = models.CharField(max_length=100)
	# avatar = models.ImageField(upload_to='images')
	info = models.TextField(default='info')  