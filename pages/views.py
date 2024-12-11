from django.views.generic import TemplateView


class HomePageView(TemplateView):
     template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

class ProjectsView(TemplateView):
    template_name = "projects.html"

class ContactView(TemplateView):
    template_name = "contact.html"
 