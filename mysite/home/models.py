from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


def get_pages(context):
    context["works_cases_page"] = Page.objects.filter(title="作品案例").first()
    context["news_page"] = Page.objects.filter(title="新闻动态").first()
    context["about_page"] = Page.objects.filter(title="关于我们").first()
    context["contact_us_page"] = Page.objects.filter(title="联系我们").first()
    context["industry_cases_page"] = Page.objects.filter(title="行业案例").first()
    context["copywriter_page"] = Page.objects.filter(title="文案策划").first()
    context["brand_design_page"] = Page.objects.filter(title="品牌设计").first()
    context["meeting_planning_page"] = Page.objects.filter(title="会议策划").first()

    return context


class MyPage(Page):
    class Meta:
        abstract = True

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        get_pages(context)

        return context


class HomePage(MyPage):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]


class WorksCasesPage(MyPage):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]


class NewsPage(MyPage):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]


class AboutPage(MyPage):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]


class ContactUsPage(MyPage):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]


class IndustryCasesPage(MyPage):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]


class CopywriterPage(MyPage):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]


class BrandDesignPage(MyPage):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]


class MeetingPlanningPage(MyPage):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]
