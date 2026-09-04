from django.db import models
from django.contrib.auth.models import User


class Itemdetails(models.Model):
    CATEGORY_CHOICES = [
        ('electronics', 'Electronics'),
        ('wallet', 'Wallet / Purse'),
        ('bag', 'Bag / Backpack'),
        ('keys', 'Keys'),
        ('document', 'Documents / ID'),
        ('jewelry', 'Jewelry'),
        ('clothing', 'Clothing'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    itemName = models.CharField(max_length=100)
    itemDescription = models.TextField()
    itemTag = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='other'
    )
    itemImage = models.ImageField(upload_to='Items/')
    location = models.CharField(max_length=300, default="Kathmandu")
    foundDate = models.DateField()
    phoneNo = models.CharField(max_length=20, default="98000000")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Found Item'
        verbose_name_plural = 'Found Items'

    def __str__(self):
        return f"{self.user.username} - {self.itemName} ({self.location})"

    def get_tag_display_label(self):
        return dict(self.CATEGORY_CHOICES).get(self.itemTag, self.itemTag)