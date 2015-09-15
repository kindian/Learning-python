import urllib.request
import ssl

import certifi


context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
context.verify_mode = ssl.CERT_REQUIRED
context.load_verify_locations(certifi.where())
httpsHandler = urllib.request.HTTPSHandler(context = context)

manager = urllib.request.HTTPPasswordMgrWithDefaultRealm()
manager.add_password(None, 'https://www.facebook.com', 'patra.kailash@yahoo.com', 'jamesbond06')
authHandler = urllib.request.HTTPBasicAuthHandler(manager)

opener = urllib.request.build_opener(httpsHandler, authHandler)

# Used globally for all urllib.request requests.
# If it doesn't fit your design, use opener directly.
urllib.request.install_opener(opener)

response = urllib.request.urlopen('https://www.facebook.com')
print(response.getcode())
