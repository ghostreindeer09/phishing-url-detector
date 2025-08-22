<h1>🔍 Phishing URL Detector</h1>

<p>A Python script to detect potentially malicious or phishing URLs using heuristic analysis of URL structure and webpage content.</p>

<hr>

<h2>📌 Features</h2>
<ul>
  <li>Detects IP addresses used as domains</li>
  <li>Checks for suspicious keywords in URLs</li>
  <li>Validates HTTPS usage</li>
  <li>Analyzes webpage content for hidden fields and fake login forms</li>
  <li>Identifies potential phishing redirects</li>
</ul>

<hr>

<h2>🚀 Getting Started</h2>

<h3>🔧 Prerequisites</h3>
<ul>
  <li>Python 3.x</li>
  <li>Install required libraries:</li>
</ul>

<pre>
pip install requests beautifulsoup4 tldextract
</pre>

<h3>📄 Usage</h3>

<pre>
python phishing_detector.py
</pre>

<p>Edit the <code>url</code> variable in the script to test a specific URL:</p>

<pre>
url = "https://example.com/login"
is_phishing, reason = check_phishing_url(url)
print(f"Phishing detected: {is_phishing}, Reason: {reason}")
</pre>

<hr>

<h2>🛡️ How It Works</h2>
<ol>
  <li>Parses and analyzes the URL structure</li>
  <li>Checks for suspicious keywords and IP usage</li>
  <li>Makes a request and inspects HTML forms and input fields</li>
  <li>Detects potential phishing indicators such as hidden password fields and fake login pages</li>
</ol>

<hr>

<h2>📁 File Structure</h2>
<ul>
  <li><code>phishing_detector.py</code> - Main script</li>
  <li><code>README.md</code> - Project documentation (this file)</li>
</ul>

<hr>

<h2>🔐 <u><em><strong>Important Disclaimer</strong></em></u></h2>

<div style="border: 2px solid red; padding: 10px; background-color: #fff3f3;">
  <p><strong><em>⚠️ This tool is for educational and testing purposes only.</em></strong></p>
  <p><strong>It uses heuristic checks and is <u>not guaranteed</u> to detect all phishing URLs.</strong></p>
  <p><strong>Do <u>not</u> rely on this tool in production environments or as a substitute for professional security solutions.</strong></p>
</div>

<hr>

<h2>📄 License</h2>
<p>This project is licensed under the MIT License.</p>
