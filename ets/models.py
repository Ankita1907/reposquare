from django.db import models



class Property(models.Model):
   
   
    id = models.AutoField(primary_key = True)
    desc =models.TextField(default=" ")
    flooring =models.CharField(max_length=100,default=" ")
    lift =models.CharField(max_length=300,default=" ")
    furnished =models.CharField(max_length=200, default=" ")
    configuration =models.TextField(default=" ")
    tower =models.CharField(max_length=200,default=" ")
    highlights =models.CharField(max_length=100,default=" ")
    locality_recom =models.TextField(default=" ")
    name = models.CharField(max_length=1000, default="")
    builder_name = models.CharField(max_length=1000, default="")
    locations =models.CharField(max_length=1000,default="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,")
    landmark = models.CharField(max_length=1000,default="")
    overlook = models.CharField(max_length=1000,default="")
    flooring = models.CharField(max_length=1000, default="")
    water = models.CharField(max_length=1000,default="")
    car_parking =models.CharField(max_length=1000,default="")
    electricity =models.CharField(max_length=1000,default="")
    full_address = models.CharField(max_length=1000, default="")
    floor_plan = models.ImageField(default=False)
    amenities = models.CharField(max_length=1000, default="")
    flat_sqft =models.CharField(max_length=1000,default="")
    price = models.CharField(max_length=1000,default="")
    pic =models.ImageField(upload_to="ets/images", default="")
    

    def __str__(self):
        return self.name



class Pictures(models.Model):

    property = models.ForeignKey(Property,on_delete=models.CASCADE)
    image = models.ImageField()
    
    


    

class Contacts(models.Model):
    name=models.CharField(max_length=1000)
    email=models.CharField(max_length=1000)
    address=models.CharField(max_length=1000)
    phone = models.CharField(max_length=1000)
    altphone = models.CharField(max_length=1000)

    def __str__(self):
	    return self.name










"""
class Features(models.Model):

    property_features = models.ForeignKey(Property, on_delete=models.CASCADE)
    name_for_property = models.CharField(max_length=1000, default="")
    materials_used = models.CharField(max_length=1000)
    floor_plan = models.ImageField()
    flat_size = models.CharField(max_length=1000)
    flat_location = models.CharField(max_length=1000)

    def __str__(self):
        return self.name_for_property

    


class Amenities(models.Model):

    name_for_property = models.CharField(max_length=1000, default="")
    property_amenities = models.ForeignKey(Property, on_delete=models.CASCADE)
    name_amenities = models.CharField(max_length=1000)

    def __str__(self):
        return self.name_for_property

"""

