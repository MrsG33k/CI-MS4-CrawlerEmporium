from django.db import models

# Create your models here.
from django.db import models

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    # Loot Box Rarity Tiers out of the books
    RARITY_CHOICES = [
        ('BRONZE', 'Bronze'),
        ('SILVER', 'Silver'),
        ('GOLD', 'Gold'),
        ('PLATINUM', 'Platinum'),
        ('LEGENDARY', 'Legendary'),
        ('CELESTIAL', 'Celestial'),
    ]

    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    
    # Rarity drop-down to group/style boxes on the frontend
    rarity = models.CharField(max_length=20, choices=RARITY_CHOICES, default='BRONZE')
    
    # Visual Description
    description = models.TextField(help_text="What the physical box looks like.")
    
    # The AI's sales pitch copy
    ai_flavour_text = models.TextField(blank=True, null=True, help_text="The System AI's verbal abuse/sales pitch.")
    
    # The randomised goodies inside
    sample_contents = models.TextField(help_text="Line-separated list of items inside.")
    
    # Price in GBP
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    # Images for the shop front
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"[{self.get_rarity_display()}] {self.name}"