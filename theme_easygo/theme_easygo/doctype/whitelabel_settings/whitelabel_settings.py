import frappe
from frappe.model.document import Document

class WhitelabelSettings(Document):
    def validate(self):
        self.update_hooks_settings()
        self.update_navbar_settings()
        self.update_login_page()
        self.update_welcome_page()
        
        # Clear cache to apply changes
        frappe.clear_cache()
    
    def update_hooks_settings(self):
        """Update app logo, favicon and other settings in hooks.py"""
        if self.app_logo:
            frappe.db.set_value("Website Settings", "Website Settings", "app_logo", self.app_logo)
        
        if self.favicon:
            frappe.db.set_value("Website Settings", "Website Settings", "favicon", self.favicon)
        
        if self.splash_image:
            frappe.db.set_value("Website Settings", "Website Settings", "splash_image", self.splash_image)
    
    def update_navbar_settings(self):
        """Update navbar settings"""
        # This will be handled by the CSS and JS files
        pass
    
    def update_login_page(self):
        """Update login page title"""
        if self.login_page_title:
            frappe.db.set_value("Website Settings", "Website Settings", "app_name", self.login_page_title)
    
    def update_welcome_page(self):
        """Remove welcome page if configured"""
        if self.remove_welcome_page:
            # Set home page to login
            frappe.db.set_value("Website Settings", "Website Settings", "home_page", "login")
        
        if self.update_welcome_blog:
            # Find and update the welcome blog post
            welcome_blog = frappe.get_all("Blog Post", filters={"title": ["like", "%Welcome%"]}, limit=1)
            if welcome_blog:
                blog = frappe.get_doc("Blog Post", welcome_blog[0].name)
                blog.published = 0  # Unpublish the welcome blog
                blog.save()
