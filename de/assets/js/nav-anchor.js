// Auto-scroll to #first anchor for "First Time Login" menu item
document.addEventListener('DOMContentLoaded', function() {
  // Find all navigation links
  const navLinks = document.querySelectorAll('nav a, .md-tabs__link');
  
  navLinks.forEach(link => {
    // Check if this is the "First Time Login" link
    if (link.textContent.trim() === 'First Time Login') {
      const href = link.getAttribute('href');
      // Add #first anchor if not already present
      if (href && !href.includes('#first')) {
        link.setAttribute('href', href + '#first');
      }
    }
  });
});

