import stripe
import stripe.error
from course.models import Course
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpRequest, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required
def crate_checkout_session(request: HttpRequest, course_id: int):
    course = get_object_or_404(Course, pk=course_id)

    price_in_cents = int(course.price * 100)

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[
            {
                "price_data": {
                    "currency": "usd",
                    "unit_amount": price_in_cents,
                    "product_data": {
                        "name": course.title,
                    },
                },
                "quantity": 1,
            },
        ],
        mode="payment",
        success_url=request.build_absolute_uri(reverse("course_success")),
        cancel_url=request.build_absolute_uri(reverse("course_cancel")),
        metadata={
            "course_id": course_id,
            "user_id": request.user.id,
        },
    )

    return redirect(session.url)


@login_required
def order_success(request: HttpRequest):
    return redirect("order_list")


@login_required
def order_cancel(request: HttpRequest):
    return redirect("order_list")


@csrf_exempt
@require_POST
def stripe_webhook(request: HttpRequest) -> JsonResponse:
    payload = smart_str(request.body)
    sig_header = request.META["HTTP_STRIPE_SIGNATURE"]

    try:
        event = stripe.Webhook.construct_event(
            payload,
            sig_header,
            settings.STRIPE_ENDPOINT_SECRET,
        )
    except ValueError:
        return JsonResponse({"error": "Invalid payload"}, status=400)

    except stripe.error.SignatureVerificationError:
        return JsonResponse({"error": "Invalid signature"}, status=400)

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        handler_checkout_session(session)

    return JsonResponse({"status": "Success"})


def handler_checkout_session(session) -> None:
    order_id = session["metadata"]["course_id"]
    user_id = session["metadata"]["user_id"]

    user = User.objects.get(id=user_id)
    order = get_object_or_404(Order, pk=order_id)
    order.subscribers.add(user)
