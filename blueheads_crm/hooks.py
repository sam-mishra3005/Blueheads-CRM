app_name = "blueheads_crm"
app_title = "Blueheads CRM"
app_publisher = "Internship Project Team"
app_description = "Customized CRM application for internship project"
app_email = "team@blueheads.local"
app_license = "GPL-3.0"
app_icon_url = "/assets/blueheads_crm/images/logo.svg"
app_icon_title = "Blueheads CRM"
app_icon_route = "/blueheads_crm"

# Apps
# ------------------

# required_apps = []
add_to_apps_screen = [
	{
		"name": "blueheads_crm",
		"logo": "/assets/blueheads_crm/images/logo.svg",
		"title": "Blueheads CRM",
		"route": "/blueheads_crm",
		"has_permission": "blueheads_blueheads_crm.api.check_app_permission",
	}
]

get_site_info = "blueheads_blueheads_crm.activation.get_site_info"

export_python_type_annotations = True
require_type_annotated_api_methods = True

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/blueheads_crm/css/blueheads_crm.css"
# app_include_js = "/assets/blueheads_crm/js/blueheads_crm.js"

# include js, css files in header of web template
# web_include_css = "/assets/blueheads_crm/css/blueheads_crm.css"
# web_include_js = "/assets/blueheads_crm/js/blueheads_crm.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "crm/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
	"Quotation": "public/js/erpnext_quotation_prefill.js",
	"Sales Order": "public/js/erpnext_sales_order_customer.js",
}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# "Role": "home_page"
# }

website_route_rules = [
	{"from_route": "/crm/<path:app_path>", "to_route": "blueheads_crm"},
]

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# "methods": "blueheads_crm.utils.jinja_methods",
# "filters": "blueheads_crm.utils.jinja_filters"
# }

# Setup wizard
# setup_wizard_requires = "assets/crm/js/setup_wizard.js"
# setup_wizard_stages = "blueheads_crm.setup.setup_wizard.setup_wizard.get_setup_stages"
setup_wizard_complete = "blueheads_crm.demo.api.create_demo_data"
# setup_wizard_test = "blueheads_crm.setup.setup_wizard.test_setup_wizard.run_setup_wizard_test"

# Installation
# ------------

before_install = "blueheads_crm.install.before_install"
after_install = "blueheads_crm.install.after_install"

# Uninstallation
# ------------

before_uninstall = "blueheads_crm.uninstall.before_uninstall"
# after_uninstall = "blueheads_crm.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "blueheads_crm.utils.before_app_install"
# after_app_install = "blueheads_crm.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "blueheads_crm.utils.before_app_uninstall"
# after_app_uninstall = "blueheads_crm.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "blueheads_crm.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

permission_query_conditions = {
	"CRM Lead": "blueheads_crm.permissions.org_hierarchy.get_lead_permission_query_conditions",
	"CRM Deal": "blueheads_crm.permissions.org_hierarchy.get_deal_permission_query_conditions",
	"CRM Notification": "blueheads_crm.fblueheads_crm.doctype.crm_notification.crm_notification.get_permission_query_conditions",
}

has_permission = {
	"CRM Lead": "blueheads_crm.permissions.org_hierarchy.has_lead_permission",
	"CRM Deal": "blueheads_crm.permissions.org_hierarchy.has_deal_permission",
	"CRM Notification": "blueheads_crm.fblueheads_crm.doctype.crm_notification.crm_notification.has_permission",
}

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
	"Contact": "blueheads_crm.overrides.contact.CustomContact",
	"Email Template": "blueheads_crm.overrides.email_template.CustomEmailTemplate",
}

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Contact": {
		"validate": ["blueheads_crm.api.contact.validate"],
	},
	"ToDo": {
		"after_insert": ["blueheads_crm.api.todo.after_insert"],
		"on_update": ["blueheads_crm.api.todo.on_update"],
	},
	"Communication": {
		"after_insert": ["blueheads_crm.utils.on_communication_insert"],
		"on_update": ["blueheads_crm.utils.on_communication_update"],
	},
	"Comment": {
		"after_insert": ["blueheads_crm.utils.on_comment_insert"],
		"on_update": ["blueheads_crm.api.comment.on_update"],
	},
	"WhatsApp Message": {
		"validate": ["blueheads_crm.api.whatsapp.validate"],
		"on_update": ["blueheads_crm.api.whatsapp.on_update"],
	},
	"CRM Deal": {
		"on_update": [
			"blueheads_crm.fblueheads_crm.doctype.erpnext_crm_settings.erpnext_crm_settings.create_customer_in_erpnext"
		],
	},
	"Sales Order": {
		"before_validate": [
			"blueheads_crm.fblueheads_crm.doctype.erpnext_crm_settings.erpnext_crm_settings.create_customer_on_sales_order"
		],
	},
	"Item": {
		"after_insert": ["blueheads_crm.integrations.erpnext.item.after_insert"],
		"on_update": ["blueheads_crm.integrations.erpnext.item.on_update"],
		"before_rename": ["blueheads_crm.integrations.erpnext.item.before_rename"],
		"after_rename": ["blueheads_crm.integrations.erpnext.item.after_rename"],
		"on_trash": ["blueheads_crm.integrations.erpnext.item.on_trash"],
	},
	"User Permission": {
		"before_validate": ["blueheads_crm.integrations.erpnext.user_permission.before_validate"],
		"after_insert": ["blueheads_crm.integrations.erpnext.user_permission.after_insert"],
		"on_update": ["blueheads_crm.integrations.erpnext.user_permission.on_update"],
		"on_trash": ["blueheads_crm.integrations.erpnext.user_permission.on_trash"],
	},
	"DocShare": {
		"before_validate": ["blueheads_crm.integrations.erpnext.doc_share.before_validate"],
		"after_insert": ["blueheads_crm.integrations.erpnext.doc_share.after_insert"],
		"on_update": ["blueheads_crm.integrations.erpnext.doc_share.on_update"],
		"on_trash": ["blueheads_crm.integrations.erpnext.doc_share.on_trash"],
	},
	"User": {
		"before_validate": ["blueheads_crm.api.live_demo.validate_user"],
		"validate_reset_password": ["blueheads_crm.api.live_demo.validate_reset_password"],
	},
}

# Scheduled Tasks
# ---------------

scheduler_events = {
	"all": ["blueheads_crm.api.event.trigger_offset_event_notifications"],
	"hourly": ["blueheads_crm.api.event.trigger_hourly_event_notifications"],
	"daily": [
		"blueheads_crm.api.event.trigger_daily_event_notifications",
		"blueheads_crm.fblueheads_crm.doctype.crm_view_settings.crm_view_settings.clear_old_versions",
	],
	"weekly": ["blueheads_crm.api.event.trigger_weekly_event_notifications"],
	"daily_long": ["blueheads_crm.lead_syncing.background_sync.sync_leads_from_sources_daily"],
	"hourly_long": ["blueheads_crm.lead_syncing.background_sync.sync_leads_from_sources_hourly"],
	"monthly_long": ["blueheads_crm.lead_syncing.background_sync.sync_leads_from_sources_monthly"],
	"cron": {
		"*/5 * * * *": ["blueheads_crm.lead_syncing.background_sync.sync_leads_from_sources_5_minutes"],
		"*/10 * * * *": ["blueheads_crm.lead_syncing.background_sync.sync_leads_from_sources_10_minutes"],
		"*/15 * * * *": ["blueheads_crm.lead_syncing.background_sync.sync_leads_from_sources_15_minutes"],
	},
}

# Testing
# -------

before_tests = "blueheads_crm.tests.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# "frappe.desk.doctype.event.event.get_events": "blueheads_crm.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# "Task": "blueheads_crm.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

ignore_links_on_delete = ["Failed Lead Sync Log"]

# Request Events
# ----------------
# before_request = ["blueheads_crm.utils.before_request"]
# after_request = ["blueheads_crm.utils.after_request"]

# Job Events
# ----------
# before_job = ["blueheads_crm.utils.before_job"]
# after_job = ["blueheads_crm.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# {
# "doctype": "{doctype_1}",
# "filter_by": "{filter_by}",
# "redact_fields": ["{field_1}", "{field_2}"],
# "partial": 1,
# },
# {
# "doctype": "{doctype_2}",
# "filter_by": "{filter_by}",
# "partial": 1,
# },
# {
# "doctype": "{doctype_3}",
# "strict": False,
# },
# {
# "doctype": "{doctype_4}"
# }
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# "blueheads_crm.auth.validate"
# ]

after_migrate = [
	"blueheads_crm.fblueheads_crm.doctype.fcrm_settings.fcrm_settings.after_migrate",
	"blueheads_crm.api.whatsapp.add_roles",
	"blueheads_crm.install.add_default_scripts",
]

standard_dropdown_items = [
	{
		"name1": "app_selector",
		"label": "Apps",
		"type": "Route",
		"route": "#",
		"is_standard": 1,
	},
	{
		"name1": "settings",
		"label": "Settings",
		"type": "Route",
		"icon": "settings",
		"route": "#",
		"is_standard": 1,
	},
	{
		"name1": "login_to_fc",
		"label": "Login to Frappe Cloud",
		"type": "Route",
		"route": "#",
		"is_standard": 1,
	},
	{
		"name1": "about",
		"label": "About",
		"type": "Route",
		"icon": "info",
		"route": "#",
		"is_standard": 1,
	},
	{
		"name1": "separator",
		"label": "",
		"type": "Separator",
		"is_standard": 1,
	},
	{
		"name1": "logout",
		"label": "Log out",
		"type": "Route",
		"icon": "log-out",
		"route": "#",
		"is_standard": 1,
	},
]
