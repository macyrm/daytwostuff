# Open the Codespace in your local VS Code
# 5. What is your terminal display "path"? (type/paste as text into the .py file)
# @macyrm ➜ /workspaces/daytwostuff (main) $ 

# Create a virtual environment
# 4. Should you include the environment in your repo or not?
# No, you should not include the environment in your repo because all of the packages used by the environment are already listed in requirements.txt. I included my environment in the .gitignore file.

# 5. Now what is your terminal display "path"? Is it different?
# My terminal display path is only slightly different. It is now "(myenv) @macyrm ➜ /workspaces/daytwostuff (main) $ ".

# Extension Management
# 2. Find the extension in the extension menu. What do you notice about the extension menu?
# In addition to showing which extensions are already downloaded and enabled, the extension menu suggests more extensions to download.

# 3. Review the capabilities, what are three useful elements of Data Wrangler
# Data Wrangler makes csv files easier to read within vscode, allows easy dataset editing, and provides a summary of statistics for the dataset.

# Package managing
# 5. Why do we use a requirements.txt file?
# We use a requirements.txt file so that someone else accessing the repository can download the exact packages used when creating the project to their virtual environment, ensuring it will work for someone else. 

import pandas as pd

data = pd.read_csv('ChocolateSales.csv')