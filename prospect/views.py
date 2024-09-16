from .models import Prospect
from .forms import ProspectForm
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse


# Create your views here.
class ProspectList(generic.ListView):
    """
    The view handles the presentations of all the prospects
    in the database
    """
    queryset = Prospect.objects.all().order_by('company')
    template_name = "prospect/prospect_list.html"
    paginate_by = 15


def prospect_detail(request, id):
    """
    The view handles the display of a prospect record
    detail
    """
    prospect = get_object_or_404(Prospect, pk=id)
    # Collect the prospect id and save it
    # to be accessed later by other views
    request.session['prospect_id'] = id

    return render(
        request,
        "prospect/prospect_detail.html",
        {"prospect": prospect}
    )


def prospect_create(request):
    """
    This view handles two requests: Get and Post
    If Post, it handles the creation of new
    prospect and save it to the database
    """
    if request.method == 'POST':
        prospect_create = ProspectForm(request.POST)
        if prospect_create.is_valid():
            prospect = prospect_create.save(commit=False)
            prospect.owner = request.user
            prospect.save()
            return JsonResponse(
                {
                    'success': True,
                    'message': 'The new prospect is successfully saved!'
                }
            )
        else:
            for field, errors in prospect_create.errors.as_data().items():
                for error in errors:
                    prospect_field_name = " ".join(
                        part.capitalize() for part in field.split("_")
                    )
                    if error.code == 'required':
                        return JsonResponse(
                            {
                                'success': False,
                                'message':
                                f"""
                                The prospect {prospect_field_name}
                                field is required!
                                Please try again!
                                """
                            }
                        )
                    elif error.code == 'unique':
                        return JsonResponse(
                            {
                                'success': False,
                                'message':
                                f"""
                                This prospect {prospect_field_name}
                                already exists!
                                """
                            }
                        )
                    else:
                        return JsonResponse(
                            {
                                'success': False,
                                'message':
                                f"""
                                The prospect {prospect_field_name}
                                has the following error: {error}!
                                """
                            }
                        )
    else:
        prospect_create = ProspectForm()
        return render(
            request,
            'prospect/prospect_create.html',
            {
                'prospect_create': prospect_create
            }
        )


def prospect_edit(request):
    """
    This view handles a Post request for updating
    any of the prospect fields
    """
    if request.method == 'POST':
        prospect_id = request.session.get('prospect_id', 'Default Value')
        prospect = get_object_or_404(Prospect, pk=prospect_id)
        prospect_edit = ProspectForm(request.POST, instance=prospect)
        f_condition = prospect_edit.is_valid()
        s_condition = prospect.owner == request.user
        t_condition = request.user.is_superuser
        if f_condition and (s_condition or t_condition):
            prospect = prospect_edit.save(commit=False)
            prospect.save()
            return JsonResponse(
                {
                    'success': True,
                    'message': 'The prospect is successfully updated!'
                }
            )
        elif ((f_condition and not s_condition) or
              (f_condition and not t_condition)):
            return JsonResponse(
                {
                    'success': False,
                    'message': 'Update denied, unauthorized user'
                }
            )
        else:
            for field, errors in prospect_edit.errors.as_data().items():
                for error in errors:
                    prospect_field_name = " ".join(
                        part.capitalize() for part in field.split("_")
                    )
                    if error.code == 'required':
                        return JsonResponse(
                            {
                                'success': False,
                                'message':
                                f"""
                                The prospect {prospect_field_name}
                                field is required!
                                Please try again!
                                """
                            }
                        )
                    elif error.code == 'unique':
                        return JsonResponse(
                            {
                                'success': False,
                                'message':
                                f"""
                                This prospect {prospect_field_name}
                                already exists!
                                """
                            }
                        )
                    else:
                        return JsonResponse(
                            {
                                'success': False,
                                'message':
                                f"""
                                The prospect {prospect_field_name}
                                has the following error: {error}!
                                """
                            }
                        )


def prospect_delete(request):
    """
    This view handles the delete request of
    a prospect
    """
    prospect_id = request.session.get('prospect_id', 'Default Value')
    prospect = get_object_or_404(Prospect, pk=prospect_id)
    f_condition = prospect.owner == request.user
    s_condition = request.user.is_superuser

    if f_condition or s_condition:
        prospect.delete()
        return JsonResponse(
            {
                'success': True,
                'message': 'The Prospect is successfully deleted'
            }
        )
    else:
        return JsonResponse(
            {
                'success': False,
                'message': 'Deletion denied, unauthorized user'
            }
        )
