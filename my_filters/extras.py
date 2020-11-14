from django import template

register = template.Library()

def discount(price, discount):
    return price - (price * discount / 100)

register.filter('discount', discount)