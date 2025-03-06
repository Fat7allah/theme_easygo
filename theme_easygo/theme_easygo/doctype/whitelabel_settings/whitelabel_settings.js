// Copyright (c) 2025, Theme Easygo and contributors
// For license information, please see license.txt

frappe.ui.form.on('Whitelabel Settings', {
	refresh: function(frm) {
		// Add preview button
		frm.add_custom_button(__('Preview Changes'), function() {
			frappe.show_alert({
				message: __('Applying whitelabel changes for preview...'),
				indicator: 'green'
			});
			
			// Save the form first
			frm.save();
			
			// Reload the page after a short delay to apply changes
			setTimeout(function() {
				window.location.reload();
			}, 1500);
		});
		
		// Add a section to show current settings
		frm.add_custom_button(__('Reset to Defaults'), function() {
			frappe.confirm(
				__('This will reset all whitelabel settings to default values. Continue?'),
				function() {
					// Reset all fields to default
					frm.set_value('app_logo', '');
					frm.set_value('app_logo_width', 30);
					frm.set_value('favicon', '');
					frm.set_value('splash_image', '');
					frm.set_value('login_page_title', 'Login');
					frm.set_value('hide_powered_by', 0);
					frm.set_value('navbar_background_color', '#083B77');
					frm.set_value('navbar_title', '');
					frm.set_value('navbar_title_css', '');
					frm.set_value('hide_help_menu', 0);
					frm.set_value('remove_welcome_page', 0);
					frm.set_value('update_welcome_blog', 0);
					
					// Save the form
					frm.save();
					
					frappe.show_alert({
						message: __('Settings reset to defaults'),
						indicator: 'green'
					});
				}
			);
		}).addClass('btn-danger');
	},
	
	app_logo_width: function(frm) {
		// Validate logo width
		if (frm.doc.app_logo_width < 20) {
			frappe.msgprint(__('Logo width should be at least 20px'));
			frm.set_value('app_logo_width', 20);
		} else if (frm.doc.app_logo_width > 200) {
			frappe.msgprint(__('Logo width should not exceed 200px'));
			frm.set_value('app_logo_width', 200);
		}
	}
});
