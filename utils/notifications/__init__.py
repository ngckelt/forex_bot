from .notify_admin import notify_admin_about_withdrawal, notify_admin_about_update_deposit, \
    notify_admin_about_one_percent_referral_deposit_update, notify_admin_about_month_deposit_update, \
    notify_admin_about_one_percent_deposit_update
from .notify_client import notify_client_about_failed_withdrawal, notify_client_about_success_withdrawal, \
    notify_client_about_success_deposit_update, notify_client_about_failed_deposit_update, \
    notify_client_about_month_deposit_update
from .notify_referrer import notify_referrer_about_one_percent_deposit_update, \
    notify_referrer_about_month_deposit_update

__all__ = (
    "notify_admin_about_withdrawal",
    "notify_admin_about_update_deposit",
    "notify_client_about_failed_withdrawal",
    "notify_client_about_success_withdrawal",
    "notify_client_about_success_deposit_update",
    "notify_client_about_failed_deposit_update",
    "notify_referrer_about_one_percent_deposit_update",
    "notify_admin_about_one_percent_referral_deposit_update",
    "notify_client_about_month_deposit_update",
    "notify_admin_about_month_deposit_update",
    "notify_referrer_about_month_deposit_update",
    "notify_admin_about_one_percent_deposit_update"
)

