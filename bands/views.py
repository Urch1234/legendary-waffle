from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from bands.models import Musician



def musician_detail(request, musician_id):
    """
    View function to retrieve a specific musician by ID and render it in the template.

    :param request: The HTTP request object.
    :param musician_id: The ID of the musician to retrieve.
    :return: Renders the 'musician.html' template with the musician data.
    """
    musician = get_object_or_404(Musician, id=musician_id)

    data = {
        "musician": musician,
    }

    return render(request, "musician.html", data)

def musicians(request):
    all_musicians = Musician.objects.all().order_by('last_name')
    paginator = Paginator(all_musicians, 2)

    page_num = request.GET.get('page', 1)
    page_num = int(page_num)

    if page_num < 1:
        page_num = 1
    elif page_num > paginator.num_pages:
        page_num = paginator.num_pages

    page = paginator.page(page_num)
    data = {
        'musicians': page.object_list,
        'page': page,
    }

    return render(request, "musicians.html", data)
