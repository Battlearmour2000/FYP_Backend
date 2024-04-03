from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    # contact_information = models.ForeignKey('ContactInformation', on_delete=models.CASCADE)
    # role = models.ForeignKey('Role', on_delete=models.CASCADE)
    password = models.CharField(max_length=100)  # For simplicity, should be hashed
    # profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    language = models.CharField(max_length=50)
    # notifications = models.ManyToManyField('Notification')
    status_state = [
        ('active', 'Active'),
        ('inactive', 'Inactive')
    ]
    user_status = models.CharField(choices=status_state, max_length=8, default='inactive')
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.surname}"

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # Add any additional fields specific to Seller if needed

class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # Add any additional fields specific to Buyer if needed


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # Add any additional fields specific to Admin if needed

class UserAddress(models.Model):
    address_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    ward = models.CharField(max_length=100)
    village_street = models.CharField(max_length=100)


# class ContactInformation(models.Model):
#     contact_id = models.AutoField(primary_key=True)
#     contact_type = models.CharField(max_length=100)
#     contact_value = models.CharField(max_length=100)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)


class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_type = models.CharField(max_length=100)
    role_name = models.CharField(max_length=100)


# class Notification(models.Model):
#     notification_type = models.CharField(max_length=100)
#     notification_content = models.TextField()
#     recipient_id = models.CharField(max_length=100)  # Assuming MSISDN or Email ID
#     date_sent = models.DateTimeField(auto_now_add=True)
#     delivery_status = models.CharField(max_length=100)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)
    time_closed = models.DateTimeField(null=True, blank=True)
    order_status = models.CharField(max_length=100)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()
    product_quantity = models.PositiveIntegerField()
    product_image = models.ImageField(upload_to='product_images/')


class Delivery(models.Model):
    delivery_id = models.AutoField(primary_key=True)
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    delivery_status = models.CharField(max_length=100)
    delivery_time = models.DateTimeField()


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    receipt = models.FileField(upload_to='payment_receipts/')
    payment_method = models.CharField(max_length=100)


class Dispute(models.Model):
    dispute_id = models.AutoField(primary_key=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    issued_by = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_closed = models.DateTimeField(null=True, blank=True)
    dispute_status = models.CharField(max_length=100)


class AuditTrail(models.Model):
    old_record = models.TextField()
    new_record = models.TextField()
    table_affected = models.CharField(max_length=100)
    action = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User, related_name='added_by', on_delete=models.CASCADE)
    attended_by = models.ForeignKey(User, related_name='attended_by', on_delete=models.CASCADE)
    attended_date = models.DateTimeField()
    reason = models.TextField()
