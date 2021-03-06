from django.shortcuts import redirect, render
from django.views.generic import ListView, UpdateView
from .forms import CommentEditForm, ShoeboxEditForm
from Shoebox.models import Comment, Shoebox
from Useradmin.models import MyUser, get_myuser_from_user


# Create your views here.
class CommentDeleteView(ListView):
    model = Comment
    context_object_name = 'all_the_comments'
    template_name = 'comment-delete.html'

    def get_context_data(self, **kwargs):
        context = super(CommentDeleteView, self).get_context_data(**kwargs)
        can_delete = False
        user = self.request.user
        myuser_get_profile_path = None
        comment_id = self.kwargs["pk"]
        comment = Comment.objects.get(id=comment_id)
        author = MyUser.objects.get(id=comment.user_id).user.username
        if not user.is_anonymous:
            myuser = get_myuser_from_user(user)
            can_delete = myuser.is_staff()
            myuser_get_profile_path = myuser.get_profile_path()
            if comment.user == myuser:
                can_delete = True

        context['can_delete'] = can_delete
        context['myuser_get_profile_path'] = myuser_get_profile_path
        context['myuser'] = myuser
        context['author'] = author
        context['comment'] = comment
        return context

    def post(self, request, *args, **kwargs):
        comment_id = request.POST['comment_id']
        if 'delete' in request.POST:
            comment = Comment.objects.get(id=comment_id)
            shoebox_id = comment.shoebox_id
            comment.delete()
            return redirect('box-detail', bpk=shoebox_id)


def comment_edit(request, pk: str):
    comment_id = pk
    comment = Comment.objects.get(id=comment_id)
    shoebox_id = comment.shoebox_id
    if request.method == 'POST':
        print('-------------', request.POST)
        if 'edit' in request.POST:
            form = CommentEditForm(request.POST)
            print("__________________________", form.is_valid())
            if form.is_valid():
                new_text = form.cleaned_data['text']
                comment.text = new_text
                print("---------------", new_text)
                comment.save()

        return redirect('box-detail', bpk=shoebox_id)

    else:
        can_delete = False
        user = request.user
        myuser_get_profile_path = None
        comment = Comment.objects.get(id=comment_id)
        if not user.is_anonymous:
            myuser = get_myuser_from_user(user)
            can_delete = myuser.is_staff()
            if comment.user == myuser:
                can_delete = True
            myuser_get_profile_path = myuser.get_profile_path()
        form = CommentEditForm(request.POST or None, instance=comment)
        context = {'form': form,
                   'can_delete': can_delete,
                   'comment': comment,
                   "myuser": myuser,
                   'myuser_get_profile_path': myuser_get_profile_path
                  }
        return render(request, 'comment-service-edit.html', context)


def editBox(request, pk: str):
    box_id = pk
    box = Shoebox.objects.get(id=box_id)
    if request.method == 'POST':
        print('-------------', request.POST)
        if 'edit' in request.POST:
            form = ShoeboxEditForm(request.POST)
            print("__________________________", form.is_valid())
            if form.is_valid():
                print(form.cleaned_data)
                brand = form.cleaned_data['brand']
                description = form.cleaned_data['description']
                flute_layers = form.cleaned_data['flute_layers']
                flute_type = form.cleaned_data['flute_type']
                height = form.cleaned_data['height']
                length = form.cleaned_data['length']
                liner_type = form.cleaned_data['liner_type']
                name = form.cleaned_data['name']
                price = form.cleaned_data['price']
                width = form.cleaned_data['width']
                ###
                box.brand = brand
                box.description = description
                box.flute_layers = flute_layers
                box.flute_type = flute_type
                box.height = height
                box.length = length
                box.liner_type = liner_type
                box.name = name
                box.price = price
                box.width = width

                box.save()

        return redirect('box-detail', bpk=box_id)

    else:
        can_delete = False
        user = request.user
        myuser_get_profile_path = None
        myuser = None
        if not user.is_anonymous:
            myuser = get_myuser_from_user(user)
            can_delete = myuser.is_staff()
            myuser_get_profile_path = myuser.get_profile_path()
        form = ShoeboxEditForm(request.POST or None, instance=box)
        context = {'form': form,
                   'can_delete': can_delete,
                   'box': box,
                   "myuser": myuser,
                   'myuser_get_profile_path': myuser_get_profile_path
                  }
        return render(request, 'box-edit.html', context)


class CommentReportView(ListView):
    model = Comment
    context_object_name = 'all_the_comments'
    template_name = 'comment-service-reports.html'

    def get_context_data(self, **kwargs):
        context = super(CommentReportView, self).get_context_data(**kwargs)
        can_delete = False
        user = self.request.user
        myuser_get_profile_path = None
        comments = Comment.objects.filter(inappropriate=True)
        if not user.is_anonymous:
            myuser = get_myuser_from_user(user)
            can_delete = myuser.is_staff()
            myuser_get_profile_path = myuser.get_profile_path()

        context['can_delete'] = can_delete
        context['myuser_get_profile_path'] = myuser_get_profile_path
        context['myuser'] = myuser
        context['comments'] = comments
        return context

