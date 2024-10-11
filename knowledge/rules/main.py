import os
from bs4 import BeautifulSoup

# Define the path where your folders are located

# Define the new header HTML content

new_header='''    <footer id="rs-footer" class="rs-footer footer-main-home">
      <div class="footer-top">
        <div class="container">
          <div class="row">
            <div class="col-lg-3 md-mb-20">
              <h3 class="footer-title">About Company</h3>
              <div class="textwidget mb-33" style="text-align: justify">
                Kedia Dhandharia & Co established in 1988, offers comprehensive
                accounting, assurance, tax advisory, and consultancy services,
                prioritizing integrity, transparency, and client success.
              </div>
              
            </div>
            <div class="col-lg-3 pl-76 md-pl-15 md-mb-10">
              <h3 class="footer-title">Contact Info</h3>
              <ul class="address-widget">
                <li>
                  <i class="fi fi-rr-map-marker-home"></i>
                  <div class="desc">
                    BC - 266, Sector 1, Salt Lake City, Kolkata, West Bengal 700064
                  </div>
                </li>
                <li>
                  <i class="fi fi-rr-phone-call"></i>
                  <div class="desc">
                    <a href="tel:033-2359-5641">033-2359-5641 / 42</a>
                  </div>
                </li>
                <li>
                  <i class="fi fi-rr-envelope-plus"></i>
                  <div class="desc">
                    <a href="mailto:info@kediadhandharia.in">info@kediadhandharia.in</a>
                  </div>
                </li>
              </ul>
            </div>
            <div class="col-lg-3 pl-75 md-pl-15 md-mb-10">
              <h3 class="footer-title">Our Services</h3>
              <ul class="site-map">
                <li>
                  <a href="/services/finance-and-accounting/">Finance & Accounting</a>
                </li>
                <li><a href="/services/indirect-taxes/">Indirect Taxes</a></li>
                <li>
                  <a href="/services/audit-and-insurance/">Audit </a>
                </li>
                <li><a href="/services/direct-taxes/">Direct Taxes</a></li>
                <li>
                  <a href="/services/corporate-law/">Corporate Law & Compliances</a>
                </li>
              </ul>
            </div>
            <div class="col-lg-3">
              <h3 class="footer-title">Our Resources</h3>
              <ul class="site-map">
                <li><a href="/about/about-company/">About Company</a></li>
                <li><a href="/about/our-clients/">Our Clients</a></li>
                <li><a href="/careers/">Careers</a></li>
                <li><a href="/contact/">Contact Us</a></li>
                <li><a href="/blogs/">Our Blogs</a></li>
              </ul>
            </div>
          </div>
        </div>
      </div>
      <div class="footer-bottom">
        <div class="container">
          <div class="row y-middle">
            
          
              <div class="copyright text-center">
                <p>
                  © 2024 Kedia Dhandharia & Co Designed By
                  <a href="https://www.switchhigh.com/" target="blank"
                    >SwitchHigh</a
                  >
                </p>
              </div>
            
          </div>
        </div>
      </div>
    </footer>'''
# Function to modify the header in the index.html file
root_directory = os.getcwd() 
def modify_html_file(file_path):
    try:
        # Open the index.html file and parse its content using BeautifulSoup
        with open(file_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')

        # Find the existing header tag and replace it with the new one
        header_div = soup.find('footer')
        if header_div:
            header_div.replace_with(BeautifulSoup(new_header, 'html.parser'))

        # Write the modified HTML content back to the index.html file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(str(soup.prettify()))
        
        print(f'Modified header in: {file_path}')
    
    except Exception as e:
        print(f'Error modifying {file_path}: {e}')

# Walk through all folders and subfolders
for root, dirs, files in os.walk(root_directory):
    for file_name in files:
        if file_name == 'index.html':  # Check if it's an index.html file
            file_path = os.path.join(root, file_name)
            print(file_path)
            modify_html_file(file_path)  # Modify the header in the file
