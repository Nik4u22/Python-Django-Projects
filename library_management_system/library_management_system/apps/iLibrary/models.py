from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.html import format_html
from tinymce.models import HTMLField


class Department(models.Model):
    department_id = models.AutoField(_("Department Id"), primary_key=True)
    name = models.CharField(_("Name"), max_length=50)

    class Meta:
        verbose_name = _("Department")
        verbose_name_plural = _("Departments")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Department_detail", kwargs={"pk": self.pk})
    

class Employee(models.Model):
    department = models.ForeignKey(Department, verbose_name=_("Department"), on_delete=models.CASCADE)
    employee_id = models.AutoField(_("Employee Id"), primary_key=True)
    image = models.ImageField(_("Avatar Image"),)
    name = models.CharField(_("Name"), max_length=50)
    gender = models.CharField(_("Gender"), max_length=1)
    address = models.CharField(_("Address"), max_length=100)
    contact_no = models.CharField(_("Contact No"), max_length=10)
    designation = models.CharField(_("Designation"), max_length=30)
    is_active = models.BooleanField(_("Is Active"), default=True)
    last_updated = models.DateTimeField(_("Last Updated"), auto_now=True, auto_now_add=False)
    date_added = models.DateTimeField(_("Date Added"), auto_now_add=True)

    class Meta:
        verbose_name = _("Employee")
        verbose_name_plural = _("Employees")

    def employee_image(self):
            return format_html('<img src="/media/{}" style="width:40px;height:40px;border-radius:50%;" />'.format(self.image))
        
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Employee_detail", kwargs={"pk": self.pk})
    

class Student(models.Model):
    department = models.ForeignKey(Department, verbose_name=_("Department"), on_delete=models.CASCADE)
    student_id = models.AutoField(_("Student Id"), primary_key=True)
    image = models.ImageField(_("Avatar Image"),)
    roll_number = models.CharField(_("Roll No"), max_length=20)
    name = models.CharField(_("Name"), max_length=50)
    gender = models.CharField(_("Gender"), max_length=1)
    address = models.CharField(_("Address"), max_length=100)
    contact_no = models.CharField(_("Contact No"), max_length=10)
    batch = models.CharField("Batch", max_length=20)
    academic_year = models.CharField(_("Academic Year"), max_length=20)
    is_active = models.BooleanField(_("Is Active"), default=True)
    last_updated = models.DateTimeField(_("Last Updated"), auto_now=True, auto_now_add=False)
    date_added = models.DateTimeField(_("Date Added"), auto_now_add=True)

    class Meta:
        verbose_name = _("Student")
        verbose_name_plural = _("Students")

    def student_image(self):
            return format_html('<img src="/media/{}" style="width:40px;height:40px;border-radius:50%;" />'.format(self.image))
        
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Student_detail", kwargs={"pk": self.pk})
    
# Create your models here.
class Book(models.Model):
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    book_id = models.AutoField(_("Book Id"), primary_key=True)
    image = models.ImageField(_("Book Image"),)
    name = models.CharField(_("Name"), max_length=100)
    author = models.CharField(_("Author"), max_length=50)
    description = models.CharField(_("Description"), max_length=200)
    is_issued = models.BooleanField(_("Is Issued"), default=False)
    last_updated = models.DateTimeField(_("Last Updated"), auto_now=True, auto_now_add=False)
    date_added = models.DateTimeField(_("Date Added"), auto_now_add=True)
    

    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Books")

    def book_image(self):
            return format_html('<img src="/media/{}" style="width:40px;height:40px;border-radius:50%;" />'.format(self.image))
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Book_detail", kwargs={"pk": self.pk})
    
    
class IssueBook(models.Model):

    user = models.ForeignKey(User, verbose_name=_("Issuer Id"), on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, verbose_name=_("Book Id"), on_delete=models.CASCADE)
    issuee_id = models.CharField(_("Issuee Id"), max_length=50)
    issue_id = models.AutoField(_("Book Issue Id"), primary_key=True)
    issue_date = models.DateTimeField(_("Date Added"))
    renew_date = models.DateTimeField(_("Date Added"))
    last_updated = models.DateTimeField(_("Last Updated"), auto_now=True, auto_now_add=False)
    date_added = models.DateTimeField(_("Date Added"), auto_now_add=True)

    class Meta:
        verbose_name = _("IssueBook")
        verbose_name_plural = _("IssueBooks")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("IssueBook_detail", kwargs={"pk": self.pk})
