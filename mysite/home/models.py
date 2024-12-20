from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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

    context["case_items"] = CaseItemPage.objects.filter(
        is_home_item=False,
    ).all()

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

        context["case_item_main"] = CaseItemPage.objects.filter(
            is_home_item=True, is_home_item_row=1
        ).first()

        context["case_item_row1_left"] = CaseItemPage.objects.filter(
            is_home_item=True, is_home_item_row=2, is_home_item_left=True
        ).first()

        context["case_item_row1_right"] = CaseItemPage.objects.filter(
            is_home_item=True, is_home_item_row=2, is_home_item_right=True
        ).first()

        context["case_item_row2_left"] = CaseItemPage.objects.filter(
            is_home_item=True, is_home_item_row=3, is_home_item_left=True
        ).first()

        context["case_item_row2_right"] = CaseItemPage.objects.filter(
            is_home_item=True, is_home_item_row=3, is_home_item_right=True
        ).first()

        context["case_items"] = CaseItemPage.objects.filter(
            is_home_item=False,
        ).all()[:6]

        context["news"] = NewsItemPage.objects.all()[:2]
        context["news_all"] = NewsItemPage.objects.all()

        context["team_image"] = AboutPage.objects.first().team_image

        heads = HomeTitle.objects.all()

        def a_f(x):
            return len(heads) if x == 1 else x - 1

        def b_f(x):
            return 1 if x == len(heads) else x + 1

        context["heads"] = [
            (a_f(i + 1), i + 1, b_f(i + 1), h) for i, h in enumerate(heads)
        ]

        return context


class HomeTitle(MyPage):
    class Meta:
        verbose_name = "首页头部轮播"

    text_row1 = models.CharField(max_length=250, blank=True)
    text_row2 = models.CharField(max_length=250, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("text_row1", heading="第一行文字"),
        FieldPanel("text_row2", heading="第二行文字"),
    ]


class WorksCasesPage(MyPage):
    class Meta:
        verbose_name = "作品案例"

    subpage_types = ["CaseItemPage"]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["items"] = CaseItemPage.objects.all()
        paginator = Paginator(context["items"], 15)
        page_number = request.GET.get("page")

        try:
            pages = paginator.page(page_number)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)

        context["pages"] = pages
        context["paginator"] = paginator

        return context


class PageGalleryImage(ClusterableModel):
    page = ParentalKey("CaseItemPage", on_delete=models.CASCADE, related_name="images")
    image = models.ForeignKey(
        "wagtailimages.Image", on_delete=models.CASCADE, related_name="+"
    )
    caption = models.CharField(max_length=250, blank=True)
    describe = models.CharField(max_length=250, blank=True)
    is_home = models.BooleanField(default=False)

    panels = [
        FieldPanel("image", heading="案例图片"),
        FieldPanel("caption", heading="案例图片标题"),
        FieldPanel("describe", heading="案例图片描述"),
        FieldPanel("is_home", heading="图片是否为首页展示图片"),
    ]


class CaseItemPage(MyPage):
    class Meta:
        verbose_name = "作品案例详情"

    industry = models.CharField(max_length=250, blank=True)
    describe = models.CharField(max_length=250, blank=True)
    is_home_item = models.BooleanField(default=False)
    is_home_item_row = models.IntegerField(default=0)
    is_home_item_left = models.BooleanField(default=False)
    is_home_item_right = models.BooleanField(default=False)

    body = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel("describe", heading="服务内容"),
        FieldPanel("industry", heading="所属行业"),
        FieldPanel("is_home_item", heading="是否在首页展示"),
        FieldPanel(
            "is_home_item_row", heading="首页展示行数(1 为第一行, 仅当在首页展示时可用)"
        ),
        FieldPanel("is_home_item_left", heading="是否展示在首页行左边"),
        FieldPanel("is_home_item_right", heading="是否展示在首页行右边"),
        FieldPanel("body", heading="案例描述"),
        InlinePanel("images", label="Images", heading="案例照片列表"),
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
        paginator = Paginator(context["news_all"], 5)
        page_number = request.GET.get("page")
        try:
            pages = paginator.page(page_number)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)

        context["pages"] = pages
        context["paginator"] = paginator

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
    content_panels = Page.content_panels + [
        FieldPanel("body", heading="正文"),
        FieldPanel("image", heading="图片"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["news_all"] = NewsItemPage.objects.all()

        return context


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

    logo_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
        FieldPanel("team_image", heading="团队照片"),
        FieldPanel("logo_image", heading="客户LOGO墙照片"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

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
        FieldPanel("addr", heading="地址"),
        FieldPanel("qrcode_image", heading="二维码"),
        FieldPanel("tel", heading="电话号码"),
        FieldPanel("mobile", heading="手机号码"),
        FieldPanel("email", heading="电子邮箱"),
    ]
