from django.contrib import admin
from django.urls import path
from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.db.models import Count
from django.utils.html import format_html


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    # Specify the fields to be displayed in the admin list view
    list_display = (
        "title",
        "description",
        "category",  # <-- work with the __str__ method
        "category_name",  # <-- bind with a custom method. category__name will not work
        "fullname",
        "get_comments_count",
        "view_details_link",
    )  # Replace with your actual field names
    search_fields = ("title",)
    list_filter = (
        "status",
        "title",
    )
    actions = ("set_post_to_publish",)
    ordering = ("-created_at",)

    def category_name(self, obj):
        # Access the related category's name
        return obj.category.name if obj.category else "No Category"

    category_name.short_description = "Category Name"  # Column header name

    def set_post_to_publish(self, request, queryset):
        count = queryset.update(status="P")
        self.message_user(request, f"{count} blogs are published successfully")

    set_post_to_publish.short_description = "mark selected as published"

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.select_related("category")
        return queryset.annotate(comments_count=Count("comment"))

    def get_comments_count(self, obj):
        return obj.comments_count  # Access the annotated field

    def fullname(self, obj):
        return obj.title + " " + str(obj.description)

    # custom view
    def view_details_link(self, obj):
        # Generate the link to the custom detail page
        return format_html(
            '<a href="{}">View Details</a>', f"/admin/app/post/{obj.id}/view_details/"
        )

    view_details_link.short_description = "Details"  # Column header name

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                "<int:object_id>/view_details/",
                self.admin_site.admin_view(self.view_details),
                name="view_post_details",
            ),
        ]
        return custom_urls + urls

    def view_details(self, request, object_id):
        post = get_object_or_404(Post, pk=object_id)
        related_data = self.get_related_data(post)

        context = dict(
            self.admin_site.each_context(request), post=post, related_data=related_data
        )
        return render(request, "admin/app/view_post_details.html", context)

    def get_related_data(self, post):
        # Custom logic to gather related data for the detail view
        return {
            "category": post.category,
            # Add other related data as needed
        }


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
