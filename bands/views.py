from django.shortcuts import render, get_object_or_404
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
