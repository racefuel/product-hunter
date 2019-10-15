from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# P̶r̶o̶d̶u̶c̶t̶ c̶l̶a̶s̶s̶:̶
# t̶i̶t̶l̶e̶, u̶r̶l̶, p̶u̶b̶_̶d̶a̶t̶e̶, t̶o̶t̶a̶l̶ v̶o̶t̶e̶s̶, i̶m̶a̶g̶e̶, i̶c̶o̶n̶, b̶o̶d̶y̶/̶d̶e̶s̶c̶r̶i̶p̶t̶i̶o̶n̶
# p̶u̶b̶_̶d̶a̶t̶e̶_̶p̶r̶e̶t̶t̶y̶, hunter


class Product(models.Model):

    title = models.CharField(max_length=250)
    pub_date = models.DateTimeField()
    body = models.TextField()
    url = models.TextField()
    image = models.ImageField(upload_to="images/")
    icon = models.ImageField(upload_to="images/")
    votes_total = models.IntegerField(default=1)
    hunter = models.ForeignKey(
        User, on_delete=models.CASCADE
    )  # Products are also deleted if the user(referenced object) is deleted

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:160]

    def pub_date_pretty(self):
        return self.pub_date.strftime("%b %e, %Y")

