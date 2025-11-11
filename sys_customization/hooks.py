app_name = "sys_customization"
app_title = "Sys Customization"
app_publisher = "Quntbit Technologies pvt ltd"
app_description = "Sys Customizations"
app_email = "quntbit.support@erpdata.in"
app_license = "mit"

website_redirects = [
    {"source": "/jobs/quantbit_technologies_private_limited/hackathon-for-developer-intern-recruitment-", 
     "target": "https://sys1.erpdata.in/quant-quest"}
]
# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "sys_customization",
# 		"logo": "/assets/sys_customization/logo.png",
# 		"title": "Sys Customization",
# 		"route": "/sys_customization",
# 		"has_permission": "sys_customization.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/sys_customization/css/sys_customization.css"
# app_include_js = "/assets/sys_customization/js/sys_customization.js"

# include js, css files in header of web template
# web_include_css = "/assets/sys_customization/css/sys_customization.css"
# web_include_js = "/assets/sys_customization/js/sys_customization.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "sys_customization/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "sys_customization/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "sys_customization.utils.jinja_methods",
# 	"filters": "sys_customization.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "sys_customization.install.before_install"
# after_install = "sys_customization.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "sys_customization.uninstall.before_uninstall"
# after_uninstall = "sys_customization.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "sys_customization.utils.before_app_install"
# after_app_install = "sys_customization.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "sys_customization.utils.before_app_uninstall"
# after_app_uninstall = "sys_customization.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "sys_customization.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"sys_customization.tasks.all"
# 	],
# 	"daily": [
# 		"sys_customization.tasks.daily"
# 	],
# 	"hourly": [
# 		"sys_customization.tasks.hourly"
# 	],
# 	"weekly": [
# 		"sys_customization.tasks.weekly"
# 	],
# 	"monthly": [
# 		"sys_customization.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "sys_customization.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "sys_customization.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "sys_customization.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["sys_customization.utils.before_request"]
# after_request = ["sys_customization.utils.after_request"]

# Job Events
# ----------
# before_job = ["sys_customization.utils.before_job"]
# after_job = ["sys_customization.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"sys_customization.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

