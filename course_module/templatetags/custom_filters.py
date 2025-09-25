from django import template

register = template.Library()

@register.filter
def smart_price(value):
    try:
        value = int(value)
        if value < 1_000_000:
            return f"{value // 1000:,} هزار تومان"
        else:
            price_in_million = value / 1_000_000
            if price_in_million.is_integer():
                return f"{int(price_in_million)} میلیون تومان"

            elif str(price_in_million).split(".")[1][0] != "0" and len(str(price_in_million).split(".")[1]) == 1:
                return f"{price_in_million:.1f} میلیون تومان"


            return f"{price_in_million:.2f} میلیون تومان"
    except (ValueError, TypeError):
        return value
