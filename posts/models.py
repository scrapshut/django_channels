from django.db import models
from django.db.models.signals import post_save, post_delete
from django.db.models import signals
#########
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.contrib.auth.models import User
from django.template.loader import render_to_string
# from posts.models import Post

# @receiver(post_delete,sender=Post)
# @receiver(post_save,sender=Post)
def change_post(sender, instance, *args, **kwargs):
	post = Post.objects.all()
	print('post is created')
	html_users = render_to_string("includes/post.html",{'post':post})
	channel_layer = get_channel_layer()
	async_to_sync(channel_layer.group_send)(
		"posts",
		{
			"type":"post_update",
			"event":"post_user",
			'html_users': html_users,
		}
	)


# Create your models here.

class Post(models.Model):
    name=models.CharField(max_length=24)
    def __str__(self):
        return self.name
signals.post_save.connect(receiver=change_post, sender=Post)
