# http://www.optionistics.com/quotes/stock-option-chains/ (web scrape)
# https://documentation.tradier.com/ (limit 60 calls/min)
#
# Script for data collection
# Felix Hu
################################################################

import numpy as np
import pandas as pd
from urllib.request import urlopen
import json
import datetime