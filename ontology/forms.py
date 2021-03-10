import re
from django import forms
from .models import Farmer,Dealer,Product,DealerNotification,KnowledgeCenterNotification,KnowledgeCenterService,Complaint,Question,Subcategory


class FarmerRegForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput,min_length=8,max_length=8)
    ConfirmPassword=forms.CharField(widget=forms.PasswordInput,min_length=8,max_length=8)

    class Meta:
        model=Farmer
        fields=('Firstame','Lastname','Gender','Address','Email','Place','Photo','Phone','Village','District','Password','ConfirmPassword')

    def clean_Firstame(self):
        name=self.cleaned_data['Firstame']
        if not re.match(r'^[A-Za-z]+$', name):
            raise forms.ValidationError("Name should be a  of Alphabets only ")
        return name

    def clean_Lastname(self):
        name=self.cleaned_data['Lastname']
        if not re.match(r'^[A-Za-z]+$', name):
            raise forms.ValidationError("Lastname should be a  of Alphabets only ")
        return name

    def clean_Place(self):
        place=self.cleaned_data['Place']
        if not re.match(r'^[A-Za-z]+$', place):
            raise forms.ValidationError("Place should be a  of Alphabets only ")
        return place

    def clean_Phone(self):
        phone=self.cleaned_data['Phone']
        length=len(str(phone))
        if length!=10:
            raise forms.ValidationError("Phone number must be 10 numbers")
        return phone

    def clean_Photo(self):
        photo=self.cleaned_data['Photo']
        return photo


class FarmerUpdateForm(forms.ModelForm):
    class Meta:
        model=Farmer
        fields=('Firstame','Lastname','Gender','Address','Email','Place','Photo','Phone','Village','District')

    def clean_Firstame(self):
        name=self.cleaned_data['Firstame']
        if not re.match(r'^[A-Za-z]+$', name):
            raise forms.ValidationError("Name should be a  of Alphabets only ")
        return name

    def clean_Lastname(self):
        name=self.cleaned_data['Lastname']
        if not re.match(r'^[A-Za-z]+$', name):
            raise forms.ValidationError("Lastname should be a  of Alphabets only ")
        return name

    def clean_Place(self):
        place=self.cleaned_data['Place']
        if not re.match(r'^[A-Za-z]+$', place):
            raise forms.ValidationError("Place should be a  of Alphabets only ")
        return place

    def clean_Phone(self):
        phone=self.cleaned_data['Phone']
        length=len(str(phone))
        if length!=10:
            raise forms.ValidationError("Phone number must be 10 numbers")
        return phone


class ChangePassForm(forms.Form):
    OldPassword = forms.CharField(widget=forms.PasswordInput, min_length=8, max_length=8)
    Password = forms.CharField(widget=forms.PasswordInput, min_length=8, max_length=8)
    ConfirmPassword = forms.CharField(widget=forms.PasswordInput, min_length=8, max_length=8)


class FarmerLoginForm(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput,min_length=8, max_length=8)

    class Meta:
        model=Farmer
        fields=('Email','Password')


class DealerRegForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput,min_length=8,max_length=8)
    ConfirmPassword=forms.CharField(widget=forms.PasswordInput,min_length=8,max_length=8)

    class Meta:
        model=Dealer
        fields=('FirstName','LastName','Email','Place','Photo','Phone','Password','ConfirmPassword')

    def clean_FirstName(self):
        name=self.cleaned_data['FirstName']
        if not re.match(r'^[A-Za-z]+$', name):
            raise forms.ValidationError("Name should be a  of Alphabets only ")
        return name

    def clean_LastName(self):
        name=self.cleaned_data['LastName']
        if not re.match(r'^[A-Za-z]+$', name):
            raise forms.ValidationError("LastName should be a  of Alphabets only ")
        return name

    def clean_Place(self):
        place=self.cleaned_data['Place']
        if not re.match(r'^[A-Za-z]+$', place):
            raise forms.ValidationError("Place should be a  of Alphabets only ")
        return place

    def clean_Phone(self):
        phone=self.cleaned_data['Phone']
        length=len(str(phone))
        if length!=10:
            raise forms.ValidationError("Phone number must be 10 numbers")
        return phone

    def clean_Photo(self):
        photo=self.cleaned_data['Photo']
        return photo


class DealerUpdateForm(forms.ModelForm):
    class Meta:
        model=Dealer
        fields=('FirstName','LastName','Email','Place','Photo','Phone')

    def clean_FirstName(self):
        name=self.cleaned_data['FirstName']
        if not re.match(r'^[A-Za-z]+$', name):
            raise forms.ValidationError("Name should be a  of Alphabets only ")
        return name

    def clean_LastName(self):
        name=self.cleaned_data['LastName']
        if not re.match(r'^[A-Za-z]+$', name):
            raise forms.ValidationError("LastName should be a  of Alphabets only ")
        return name

    def clean_Place(self):
        place=self.cleaned_data['Place']
        if not re.match(r'^[A-Za-z]+$', place):
            raise forms.ValidationError("Place should be a  of Alphabets only ")
        return place

    def clean_Phone(self):
        phone=self.cleaned_data['Phone']
        length=len(str(phone))
        if length!=10:
            raise forms.ValidationError("Phone number must be 10 numbers")
        return phone


class DealerLoginForm(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput,min_length=8, max_length=8)

    class Meta:
        model=Dealer
        fields=('Email','Password')


class AddProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=('Name','Price','Rent_Amount','Quantity','Photo','Use')

    def clean_Name(self):
        name=self.cleaned_data['Name']
        if not re.match(r'^[A-Za-z]+$', name):
            raise forms.ValidationError("Name should be a  of Alphabets only ")
        return name

    def clean_Use(self):
        use=self.cleaned_data['Use']
        if not re.match(r'^[A-Za-z]+$', use):
            raise forms.ValidationError("Use should be a  of Alphabets only ")
        return use


class CategoryForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=('Category',)


class SubcategoryForm(forms.ModelForm):
    class Meta:
        model=Subcategory
        fields='__all__'


class DealerNotificationForm(forms.ModelForm):
    class Meta:
        model=DealerNotification
        fields=('Notification',)

    def clean_Notification(self):
        notification=self.cleaned_data['Notification']
        if not re.match(r'^[A-Z a-z]+$', notification):
            raise forms.ValidationError("Notification should be Alphabets")
        return notification


class KnowledgeCenterNotificationForm(forms.ModelForm):
    class Meta:
        model=KnowledgeCenterNotification
        fields=('Notification',)


class KnowledgeCenterServiceForm(forms.ModelForm):
    class Meta:
        model=KnowledgeCenterService
        fields=('Service',)


class ComplaintForm(forms.ModelForm):
    class Meta:
        model=Complaint
        fields=('complaint',)


class ReplayComplaintForm(forms.ModelForm):
    class Meta:
        model=Complaint
        fields=('replay',)


class QuestionForm(forms.ModelForm):
    class Meta:
        model=Question
        fields=('question',)


class ReplayQuestionForm(forms.ModelForm):
    class Meta:
        model=Question
        fields=('replay',)

