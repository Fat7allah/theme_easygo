import frappe
import os
import re
from frappe.utils import get_site_path

def generate_whitelabel_css():
    """Generate CSS based on whitelabel settings"""
    if not frappe.db.exists("DocType", "Whitelabel Settings"):
        return
    
    try:
        # Get whitelabel settings
        settings = frappe.get_single("Whitelabel Settings")
        
        # Path to the CSS file
        css_path = os.path.join(get_site_path('public', 'files'), 'whitelabel_custom.css')
        
        # Generate CSS content
        css_content = []
        css_content.append(":root {")
        
        # Navbar background color
        if settings.navbar_background_color:
            css_content.append(f"  --navbar-bg-color: {settings.navbar_background_color};")
        
        # App logo width
        if settings.app_logo_width:
            css_content.append(f"  --app-logo-width: {settings.app_logo_width}px;")
        
        css_content.append("}")
        
        # Custom navbar title CSS
        if settings.navbar_title_css:
            css_content.append("/* Custom navbar title CSS */")
            css_content.append(".navbar-brand {")
            css_content.append(f"{settings.navbar_title_css}")
            css_content.append("}")
        
        # Hide help menu
        if settings.hide_help_menu:
            css_content.append("/* Hide help menu */")
            css_content.append(".dropdown-help { display: none !important; }")
        
        # Hide powered by text
        if settings.hide_powered_by:
            css_content.append("/* Hide powered by text */")
            css_content.append(".web-footer .footer-powered { display: none !important; }")
        
        # Write CSS to file
        with open(css_path, 'w') as f:
            f.write('\n'.join(css_content))
        
        # Update onboarding steps (Version 13)
        update_onboarding_steps()
        
        return css_path
    except Exception as e:
        frappe.log_error(f"Error generating whitelabel CSS: {e}", "Whitelabel CSS Generation")

def update_onboarding_steps():
    """Update onboarding steps to remove video and documentation links (Version 13)"""
    try:
        # Check if we're on version 13
        if frappe.utils.cint(frappe.__version__.split('.')[0]) >= 13:
            # Find all onboarding steps
            onboarding_steps = frappe.get_all("Onboarding Step", fields=["name", "path", "is_complete"])
            
            for step in onboarding_steps:
                if not step.is_complete and step.path and ("video" in step.path.lower() or "documentation" in step.path.lower()):
                    # Mark the step as complete to skip it
                    doc = frappe.get_doc("Onboarding Step", step.name)
                    doc.is_complete = 1
                    doc.save(ignore_permissions=True)
    except Exception as e:
        frappe.log_error(f"Error updating onboarding steps: {e}", "Whitelabel Onboarding Update")

def apply_custom_navbar_title():
    """Apply custom navbar title if set"""
    try:
        if frappe.db.exists("DocType", "Whitelabel Settings"):
            settings = frappe.get_single("Whitelabel Settings")
            if settings.navbar_title:
                return settings.navbar_title
    except Exception:
        pass
    
    return None
