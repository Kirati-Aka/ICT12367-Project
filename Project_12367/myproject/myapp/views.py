from django.shortcuts import render, redirect, get_object_or_404
from .models import Poll, Option

def home(request):
    polls = Poll.objects.all().prefetch_related('options')
    for poll in polls:
        total_votes = sum(option.votes for option in poll.options.all())
        poll.total_votes = total_votes
        for option in poll.options.all():
            option.percentage = round((option.votes / total_votes) * 100, 1) if total_votes > 0 else 0
    return render(request, 'index.html', {'polls': polls})


def create_poll(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        question = request.POST.get('question')
        options = request.POST.getlist('option[]')

        if title and question and len(options) >= 2:
            poll = Poll.objects.create(title=title, question=question)
            for opt in options:
                Option.objects.create(poll=poll, text=opt)
            return redirect('/')

    return render(request, 'post.html')

def vote_poll(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)

    if request.method == "POST":
        option_id = request.POST.get("option")
        if option_id:
            option = get_object_or_404(Option, id=option_id, poll=poll)
            option.votes += 1
            option.save()
            return redirect("poll_result", poll_id=poll.id)

    return render(request, "vote.html", {"poll": poll})

def poll_result(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    return render(request, "result.html", {"poll": poll})

def edit_poll_options(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)

    if request.method == 'POST':
        if 'delete_option' in request.POST:
            option_id = request.POST['delete_option']
            option = Option.objects.filter(id=option_id, poll=poll).first()
            if option and option.votes == 0:
                option.delete()

        elif 'add_option' in request.POST:
            new_text = request.POST.get('new_option')
            if new_text:
                Option.objects.create(poll=poll, text=new_text.strip())

        elif 'save_options' in request.POST:
            for key, value in request.POST.items():
                if key.startswith("option_"):
                    option_id = key.split("_")[1]
                    option = Option.objects.filter(id=option_id, poll=poll).first()
                    if option:
                        option.text = value.strip()
                        option.save()

    return redirect('/')
