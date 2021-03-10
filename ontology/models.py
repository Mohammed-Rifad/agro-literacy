from django.db import models


class Dealer(models.Model):
    FirstName=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    Email=models.EmailField()
    Photo=models.ImageField()
    Place=models.CharField(max_length=100,null=True)
    Phone=models.PositiveIntegerField()
    Password = models.CharField(max_length=100)
    ConfirmPassword = models.CharField(max_length=10)
    Status = models.BooleanField(default=False)

    def __str__(self):
        return self.FirstName


choice=(
    ('male','Male'),
    ('female','Female')
)


class District(models.Model):
    District=models.CharField(max_length=100)

    def __str__(self):
        return self.District


class Farmer(models.Model):
    Firstame=models.CharField(max_length=100)
    Lastname=models.CharField(max_length=100)
    Gender=models.CharField(max_length=100,choices=choice)
    Address=models.CharField(max_length=100)
    Email=models.EmailField()
    Place=models.CharField(max_length=100)
    Photo=models.ImageField()
    Phone=models.IntegerField()
    Village=models.CharField(max_length=100)
    District=models.ForeignKey(District,on_delete=models.CASCADE,null=True)
    Password=models.CharField(max_length=8)
    ConfirmPassword=models.CharField(max_length=8)
    Status=models.BooleanField(default=False)

    def __str__(self):
        return self.Firstame


class Category(models.Model):
    Name = models.CharField(max_length=30)
    Photo=models.ImageField()

    def __str__(self):
        return self.Name


class Subcategory(models.Model):
    Category=models.ForeignKey(Category,on_delete=models.CASCADE)
    Name=models.CharField(max_length=30)
    Photo=models.ImageField()

    def __str__(self):
        return self.Name


class Product(models.Model):
    OwnerId=models.PositiveIntegerField()
    OwnerName=models.CharField(max_length=100)
    Category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    Subcategory=models.ForeignKey(Subcategory,on_delete=models.CASCADE,null=True)
    Name = models.CharField(max_length=40)
    Price = models.PositiveIntegerField()
    Rent_Amount=models.PositiveIntegerField()
    Quantity = models.PositiveIntegerField()
    Photo = models.ImageField()
    Use = models.TextField()

    def __str__(self):
        return self.Name


class DealerNotification(models.Model):
    DealerId=models.ForeignKey(Dealer,on_delete=models.CASCADE)
    Notification=models.TextField()

    def __str__(self):
        return self.Notification


class KnowledgeCenterNotification(models.Model):
    Notification=models.TextField()

    def __str__(self):
        return self.Notification


class KnowledgeCenterService(models.Model):
    Service=models.TextField()

    def __str__(self):
        return self.Service


class Rent(models.Model):
    Product=models.ForeignKey(Product,on_delete=models.CASCADE)
    No_of_Days=models.PositiveIntegerField()
    Farmer=models.ForeignKey(Farmer,on_delete=models.CASCADE)
    Total_Amount=models.PositiveIntegerField()
    Rent_Date=models.DateTimeField(null=True)
    Return_Date=models.DateTimeField(blank=True,null=True)
    Status=models.CharField(max_length=50,default="Pending")

    def __str__(self):
        return self.Product.Name


class Order(models.Model):
    Product=models.ForeignKey(Product,on_delete=models.CASCADE)
    Quantity=models.PositiveIntegerField()
    Total_Amount=models.PositiveIntegerField()
    Farmer=models.ForeignKey(Farmer,on_delete=models.CASCADE)
    Dealer=models.ForeignKey(Dealer,on_delete=models.CASCADE)
    Type=models.CharField(max_length=50)
    Status=models.CharField(max_length=50,default="Pending")
    Delivery = models.CharField(max_length=50,null=True)
    Delivery_status = models.CharField(max_length=50, default='pending')

    def __str__(self):
        return self.Product.Name


class Complaint(models.Model):
    farmer=models.ForeignKey(Farmer,on_delete=models.CASCADE)
    complaint=models.TextField()
    c_date=models.DateField()
    replay=models.TextField(null=True)
    replay_date=models.DateField(null=True)

    def __str__(self):
        return self.complaint


class Question(models.Model):
    farmer=models.ForeignKey(Farmer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    question=models.TextField()
    que_date=models.DateTimeField()
    replay = models.TextField(null=True)
    replay_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.question






