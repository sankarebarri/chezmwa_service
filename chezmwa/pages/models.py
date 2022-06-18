from django.db import models

class State(models.Model):
    state_name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.state_name)

class Realtor(models.Model):
    realtor_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    hired_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.realtor_name)

class Neighborhood(models.Model):
    neighborhood_name = models.CharField(max_length=200)
    neighborhood_state = models.ForeignKey(State, on_delete=models.CASCADE)
    neighborhood_image = models.ImageField(upload_to='neighborhood_image', blank=True, default='house.jpg')

    def __str__(self):
        return str(self.neighborhood_name)

class Listing(models.Model):
    title = models.CharField(max_length=200)
    state = models.ForeignKey(State, on_delete=models.DO_NOTHING)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    garages = models.IntegerField()
    price = models.IntegerField()
    is_highstanding = models.BooleanField(default=False)
    type = models.TextField()
    description = models.TextField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    realtor = models.ForeignKey(Realtor, on_delete=models.CASCADE)
    list_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} -> {self.neighborhood}"
