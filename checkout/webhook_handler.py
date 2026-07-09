from django.http import HttpResponse
from .models import Order, OrderLineItem
from lootboxes.models import Product
from django.conf import settings
from profiles.models import UserProfile

import json
import time


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id

        backpack = '{}'
        if 'backpack' in intent.metadata:
            backpack = intent.metadata['backpack']

        username = intent.metadata.get('username')
        save_info = intent.metadata.get('save_info') == 'True'

        if hasattr(intent, 'charges') and intent.charges.data:
            charge = intent.charges.data[0]
        else:
            import stripe
            stripe.api_key = settings.STRIPE_SECRET_KEY
            charge = stripe.Charge.retrieve(intent.latest_charge)

        billing_details = charge.billing_details
        shipping_details = intent.shipping
        grand_total = round(charge.amount / 100, 2)

        if shipping_details is not None:
            for field, value in shipping_details.address.items():
                if value == "":
                    shipping_details.address[field] = None
        else:
            shipping_details = billing_details

        order_exists = False
        attempt = 1

        # Try to find the order 5 times over 5 seconds
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone if hasattr(shipping_details, 'phone') else billing_details.phone,   # noqa: E501
                    country__iexact=shipping_details.address.country if hasattr(shipping_details, 'address') and shipping_details.address else billing_details.address.country,   # noqa: E501
                    postcode__iexact=shipping_details.address.postal_code if hasattr(shipping_details, 'address') and shipping_details.address else billing_details.address.postal_code,   # noqa: E501
                    town_or_city__iexact=shipping_details.address.city if hasattr(shipping_details, 'address') and shipping_details.address else billing_details.address.city,   # noqa: E501
                    street_address1__iexact=shipping_details.address.line1 if hasattr(shipping_details, 'address') and shipping_details.address else billing_details.address.line1,   # noqa: E501
                    street_address2__iexact=shipping_details.address.line2 if hasattr(shipping_details, 'address') and shipping_details.address else billing_details.address.line2,   # noqa: E501
                    county__iexact=shipping_details.address.state if hasattr(shipping_details, 'address') and shipping_details.address else billing_details.address.state,   # noqa: E501
                    grand_total=grand_total,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)

        if order_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database', status=200)   # noqa: E501
        else:
            order = None
            try:
                # Fallback: Browser crashed, create the order from Stripe data
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    email=billing_details.email,
                    phone_number=shipping_details.phone if hasattr(shipping_details, 'phone') else billing_details.phone,   # noqa: E501
                    country=shipping_details.address.country if hasattr(shipping_details, 'address') and shipping_details.address else billing_details.address.country,   # noqa: E501
                    postcode=shipping_details.address.postal_code if hasattr(shipping_details, 'address') and shipping_details.address else billing_details.address.postal_code,   # noqa: E501
                    town_or_city=shipping_details.address.city if hasattr(shipping_details, 'address') and shipping_details.address else billing_details.address.city,   # noqa: E501
                    street_address1=shipping_details.address.line1 if hasattr(shipping_details, 'address') and shipping_details.address else billing_details.address.line1,   # noqa: E501
                    street_address2=shipping_details.address.line2 if hasattr(shipping_details, 'address') and shipping_details.address else billing_details.address.line2,   # noqa: E501
                    county=shipping_details.address.state if hasattr(shipping_details, 'address') and shipping_details.address else billing_details.address.state,   # noqa: E501
                    stripe_pid=pid,
                )
                # Reconstruct the order lines
                # from the backpack metadata json string
                for item_id, item_data in json.loads(backpack).items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()

                profile = None
                if username and username != 'AnonymousUser':
                    profile = UserProfile.objects.get(user__username=username)
                    if save_info:
                        profile.default_phone_number = shipping_details.phone   # noqa: E501
                        profile.default_country = shipping_details.address.country   # noqa: E501
                        profile.default_postcode = shipping_details.address.postal_code   # noqa: E501
                        profile.default_town_or_city = shipping_details.address.city   # noqa: E501
                        profile.default_street_address1 = shipping_details.address.line1   # noqa: E501
                        profile.default_street_address2 = shipping_details.address.line2   # noqa: E501
                        profile.default_county = shipping_details.address.state
                        profile.save()

            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)

        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',   # noqa: E501
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
