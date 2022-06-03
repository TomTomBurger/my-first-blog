from extra_views import ModelFormSetView
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .models import Member
from .forms import MemberUpdateForm

class ListUpdateView(ModelFormSetView):
    model = Member
    template_name = 'member_list.html'
    form_class = MemberUpdateForm

def member_remove(request, pk):
    member = get_object_or_404(Member, pk=pk)
    member.delete()
    return redirect('update_sample')