from django.shortcuts import render,redirect 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
# . is used means in the same folder
# Create your views here.
 
def register(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            messages.success(request, f'Your account is created! You are ready to Login')
            return redirect('login')
    else:    
        form = UserRegisterForm()
    # in http there are diff types of request most basic ones are get and post,in post request 
    # we validate the data whereas in get request we send when we navigate to the page
    
    return render(request,'users/register.html',{'form':form})
# messages.debug
# messages.succes
# messages.warning
# messages.error
# messages.info
# decorator used so that we see the profile page only when we are logged in
@login_required
def profile(request):
    if request.method =='POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES ,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()   
            p_form.save()    
            messages.success(request, f'Your account is Updated')
            return redirect('profile')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)
    
    context={
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request,'users/profile.html',context)
