from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Farmer,Dealer,Product,Category,DealerNotification,KnowledgeCenterService,KnowledgeCenterNotification,Order,Rent,Complaint,Question,Subcategory
from .forms import FarmerLoginForm,FarmerRegForm,DealerLoginForm,DealerRegForm,FarmerUpdateForm,AddProductForm,CategoryForm,ReplayComplaintForm,SubcategoryForm
from .forms import DealerNotificationForm,DealerUpdateForm,KnowledgeCenterNotificationForm,KnowledgeCenterServiceForm,ComplaintForm,QuestionForm,ReplayQuestionForm,ChangePassForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from datetime import date
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request,'ontology/index.html')


def knowledge_center_login(request):
    
    return render(request, 'ontology/knowledge_center_login.html', {'form': form})


def knowledge_center_home(request):
    if request.session.has_key:
        username = request.session['email']
        sid = request.session['sid']
        return render(request, 'ontology/knowledge_center_home.html', {'name': username, 'sid': sid})


def manage_farmer(request):
    q=Farmer.objects.filter(Status=False)
    return render(request,'ontology/manage_farmer.html',{'q':q})


def approve_farmer(request,id):
    qr=Farmer.objects.get(id=id)
    qr.Status=1
    qr.save()
    return redirect('/manage_farmer')


def reject_farmer(request,id):
    qr=Farmer.objects.get(id=id)
    qr.Status=0
    qr.save()
    return redirect('/manage_farmer')


def manage_dealer(request):
    q=Dealer.objects.filter(Status=False)
    return render(request,'ontology/manage_dealer.html',{'q':q})


def approve_dealer(request,id):
    qr=Dealer.objects.get(id=id)
    qr.Status=1
    qr.save()
    return redirect('/manage_dealer')


def reject_dealer(request,id):
    qr=Dealer.objects.get(id=id)
    qr.Status=0
    qr.save()
    return redirect('/manage_dealer')


def add_knowledge_center_notification(request):
    sid = request.session['sid']
    admin=User.objects.get(id=sid)
    if request.method == 'POST':
        form = KnowledgeCenterNotificationForm(request.POST)
        if form.is_valid():
            notification = form.cleaned_data['Notification']
            res = KnowledgeCenterNotification(Notification=notification)
            res.save()
            messages.success(request, "Notification added successfully")
            return redirect('/knowledge_center_home')
    else:
        form = KnowledgeCenterNotificationForm()
    return render(request, 'ontology/add_knowledge_center_notification.html', {'form': form,'admin':admin})


def knowledge_center_select_category(request):
    sid = request.session['sid']
    admin = User.objects.get(id=sid)
    category=Category.objects.all()
    return render(request,'ontology/knowledge_center_select_category.html',{'category':category,'admin':admin})


def knowledge_center_select_subcategory(request):
    sid = request.session['sid']
    admin = User.objects.get(id=sid)
    cat = request.POST.get('Category')
    request.session['cat']=cat
    sub=Subcategory.objects.filter(Category=cat)
    subcat =request.POST.get('Subcategory')
    if subcat:
        subcat=Subcategory.objects.filter(id=subcat)
        return redirect('/knowledge_center_add_product/%s' % subcat)
    return render(request,'ontology/knowledge_center_select_subcategory.html',{'admin':admin,'category':cat,'sub':sub})


def knowledge_center_add_product(request,id):
    sid = request.session['sid']
    admin = User.objects.get(id=sid)
    cat=request.session['cat']
    subcat=request.POST.get('Subcategory')
    sub=Subcategory.objects.get(id=id)
    category=Category.objects.get(id=cat)
    if request.method=='POST':
        form=AddProductForm(request.POST,request.FILES)
        if form.is_valid():
            name=form.cleaned_data['Name']
            price=form.cleaned_data['Price']
            rent_amount=form.cleaned_data['Rent_Amount']
            quantity=form.cleaned_data['Quantity']
            photo=form.cleaned_data['Photo']
            use=form.cleaned_data['Use']
            res=Product(OwnerId=sid,OwnerName=admin.username,Category=category,Subcategory=sub,Name=name,Price=price,Rent_Amount=rent_amount,
                        Quantity=quantity,Photo=photo,Use=use)
            res.save()
            messages.success(request,"Product added!")
            msg = "Product added Successfully"
            return render(request, 'ontology/knowledge_center_add_product.html', {'form': form,'category':category, 'admin': admin, 'msg': msg})
    else:
        form=AddProductForm()
    return render(request,'ontology/knowledge_center_add_product.html',{'form':form,'admin':admin,'sub':sub})


def add_knowledge_center_service(request):
    sid = request.session['sid']
    admin=User.objects.get(id=sid)
    if request.method == 'POST':
        form = KnowledgeCenterServiceForm(request.POST)
        if form.is_valid():
            service = form.cleaned_data['Service']
            res = KnowledgeCenterService(Service=service)
            res.save()
            messages.success(request, "Service added successfully")
            return redirect('/knowledge_center_home')
    else:
        form = KnowledgeCenterServiceForm()
    return render(request, 'ontology/add_knowledge_center_service.html', {'form': form,'admin':admin})


def view_all_farmers(request):
    sid = request.session['sid']
    admin = User.objects.get(id=sid)
    farmer=Farmer.objects.filter(Status=True)
    return render(request,'ontology/view_all_farmers.html',{'admin':admin,'farmer':farmer})


def view_all_dealers(request):
    sid = request.session['sid']
    admin = User.objects.get(id=sid)
    dealer=Dealer.objects.filter(Status=True)
    return render(request,'ontology/view_all_dealers.html',{'admin':admin,'dealer':dealer})


def knowledge_center_view_all_products(request):
    sid = request.session['sid']
    admin = User.objects.get(id=sid)
    product=Product.objects.all()
    return render(request,'ontology/knowledge_center_view_all_products.html',{'admin':admin,'product':product})


def view_complaints(request):
    sid = request.session['sid']
    admin = User.objects.get(id=sid)
    complaint=Complaint.objects.all()
    return render(request,'ontology/view_complaints.html',{'admin':admin,'complaint':complaint})


def send_complaint_replay(request,id):
    sid = request.session['sid']
    admin = User.objects.get(id=sid)
    complaint = Complaint.objects.get(id=id)
    farmer=Farmer.objects.get(id=complaint.farmer_id)
    if request.method=='POST':
        form=ReplayComplaintForm(request.POST)
        if form.is_valid():
            replay=form.cleaned_data['replay']
            complaint.replay_date=date.today()
            complaint.replay=replay
            complaint.save()
            messages.success(request,"Replay send!")
            return redirect('/view_complaints')
    else:
        form=ReplayComplaintForm()
    return render(request,'ontology/send_complaint_replay.html',{'form':form,'admin':admin,'complaint':complaint})


def view_questions(request):
    sid = request.session['sid']
    admin = User.objects.get(id=sid)
    question=Question.objects.all()
    return render(request,'ontology/view_questions.html',{'admin':admin,'question':question})


def send_question_replay(request,id):
    sid = request.session['sid']
    admin = User.objects.get(id=sid)
    question=Question.objects.get(id=id)
    farmer=Farmer.objects.get(id=question.farmer_id)
    if request.method=='POST':
        form=ReplayQuestionForm(request.POST)
        if form.is_valid():
            replay=form.cleaned_data['replay']
            question.replay=replay
            question.replay_date=date.today()
            question.save()
            messages.success(request,"Replay Send!")
            return redirect('/view_questions')
    else:
        form=ReplayQuestionForm()
    return render(request,'ontology/send_question_replay.html',{'form':form,'admin':admin,'question':question})


def admin_view_notification(request):
    sid = request.session['sid']
    admin = User.objects.get(id=sid)
    notification=DealerNotification.objects.all()
    return render(request,'ontology/admin_view_notification.html',{'admin':admin,'notification':notification})


def manage_stock(request):
    sid = request.session['sid']
    admin = User.objects.get(id=sid)
    product=Product.objects.filter(OwnerId=sid,OwnerName=admin.username)
    return render(request,'ontology/manage_stock.html',{'admin':admin,'product':product})


def admin_update_stock(request,id):
    sid = request.session['sid']
    admin = User.objects.get(id=sid)
    product=Product.objects.get(id=id)
    form=AddProductForm(request.POST or None,instance=product)
    if form.is_valid():
        form.save()
        return redirect('/manage_stock')
    return render(request,'ontology/admin_update_stock.html',{'form':form,'product':product,'admin':admin})


def delete_admin_product(request,id):
    sid = request.session['sid']
    admin = User.objects.get(id=sid)
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('/manage_stock')


def farmer_reg(request):
    if request.method=='POST':
        form=FarmerRegForm(request.POST,request.FILES)
        if form.is_valid():
            firstname=form.cleaned_data['Firstame']
            lastname=form.cleaned_data['Lastname']
            gender=form.cleaned_data['Gender']
            address=form.cleaned_data['Address']
            email=form.cleaned_data['Email']
            place=form.cleaned_data['Place']
            photo=request.POST.get('Photo')
            phone=form.cleaned_data['Phone']
            village=form.cleaned_data['Village']
            district=form.cleaned_data['District']
            password=form.cleaned_data['Password']
            confirmpassword=form.cleaned_data['ConfirmPassword']
            fr=Farmer.objects.filter(Email=email).exists()
            if fr:
                msg="Farmer with same email is already exist!"
                args={'form':form,'error':msg}
                return render(request,'ontology/farmer_reg.html',args)
            elif password!=confirmpassword:
                msg="Enter correct password! passwword mismatch"
                args={'form':form,'error':msg}
                return render(request,'ontology/farmer_reg.html',args)
            else:
                res=Farmer(Firstame=firstname,Lastname=lastname,Gender=gender,Address=address,Email=email,Place=place,Photo=photo,
                           Phone=phone,Village=village,District=district,Password=password,ConfirmPassword=confirmpassword)
                res.save()
                return redirect('ontology:farmer_reg')
    else:
        form=FarmerRegForm()
    return render(request,'ontology/farmer_reg.html',{'form':form})


def dealer_reg(request):
    if request.method=='POST':
        form=DealerRegForm(request.POST,request.FILES)
        if form.is_valid():
            firstname=form.cleaned_data['FirstName']
            lastname=form.cleaned_data['LastName']
            email=form.cleaned_data['Email']
            phone=form.cleaned_data['Phone']
            photo=form.cleaned_data['Photo']
            place=form.cleaned_data['Place']
            password=form.cleaned_data['Password']
            confirmpassword=form.cleaned_data['ConfirmPassword']
            fr=Dealer.objects.filter(Email=email).exists()
            if fr:
                msg="Farmer with same email is already exist!"
                args={'form':form,'error':msg}
                return render(request,'ontology/dealer_reg.html',args)
            elif password!=confirmpassword:
                msg="Enter correct password! passwword mismatch"
                args={'form':form,'error':msg}
                return render(request,'ontology/dealer_reg.html',args)
            else:
                res=Dealer(FirstName=firstname,LastName=lastname,Email=email,Photo=photo,Phone=phone,Place=place,
                            Password=password,ConfirmPassword=confirmpassword)
                res.save()
                messages.success(request,"Registered successfully")
                return redirect('ontology:dealer_reg')
    else:
        form=DealerRegForm()
    return render(request,'ontology/dealer_reg.html',{'form':form})


def farmer_login(request):
    if request.method=='POST':
        form=FarmerLoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            try:
                fr=Farmer.objects.get(Email=email,Status=True)
                if not fr:
                    msg="Incorrect Email or password!"
                    args={'form':form,'error':msg}
                    return render(request,'ontology/farmer_login.html',args)
                elif password!=fr.Password:
                    msg="Incorrect Email or Password"
                    args={'form':form,'error':msg}
                    return render(request,'ontology/farmer_login.html',args)
                else:
                    request.session['email'] = email
                    request.session['sid']=fr.id
                    return redirect('/farmer_home/%s' % fr.id)
            except:
                msg = "Incorrect Email or password!"
                args = {'form': form, 'error': msg}
                return render(request, 'ontology/farmer_login.html', args)
    else:
        form=FarmerLoginForm()
    returnrender(request,'ontology/farmer_login.html',{'form':form})


def dealer_login(request):
    if request.method=='POST':
        form=DealerLoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            try:
                fr=Dealer.objects.get(Email=email,Status=True)
                if not fr:
                    msg="Incorrect Email or password!"
                    args={'form':form,'error':msg}
                    return render(request,'ontology/dealer_login.html',args)
                elif password!=fr.Password:
                    msg="Incorrect Email or Password"
                    args={'form':form,'error':msg}
                    return render(request,'ontology/dealer_login.html',args)
                else:
                    request.session['email'] = email
                    request.session['sid']=fr.id
                    return redirect('/dealer_home/%s' % fr.id)
            except:
                msg = "Incorrect Email or password!"
                args = {'form': form, 'error': msg}
                return render(request, 'ontology/dealer_login.html', args)
    else:
        form=DealerLoginForm()
    return render(request,'ontology/dealer_login.html',{'form':form})


def dealer_home(request,id):
    if request.session.has_key:
        email = request.session['email']
        farmer_id=request.session['sid']
        fr=Dealer.objects.get(Email=email)
        return render(request,'ontology/dealer_home.html',{'far':fr})


def add_subcategory(request,id):
    sid = request.session['sid']
    far = Dealer.objects.get(id=sid)
    if request.method=='POST':
        form=SubcategoryForm(request.POST,request.FILES)
        if form.is_valid():
            cate=form.cleaned_data['Category']
            name=form.cleaned_data['Name']
            photo=form.cleaned_data['Photo']
            res=Subcategory(Category=cate,Name=name,Photo=photo)
            res.save()
            msg="Added Successfuly"
            return render(request,'ontology/add_subcategory.html',{'form':form,'far':far,'msg':msg})
    else:
        form=SubcategoryForm()
    return render(request, 'ontology/add_subcategory.html', {'form': form, 'far': far})


def select_category(request,id):
    sid = request.session['sid']
    far = Dealer.objects.get(id=sid)
    category=Category.objects.all()
    return render(request,'ontology/select_category.html',{'category':category,'far':far})


def select_subcategory(request,id):
    sid = request.session['sid']
    far = Dealer.objects.get(id=sid)
    cat = request.POST.get('Category')
    request.session['cat']=cat
    sub=Subcategory.objects.filter(Category=cat)
    subcat =request.POST.get('Subcategory')
    if subcat:
        subcat=Subcategory.objects.filter(id=subcat)
        return redirect('/add_product/%s' % subcat)
    return render(request,'ontology/select_subcategory.html',{'far':far,'category':cat,'sub':sub})


def add_product(request,id):
    form = AddProductForm()
    cat=request.session['cat']
    subcat=request.POST.get('Subcategory')
    sub=Subcategory.objects.get(id=id)
    category=Category.objects.get(id=cat)
    sid=request.session['sid']
    dealer=Dealer.objects.get(id=sid)
    if request.method=='POST':
        form=AddProductForm(request.POST,request.FILES)
        if form.is_valid():
            name=form.cleaned_data['Name']
            price=form.cleaned_data['Price']
            rent_amount=form.cleaned_data['Rent_Amount']
            quantity=form.cleaned_data['Quantity']
            photo=form.cleaned_data['Photo']
            use=form.cleaned_data['Use']
            res=Product(OwnerId=sid,OwnerName=dealer.FirstName,Category=category,Subcategory=sub,Name=name,Price=price,Rent_Amount=rent_amount,
                        Quantity=quantity,Photo=photo,Use=use)
            res.save()
            messages.success(request,"Product added!")
            msg = "Product added Successfully"
            return render(request, 'ontology/add_product.html', {'form': form,'category':category, 'far': dealer, 'msg': msg})
    else:
        form=AddProductForm()
    return render(request,'ontology/add_product.html',{'form':form,'far':dealer,'sub':sub})


def view_all_products(request):
    sid=request.session['sid']
    dealer=Dealer.objects.get(id=sid)
    product=Product.objects.filter(OwnerId=dealer.id,OwnerName=dealer.FirstName)
    return render(request,'ontology/view_all_products.html',{'far':dealer,'product':product})


def update_product_stock(request,id):
    sid = request.session['sid']
    dealer = Dealer.objects.get(id=sid)
    product=Product.objects.get(id=id)
    form=AddProductForm(request.POST or None,instance=product)
    if form.is_valid():
        form.save()
        return redirect('/view_all_products')
    return render(request,'ontology/update_product_stock.html',{'form':form,'product':product,'far':dealer})


def delete_dealer_product(request,id):
    sid = request.session['sid']
    dealer = Dealer.objects.get(id=sid)
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('/view_all_products')


def add_dealer_notification(request,id):
    dealer=Dealer.objects.get(id=id)
    if request.method=='POST':
        form=DealerNotificationForm(request.POST)
        if form.is_valid():
            notification=form.cleaned_data['Notification']
            res=DealerNotification(DealerId=dealer,Notification=notification)
            res.save()
            messages.success(request,"Notification added successfully")
            msg="Notification added successfully"
            return render(request, 'ontology/add_dealer_notification.html', {'far': dealer, 'error':msg,'form': form})
    else:
        form=DealerNotificationForm()
    return render(request,'ontology/add_dealer_notification.html',{'far':dealer,'form':form})


def view_all_payment_detail(request):
    sid=request.session['sid']
    dealer=Dealer.objects.get(id=sid)
    prod = Order.objects.filter(Dealer_id=sid,Status='Pending')
    return render(request, 'ontology/view_all_payment_detail.html', {'far': dealer, 'prod': prod})


def approve_order(request,id):
    prod = Order.objects.get(id=id)
    prod.Status='Approved'
    prod.save()
    return redirect('/view_all_payment_detail')


def reject_order(request,id):
    prod = Order.objects.get(id=id)
    prod.Status='Rejected'
    prod.save()
    return redirect('/view_all_payment_detail')


def view_all_delivery_status(request):
    sid = request.session['sid']
    dealer = Dealer.objects.get(id=sid)
    prod = Order.objects.filter(Dealer_id=sid, Status='Approved')
    return render(request,'ontology/view_all_delivery_status.html',{'far':dealer, 'prod':prod})


def product_delivered(request,id):
    prod = Order.objects.get(id=id)
    prod.Delivery_status='Delivered'
    prod.save()
    return redirect('/view_all_delivery_status')


def product_not_delivered(request,id):
    prod = Order.objects.get(id=id)
    prod.Delivery_status='pending'
    prod.save()
    return redirect('/view_all_delivery_status')


def dealer_view_notification(request):
    sid = request.session['sid']
    dealer = Dealer.objects.get(id=sid)
    notification=KnowledgeCenterNotification.objects.all()
    return render(request,'ontology/dealer_view_notification.html',{'far':dealer,'notification':notification})


def view_dealer_profile(request,id):
    dealer=Dealer.objects.get(id=id)
    form=DealerUpdateForm(request.POST or None,instance=dealer)
    if form.is_valid():
        firstname = form.cleaned_data['FirstName']
        lastname = form.cleaned_data['LastName']
        email=form.cleaned_data['Email']
        place=form.cleaned_data['Place']
        photo=form.cleaned_data['Photo']
        phone=form.cleaned_data['Phone']
        res=Dealer(id=id,FirstName=firstname,LastName=lastname,Email=email,Place=place,Photo=photo,Phone=phone,Password=dealer.Password,
                   ConfirmPassword=dealer.ConfirmPassword,Status=dealer.Status)
        res.save()
        messages.success(request, "Updated Successfully!")
        return redirect('/dealer_home/%s' % id)
    return render(request, 'ontology/view_dealer_profile.html', {'form': form, 'far': dealer})


def dealer_change_password(request,id):
    fid = request.session['sid']
    dealer = Dealer.objects.get(id=id)
    if request.method=='POST':
        form=ChangePassForm(request.POST)
        if form.is_valid():
            old=form.cleaned_data['OldPassword']
            new=form.cleaned_data['Password']
            c_new=form.cleaned_data['ConfirmPassword']
            if old!=dealer.Password:
                msg="Invalid Password! enter Your correct password"
                args={'error':msg,'form':form,'far':dealer}
                return render(request,'ontology/dealer_change_password.html', args)
            elif new!=c_new:
                msg = "Password Missmatch"
                args = {'error': msg, 'form': form,'far':dealer}
                return render(request, 'ontology/dealer_change_password.html', args)
            else:
                dealer.Password=new
                dealer.ConfirmPassword=c_new
                dealer.save()
                msg = "Password Changed"
                args = {'error': msg, 'form': form,'far':dealer}
                return render(request, 'ontology/dealer_change_password.html', args)
    else:
        form=ChangePassForm()
    return render(request, 'ontology/dealer_change_password.html',{'form': form,'far':dealer})


def farmer_home(request,id):
    if request.session.has_key:
        email = request.session['email']
        farmer_id=request.session['sid']
        fr=Farmer.objects.get(Email=email)
        return render(request,'ontology/farmer_home.html',{'far':fr})


def logout(request):
    try:
        del request.session['email']
        return redirect('/')
    except:
        pass


def view_farmer_profile(request,id):
    email = request.session['email']
    farmer=Farmer.objects.get(id=id)
    form=FarmerUpdateForm(request.POST or None,instance=farmer)
    if form.is_valid():
        firstname=form.cleaned_data['Firstame']
        lastname=form.cleaned_data['Lastname']
        gender=form.cleaned_data['Gender']
        address=form.cleaned_data['Address']
        email=form.cleaned_data['Email']
        place=form.cleaned_data['Place']
        photo=form.cleaned_data['Photo']
        phone=form.cleaned_data['Phone']
        village=form.cleaned_data['Village']
        district=form.cleaned_data['District']
        res=Farmer(id=id,Firstame=firstname,Lastname=lastname,Gender=gender,Address=address,Email=email,Place=place,Phone=phone,
                   Photo=photo,Village=village,District=district,Password=farmer.Password,ConfirmPassword=farmer.ConfirmPassword,Status=farmer.Status)
        res.save()
        messages.success(request,"Updated Successfully!")
        return redirect('/farmer_home/%s' %id)
    return render(request,'ontology/view_farmer_profile.html',{'form':form,'far':farmer})


def view_services(request,id):
    email = request.session['email']
    far = Farmer.objects.get(id=id)
    service=KnowledgeCenterService.objects.all()
    return render(request,'ontology/view_services.html',{'services':service,'far':far})


def view_product_cat(request):
    fid=request.session['sid']
    far=Farmer.objects.get(id=fid)
    category=Category.objects.all()
    return render(request,'ontology/view_product_cat.html',{'far':far,'category':category})


def view_product_sub_cat(request,id):
    fid=request.session['sid']
    far=Farmer.objects.get(id=fid)
    category=Category.objects.get(id=id)
    sub=Subcategory.objects.filter(Category=category)
    return render(request,'ontology/view_product_sub_cat.html',{'far':far,'category':category,'sub':sub})


def show_products(request,id):
    fid = request.session['sid']
    far = Farmer.objects.get(id=fid)
    sub=Subcategory.objects.get(id=id)
    product=Product.objects.filter(Subcategory_id=id)
    return render(request,'ontology/show_products.html',{'far':far,'sub':sub,'product':product})


def show_single_product(request,id):
    fid = request.session['sid']
    far = Farmer.objects.get(id=fid)
    product=Product.objects.get(id=id)
    return render(request, 'ontology/show_single_product.html', {'far': far,'product': product})


def farmer_buy_product(request,id):
    fid = request.session['sid']
    farmer = Farmer.objects.get(id=fid)
    product = Product.objects.get(id=id)
    dealer=Dealer.objects.get(id=product.OwnerId)
    quantity=int(request.POST.get('quantity'))
    pay_type=request.POST.get('type')
    price=product.Price
    total =quantity * price
    res=Order(Product=product,Farmer=farmer,Dealer=dealer,Quantity=quantity,Total_Amount=total,Type=pay_type)
    res.save()
    product.Quantity=product.Quantity - quantity
    product.save()
    if pay_type=='standared':
        args={'far':farmer,'product':product,'dealer':dealer,'quantity':quantity,'price':price,'total':total}
        return render(request,'ontology/farmer_buy_product.html',args)
    elif pay_type=='online':
        request.session['amount'] = total
        return redirect('/make_payment/%s' % id)
    else:
        return HttpResponse("Must Select Type Delivery")


def make_payment(request,id):
    fid = request.session['sid']
    farmer = Farmer.objects.get(id=fid)
    product = Product.objects.get(id=id)
    amount=request.session['amount']
    return render(request,'ontology/make_payment.html',{'far':farmer,'amount':amount,'product':product})


def payed(request,id):
    fid = request.session['sid']
    farmer = Farmer.objects.get(id=fid)
    product = Product.objects.get(id=id)
    amount = request.session['amount']
    return render(request, 'ontology/payed.html', {'far': farmer, 'amount': amount, 'product': product})


def rent_equipments(request):
    fid = request.session['sid']
    far = Farmer.objects.get(id=fid)
    category=Category.objects.filter(Name='Equipments')
    product=Product.objects.filter(Category_id=4)
    args={'far':far,'category':category,'product':product}
    return render(request,'ontology/rent_equipments.html',args)


def show_single_equipments(request,id):
    fid = request.session['sid']
    far = Farmer.objects.get(id=fid)
    product=Product.objects.get(id=id)
    return render(request,'ontology/show_single_equipments.html',{'far': far,'product': product})


def farmer_rent_equipments(request,id):
    fid = request.session['sid']
    far = Farmer.objects.get(id=fid)
    product = Product.objects.get(id=id)
    dealer=Dealer.objects.get(id=product.OwnerId)
    num_of_days=int(request.POST.get('days'))
    return_date=request.POST.get('date')
    Rent_Amount=product.Rent_Amount
    total=num_of_days * Rent_Amount
    res=Rent(Product=product,Farmer=far,No_of_Days=num_of_days,Total_Amount=total,Rent_Date=date.today(),
             Return_Date=return_date)
    res.save()
    args={'far':far,'product':product,'dealer':dealer,'num_of_days':num_of_days,'Rent_Amount':Rent_Amount,'total':total,'return_date':return_date}
    return render(request,'ontology/farmer_rent_equipments.html',args)


def send_complaint(request,id):
    fid = request.session['sid']
    far = Farmer.objects.get(id=id)
    if request.method=='POST':
        form=ComplaintForm(request.POST)
        if form.is_valid():
            complaint=form.cleaned_data['complaint']
            try:
                res=Complaint(farmer=far,complaint=complaint,c_date=date.today())
                res.save()
                msg="Complaint send!"
                return render(request,'ontology/send_complaint.html', {'form': form, 'far': far,'error':msg})
            except:
                pass
    else:
        form=ComplaintForm()
    return render(request,'ontology/send_complaint.html',{'form':form,'far':far})


def farmer_view_replay(request,id):
    fid = request.session['sid']
    far = Farmer.objects.get(id=id)
    complaint=Complaint.objects.filter(farmer=far)
    return render(request,'ontology/farmer_view_replay.html',{'complaint':complaint,'far':far})


def add_question(request,id):
    fid = request.session['sid']
    far = Farmer.objects.get(id=fid)
    product = Product.objects.get(id=id)
    if request.method=='POST':
        form=QuestionForm(request.POST)
        if form.is_valid():
            question=form.cleaned_data['question']
            res=Question(farmer=far,product=product,question=question,que_date=date.today())
            res.save()
            messages.success(request,'Question Send Successfully!')
            msg="Question Send Successfully!"
            return render(request, 'ontology/add_question.html', {'form': form, 'far': far,'error':msg, 'product': product})
    else:
        form=QuestionForm()
    return render(request,'ontology/add_question.html',{'form':form,'far':far,'product':product})


def farmer_view_question_replay(request,id):
    fid = request.session['sid']
    far = Farmer.objects.get(id=id)
    question=Question.objects.filter(farmer=far)
    return render(request,'ontology/farmer_view_question_replay.html',{'question':question,'far':far})


def farmer_view_payment_detail(request):
    fid = request.session['sid']
    far = Farmer.objects.get(id=fid)
    prod=Order.objects.filter(Farmer_id=fid)
    return render(request,'ontology/farmer_view_payment_detail.html',{'far':far,'prod':prod})


def farmer_view_notification(request):
    fid = request.session['sid']
    far = Farmer.objects.get(id=fid)
    d_noti=DealerNotification.objects.all()
    k_noti=KnowledgeCenterNotification.objects.all()
    return render(request,'ontology/farmer_view_notification.html',{'far':far,'d_noti':d_noti,'k_noti':k_noti})


def farmer_change_password(request,id):
    fid = request.session['sid']
    farmer = Farmer.objects.get(id=id)
    if request.method=='POST':
        form=ChangePassForm(request.POST)
        if form.is_valid():
            old=form.cleaned_data['OldPassword']
            new=form.cleaned_data['Password']
            c_new=form.cleaned_data['ConfirmPassword']
            if old!=farmer.Password:
                msg="Invalid Password! enter Your correct password"
                args={'error':msg,'form':form,'far':farmer}
                return render(request,'ontology/farmer_change_password.html', args)
            elif new!=c_new:
                msg = "Password Missmatch"
                args = {'error': msg, 'form': form,'far':farmer}
                return render(request, 'ontology/farmer_change_password.html', args)
            else:
                farmer.Password=new
                farmer.ConfirmPassword=c_new
                farmer.save()
                msg = "Password Changed"
                args = {'error': msg, 'form': form,'far':farmer}
                return render(request, 'ontology/farmer_change_password.html', args)
    else:
        form=ChangePassForm()
    return render(request, 'ontology/farmer_change_password.html',{'form': form,'far':farmer})


def contact_dealer(request,id):
    fid = request.session['sid']
    farmer = Farmer.objects.get(id=id)
    return render(request,'ontology/contact_dealer.html',{'far':farmer})


def contact_knowledge_center(request,id):
    fid = request.session['sid']
    farmer = Farmer.objects.get(id=id)
    return render(request,'ontology/contact_knowledge_center.html',{'far':farmer})


def contact_send(request,id):
    fid = request.session['sid']
    farmer = Farmer.objects.get(id=id)
    return render(request,'ontology/contact_send.html',{'far':farmer})
