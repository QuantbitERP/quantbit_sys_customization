# Copyright (c) 2025, Quntbit Technologies Pvt Ltd and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Registrations(Document):

	def before_save(self):
		if self.collage == "KIT's College of Engineering, Kolhapur":
			email_list = [i.email_address for i in self.table_rono]
			if not self.registration_mail:
				message = f"""
				<html>
					<head>
						<meta charset="utf-8">
						<title>Registration Successful - Quant-Quest 2025 – Hackathon</title>
					</head>
					<body style="font-family: Arial, Helvetica, sans-serif; background-color: #f7f8fa; margin: 0; padding: 0;">
						<table role="presentation" cellpadding="0" cellspacing="0" width="100%" style="background-color: #f7f8fa; padding: 24px 0;">
							<tr>
								<td align="center">
									<table role="presentation" cellpadding="0" cellspacing="0" width="600" style="background-color: #ffffff; border-radius: 8px; padding: 32px; box-shadow: 0 2px 6px rgba(0,0,0,0.08);">
										<tr>
											<td style="font-size: 15px; color: #333;">
												<h2 style="margin-top: 0; color: #0b5cff;">Registration Successful - Quant-Quest 2025 – Hackathon</h2>
												<p style="font-size: 16px; margin: 0 0 16px 0;">Hi Team <strong>{self.group_name}</strong>,</p>
												<p style="margin: 0 0 16px 0;">
													Thank you for registering for <strong>Quantbit's Quant-Quest 2025 🎉</strong><br>
													Your registration has been successfully received.
												</p>
												<p style="margin: 0 0 16px 0;">
													We're excited to have you on board for this challenge of <strong>Innovation, Logic, and Programming Excellence!</strong>
												</p>
												<p style="margin: 0 0 16px 0; line-height: 1.6;">
													📅 <strong>Event:</strong> Quant Quest – Hackathon & Quiz Contest<br>
													🏢 <strong>Organizer:</strong> Quantbit Technologies Pvt Ltd<br>
													📧 <strong>Contact:</strong> 
													<a href="mailto:quantquest@erpdata.in" style="color:#0b5cff; text-decoration:none;">quantquest@erpdata.in</a> (for any queries)
												</p>
												<p style="margin: 0 0 16px 0;">
													Please keep an eye on your inbox for further updates, contest schedule, and participation guidelines.
												</p>
												<p style="margin: 0 0 24px 0;">
													💬 <strong>Join our official Telegram group for live updates and announcements:</strong><br>
													<a href="https://t.me/+z7oOunRr22w0NGFl" target="_blank" style="display: inline-block; background-color: #0088cc; color: #ffffff; padding: 10px 20px; border-radius: 6px; text-decoration: none; font-weight: bold;">
														👉 Join Telegram Group
													</a>
												</p>
												<p style="margin: 0 0 16px 0;">
													We wish you the very best — get ready to <strong>Code, Innovate, Win 💪</strong>
												</p>
												<p style="margin: 24px 0 8px 0;">
													Best regards,<br>
													<strong>Quantbit Technologies Pvt. Ltd.</strong>
												</p>
											</td>
										</tr>
									</table>
								</td>
							</tr>
						</table>
					</body>
				</html>
				"""

				frappe.sendmail(
					recipients=[self.group_leader_email_address] + email_list,
					subject='QUANTBIT HACKATHON - Quant Quest 2025',
					message=message,
					delayed=True,
					reference_doctype="Registrations",
					reference_name=self.name,
				)
				self.registration_mail = 1

		if self.collage == "KIT's College of Engineering, Kolhapur":
			email_list = [i.email_address for i in self.table_rono]
			if not self.problem_statement:
				message = f"""
				<!DOCTYPE html>
				<html>
				<head>
					<meta charset="UTF-8">
					<title>Quant-Quest 2025 – Problem Statements & Submission Details</title>
					<style>
						body {{
							font-family: Arial, Helvetica, sans-serif;
							line-height: 1.6;
							color: #333333;
							background-color: #f8f9fa;
							margin: 0;
							padding: 20px;
						}}
						.container {{
							background: #ffffff;
							padding: 30px;
							border-radius: 8px;
							box-shadow: 0 2px 6px rgba(0,0,0,0.1);
							max-width: 700px;
							margin: 0 auto;
						}}
						h1 {{
							color: #004aad;
							text-align: center;
						}}
						p {{
							margin: 12px 0;
						}}
						ul {{
							margin: 10px 0 10px 25px;
						}}
						a {{
							color: #004aad;
							text-decoration: none;
						}}
						a:hover {{
							text-decoration: underline;
						}}
						.footer {{
							margin-top: 25px;
							font-size: 14px;
							color: #666;
							text-align: center;
						}}
					</style>
				</head>
				<body>
					<div class="container">
						<h1>Quant-Quest 2025</h1>
						<h3>Problem Statements</h3>

						<p style="font-size: 16px; margin: 0 0 16px 0;">Hi Team <strong>{self.group_name}</strong>,</p>

						<p>
							Please find attached the set of <strong>problem statements</strong> for this year’s hackathon.
							You are required to <strong>choose and solve any one</strong> of them.
							Go through each problem carefully before deciding which one to work on.
						</p>

						<p><strong>Key Instructions:</strong></p>
						<ul>
							<li>Review all problem statements thoroughly.</li>
							<li>Select one problem that best matches your interests and skills.</li>
							<li>You may participate individually or in teams (as per event guidelines).</li>
							<li>We have suggested a few preferred tech stacks, but you are free to choose your own.</li>
						</ul>

						<p>
							If you have any doubts or need clarifications about any of the problem statements,
							reach out to us at 
							<a href="mailto:quantquest@erpdata.in">quantquest@erpdata.in</a> 
							or post your queries in the Telegram group:
							<a href="https://t.me/+z7oOunRr22w0NGFl" target="_blank" style="display: inline-block; background-color: #0088cc; color: #ffffff; padding: 10px 20px; border-radius: 6px; text-decoration: none; font-weight: bold;">
								👉 Join Telegram Group
							</a>.
						</p>

						<div class="footer">
							<p>Best regards,<br>
							<strong>Team Quant-Quest 2025</strong></p>
						</div>
					</div>
				</body>
				</html>
				"""

				frappe.sendmail(
					recipients=[self.group_leader_email_address] + email_list,
					subject='Problem Statements - QUANTBIT HACKATHON - Quant Quest 2025',
					message=message,
					delayed=True,
					reference_doctype="Registrations",
					reference_name=self.name,
					attachments=[{"fid": "fa499a805c"}]
				)
				self.problem_statement = 1
