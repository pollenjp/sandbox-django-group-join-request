# Standard Library
from typing import Any
from typing import Dict
from typing import Optional

# Third Party Library
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import Http404
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from rules.contrib.views import PermissionRequiredMixin
from rules.contrib.views import permission_required

# Local Library
from .forms import RequestPostForm
from .models import RequestPost

# from django.views.generic import DeleteView


class RequestPostListView(LoginRequiredMixin, ListView):
    model = RequestPost
    context_object_name = "posts"
    ordering = ["-id"]

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        return qs.filter(created_by=self.request.user)


class RequestPostAllListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = RequestPost
    context_object_name = "posts"
    template_name = "join_request/requestpost_list_all.html"
    permission_required = "join_request.rules_view_all_request_post"
    ordering = ["-id"]

    def get_queryset(self, *args, **kwargs):
        fileter_kwargs: Dict[str, Any] = {}
        val: Optional[str] = self.request.GET.get("is_open", None)
        if val is not None:
            if val.lower() == "true":
                fileter_kwargs["is_open"] = True
            elif val.lower() == "false":
                fileter_kwargs["is_open"] = False

        qs = super().get_queryset(*args, **kwargs)
        return qs.filter(**fileter_kwargs)


class RequestPostDetailView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    model = RequestPost
    context_object_name = "post"
    permission_required = ("join_request.rules_view_request_post_detail",)


class RequestPostCreateView(LoginRequiredMixin, CreateView):
    model = RequestPost
    form_class = RequestPostForm
    success_url = reverse_lazy("join_request_list")

    def form_valid(self, form):
        """
        ref:
            <https://docs.djangoproject.com/en/4.0/topics/class-based-views/generic-editing/#models-and-request-user>
        """
        form.instance.created_by = self.request.user
        messages.success(self.request, "Successfully saved.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Failed to save.")
        return super().form_invalid(form)


class RequestPostUpdateView(LoginRequiredMixin, UpdateView):
    model = RequestPost
    form_class = RequestPostForm
    # template_name_suffix = "_update_form"

    def get_object(self, *args, **kwargs):
        obj = super().get_object(*args, **kwargs)
        if not obj.created_by == self.request.user:
            raise Http404
        return obj

    def get_success_url(self):
        return reverse_lazy("join_request_detail", kwargs={"pk": self.kwargs["pk"]})

    def form_valid(self, form):
        messages.success(self.request, "Successfully updated.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Failed to update.")
        return super().form_invalid(form)


redirect_page_name: str = "join_request_detail"


@permission_required("join_request.rules_approve_request_post")
def approve_request_post(request, pk):
    post: RequestPost = get_object_or_404(RequestPost, pk=pk)
    post.is_open = False
    post.save()

    messages.success(request, "Successfully approved.")
    return redirect("join_request_detail", pk)


# class BlogDeleteView(LoginRequiredMixin, DeleteView):
#     model = RequestPostForm
#     success_url = reverse_lazy("index")

#     def delete(self, request, *args, **kwargs):
#         messages.success(request, message="削除しました.")
#         return super().delete(request, *args, **kwargs)
