# Changelog for Theme EasyGo

## [Unreleased] - 2025-03-06

### Fixed
- Fixed theme not changing by correcting the CSS file reference in hooks.py
- Renamed CSS file from `corporate_theme.css` to `theme_easygo.css` to match the reference in hooks.py

### Changed
- Updated color scheme to use:
  - Primary color: #083B77 (dark blue)
  - Secondary color: #12549F (medium blue)
  - Background color: #F8F9FA (light gray)
- Replaced hardcoded color values with CSS variables for better consistency and easier future updates
- Improved CSS structure by using variables throughout the stylesheet

## Details of Changes

### 1. CSS File Reference Fix

The theme wasn't changing because there was a mismatch between the CSS file referenced in hooks.py and the actual CSS file name in the project.

**Before:**
```python
# In hooks.py
app_include_css = "/assets/theme_easygo/css/theme_easygo.css"
```

But the actual file was named `corporate_theme.css`.

**After:**
We renamed the file to match the reference:
```
theme_easygo/public/css/theme_easygo.css
```

### 2. Color Scheme Update

Updated the color scheme to use a blue-based palette:

**Before:**
```css
:root {
    --bg-color:  #e5e8eb;
    --btn-primary: #714B67;
    --btn-secondary: #017E8480;
    --secondary: #017E84;
    --navbar-bg: #714B67;
    --text-btn-color: white;
    --table-border-color: #714b6740;
    --btn-default-hover-bg: white;
    --sidebar-select-color: #017E8420;
    --checkbox-gradient: linear-gradient(180deg, var(--btn-primary) -124.51%, var(--btn-primary) 100%);
    --text-base: 14px;
}
```

**After:**
```css
:root {
    --bg-color: #F8F9FA;
    --btn-primary: #083B77;
    --btn-secondary: #12549F80;
    --secondary: #12549F;
    --navbar-bg: #083B77;
    --text-btn-color: white;
    --table-border-color: #083B7740;
    --btn-default-hover-bg: white;
    --sidebar-select-color: #12549F20;
    --checkbox-gradient: linear-gradient(180deg, var(--btn-primary) -124.51%, var(--btn-primary) 100%);
    --text-base: 14px;
}
```

### 3. CSS Variable Usage

Replaced hardcoded color values with CSS variables for better consistency:

**Before:**
```css
.es-icon {
    fill: #017E8480 !important; 
    stroke: #017E8480 !important;
}

.widget.links-widget-box, .widget.dashboard-widget-box {
    border: 1px solid #714B6780;
}
```

**After:**
```css
.es-icon {
    fill: var(--btn-secondary) !important; 
    stroke: var(--btn-secondary) !important;
}

.widget.links-widget-box, .widget.dashboard-widget-box {
    border: 1px solid var(--btn-primary);
}
```

## Git Commits

1. **Fix theme CSS file reference in hooks.py and rename CSS file** (cf84bd1)
   - Changed CSS file reference in hooks.py
   - Renamed corporate_theme.css to theme_easygo.css

2. **Update theme colors to use #083B77, #12549F, #F8F9FA color scheme** (c62494d)
   - Updated root CSS variables to use new color scheme
   - Replaced hardcoded color values with CSS variables
   - Improved consistency across UI elements

## How to Apply Changes

For the changes to take effect in your Frappe installation:

1. Clear the cache:
```
bench --site [your-site-name] clear-cache
```

2. Restart the Frappe server:
```
bench restart
```

## Next Steps

Potential improvements for future work:

1. Add more theme customization options
2. Create a settings page to allow users to change theme colors
3. Add dark mode support
4. Optimize CSS for better performance
5. Add more custom styling for specific Frappe/ERPNext modules
