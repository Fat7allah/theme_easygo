frappe.ui.form.on('Whitelabel Settings', {
    refresh: function(frm) {
        // Add a preview button for logo and favicon
        frm.add_custom_button(__('Apply Changes'), function() {
            frappe.show_alert({
                message: __('Applying whitelabel changes...'),
                indicator: 'green'
            });
            
            // Reload the page to apply changes
            setTimeout(function() {
                window.location.reload();
            }, 1000);
        });
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
