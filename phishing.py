import re
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import tldextract

def check_phishing_url(url):
    suspicious_patterns = [
        'login', 'signin', 'verify', 'account', 'secure',
        'update', 'confirm', 'validate', 'password'
    ]
    
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    
    # IP address in domain
    if re.match(r'\d+\.\d+\.\d+\.\d+', domain):
        return True, "Contains IP address"
    
    # Excessive subdomains
    if len(domain.split('.')) > 3:
        return True, "Excessive subdomains"
    
    # Obfuscation techniques
    if '@' in url:
        return True, "URL contains @ symbol (obfuscation)"
    
    if len(url) > 100:
        return True, "URL is excessively long"
    
    if re.search(r'%[0-9a-fA-F]{2}', url):
        return True, "URL contains hex encoding"

    # Domain analysis
    extracted = tldextract.extract(domain)
    registered_domain = f"{extracted.domain}.{extracted.suffix}"
    if any(pat in domain for pat in suspicious_patterns) and registered_domain != domain:
        return True, "Suspicious subdomain in URL"

    # Check HTTPS
    if not url.startswith('https'):
        return True, "Uses HTTP instead of HTTPS"
    
    try:
        response = requests.get(url, timeout=5)
        
        if not response.url.startswith('https'):
            return True, "Redirects to HTTP"

        soup = BeautifulSoup(response.text, 'html.parser')
        forms = soup.find_all('form')

        for form in forms:
            for input_field in form.find_all('input'):
                if input_field.get('type') == 'hidden':
                    return True, "Hidden form fields detected"

        if 'login' in url.lower() and 'password' in response.text.lower():
            return True, "Potential fake login page"
    
    except requests.exceptions.RequestException as e:
        return False, f"Unable to verify (network error): {str(e)}"

    return False, "No obvious phishing indicators found"
