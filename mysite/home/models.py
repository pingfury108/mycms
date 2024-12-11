from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel


def get_pages(context):
    context["works_cases_page"] = WorksCasesPage.objects.first()
    context["news_page"] = NewsPage.objects.first()
    context["about_page"] = AboutPage.objects.first()
    context["contact_us_page"] = ContactUsPage.objects.first()
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
    class Meta:
        verbose_name = "首页"

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["news"] = NewsItemPage.objects.all()[:2]
        context["news_all"] = NewsItemPage.objects.all()

        context["team_image"] = AboutPage.objects.first().team_image

        return context


class WorksCasesPage(MyPage):
    class Meta:
        verbose_name = "作品案例"

    subpage_types = ["CaseItemPage"]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["items"] = CaseItemPage.objects.all()

        return context


class PageGalleryImage(ClusterableModel):
    page = ParentalKey("CaseItemPage", on_delete=models.CASCADE, related_name="images")
    image = models.ForeignKey(
        "wagtailimages.Image", on_delete=models.CASCADE, related_name="+"
    )
    caption = models.CharField(max_length=250, blank=True)
    describe = models.CharField(max_length=250, blank=True)

    panels = [FieldPanel("image"), FieldPanel("caption"), FieldPanel("describe")]


class CaseItemPage(MyPage):
    class Meta:
        verbose_name = "作品案例详情"

    industry = models.CharField(max_length=250, blank=True)
    describe = models.CharField(max_length=250, blank=True)
    body = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel("describe"),
        FieldPanel("industry"),
        FieldPanel("body"),
        InlinePanel("images", label="Images"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        return context


class NewsPage(MyPage):
    class Meta:
        verbose_name = "新闻动态"

    subpage_types = ["NewsItemPage"]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["news_all"] = NewsItemPage.objects.all()

        return context


class NewsItemPage(MyPage):
    class Meta:
        verbose_name = "新闻动态详情"

    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    body = RichTextField(blank=True)
    content_panels = Page.content_panels + [FieldPanel("body"), FieldPanel("image")]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["news_all"] = NewsItemPage.objects.all()

        return context


class LogGalleryImage(ClusterableModel):
    page = ParentalKey("AboutPage", on_delete=models.CASCADE, related_name="logos")
    image = models.ForeignKey(
        "wagtailimages.Image", on_delete=models.CASCADE, related_name="+"
    )
    caption = models.CharField(max_length=250, blank=True)

    panels = [FieldPanel("image"), FieldPanel("caption")]


class AboutPage(MyPage):
    class Meta:
        verbose_name = "关于我们"

    body = RichTextField(blank=True)

    team_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
        FieldPanel("team_image"),
        InlinePanel("logos", label="Logos"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["logos"] = LogGalleryImage.objects.all()

        return context


class ContactUsPage(MyPage):
    class Meta:
        verbose_name = "联系我们"

    body = RichTextField(blank=True)

    qrcode_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    tel = models.CharField(max_length=250, blank=True)
    mobile = models.CharField(max_length=250, blank=True)
    addr = models.CharField(max_length=250, blank=True)
    email = models.CharField(max_length=250, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("body"),
        FieldPanel("addr"),
        FieldPanel("qrcode_image"),
        FieldPanel("tel"),
        FieldPanel("mobile"),
        FieldPanel("email"),
    ]


class IndustryCasesPage(MyPage):
    class Meta:
        verbose_name = "行业案例"

    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]


class CopywriterPage(MyPage):
    class Meta:
        verbose_name = "文案策划"

    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]


class BrandDesignPage(MyPage):
    class Meta:
        verbose_name = "品牌设计"

    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]


class MeetingPlanningPage(MyPage):
    class Meta:
        verbose_name = "会议策划"

    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]
