from site_module.models import SiteSetting , FooterLinkBox




def site_footer(request):
    site_setting = SiteSetting.objects.filter(is_main_setting=True).first()
    footer_link_boxes = FooterLinkBox.objects.prefetch_related('links').all()
    return{'footer_link_boxes':footer_link_boxes, 'setting':site_setting }



    