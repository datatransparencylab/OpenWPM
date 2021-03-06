from automation import TaskManager

# The list of sites that we wish to crawl
NUM_BROWSERS = 3
sites = ['http://www.example.com',
         'http://www.princeton.edu',
         'https://citp.princeton.edu/']

# Loads the manager preference and 3 copies of the default browser dictionaries
manager_params, browser_params = TaskManager.load_default_params(NUM_BROWSERS)

# Update browser configuration (use this for per-browser settings)
for i in xrange(NUM_BROWSERS):
    browser_params[i]['disable_flash'] = False #Enable flash for all three browsers
browser_params[0]['headless'] = True #Launch only browser 0 headless

# Update TaskManager configuration (use this for crawl-wide settings)
manager_params['data_directory'] = '~/Desktop/'
manager_params['log_directory'] = '~/Desktop/'

# Instantiates the measurement platform
# Commands time out by default after 60 seconds
manager = TaskManager.TaskManager(manager_params, browser_params)

# Visits the sites with both browsers simultaneously
for site in sites:
    manager.get(site, index='**') # ** = synchronized browsers

# Shuts down the browsers and waits for the data to finish logging
manager.close()
